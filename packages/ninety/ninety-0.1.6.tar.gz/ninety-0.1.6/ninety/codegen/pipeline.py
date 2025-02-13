"""Pipeline for generating and validating code."""

import json
from typing import List, Dict, Any, Optional, Literal
from tqdm import tqdm
import pandas as pd
import openai
import os
import time
import sys
from datetime import datetime

from .generators import CodeGenerator
from .validators import SyntaxChecker, JudgeLLM
from .utils import CodeExtractor

# Supported languages
SUPPORTED_LANGUAGES = Literal["Python", "SQL", "Verilog"]

# ASCII Art
NINETY_ASCII = """
  ___     ___   ___   ___
 / _ \\   / _ \\  \\  \\ /  /
| (_) | | | | |  \\  V  / 
 \\__, | | | | |   >   <  
   / /  | |_| |  /  .  \\ 
  /_/    \\___/  /__/ \\__\\
"""

GENERATING_FRAMES = [
    "⠋ Generating code outputs...",
    "⠙ Running syntax validation...",
    "⠹ Checking code correctness...",
    "⠸ Processing results..."
]

class Pipeline:
    """Orchestrates the code generation and validation pipeline."""
    
    def __init__(
        self, 
        instructions_path: str,
        *,  # Force keyword arguments
        api_key: Optional[str] = None,
        output_model: str = "gpt-3.5-turbo",  # Model for code generation
        judge_model: str = "gpt-3.5-turbo",   # Model for code validation
        language: SUPPORTED_LANGUAGES = "Python",
        syntax_check: bool = True,
        samples: int = 1,
    ):
        """Initialize pipeline components.
        
        Args:
            instructions_path: Path to CSV file with instructions
            api_key: Optional OpenAI API key. If not provided, 
                     will use the default from environment
            output_model: OpenAI model for code generation
            judge_model: OpenAI model for code validation
            language: Target programming language
            syntax_check: Whether to validate syntax and correctness
            samples: Number of samples to generate per instruction
        """
        # Set API key if provided
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        
        # Read instructions
        self.instructions = pd.read_csv(instructions_path)["instruction"].tolist()
        
        # Initialize generator with reasonable defaults
        self.generator = CodeGenerator(
            model_name=output_model,
            sample_k=samples,
            temperature=0.7,
            api_key=api_key  # Pass API key to generator
        )
        
        self.language = language
        self.syntax_check = syntax_check
        
        # Only create validators if needed
        if syntax_check:
            self.syntax_checker = SyntaxChecker()
            self.judge = JudgeLLM(judge_model)
        else:
            self.syntax_checker = None
            self.judge = None
            
    def _print_with_animation(self, frame_idx: int) -> None:
        """Print animated frame."""
        sys.stdout.write("\033[K")  # Clear line
        print(GENERATING_FRAMES[frame_idx], end="\r")
        
    def run(self) -> pd.DataFrame:
        """Run the pipeline and return results as a DataFrame."""
        # Print cool ASCII art
        print("\033[36m" + NINETY_ASCII + "\033[0m")  # Cyan color
        print("\033[1m🚀 Starting code generation pipeline...\033[0m\n")  # Bold
        
        results = []
        total = len(self.instructions)
        frame_idx = 0
        start_time = time.time()
        
        for idx, instruction in enumerate(self.instructions, 1):
            # Update animation
            self._print_with_animation(frame_idx)
            frame_idx = (frame_idx + 1) % len(GENERATING_FRAMES)
            
            # Generate code
            outputs = self.generator.generate_batch([instruction])
            
            for code in outputs[0]:
                code = CodeExtractor.extract_code(code, self.language)
                
                # Validate if requested
                if self.syntax_check:
                    if not self.syntax_checker.check(code, self.language):
                        continue
                    if self.judge.judge(instruction, code) != "pass":
                        continue
                        
                results.append({
                    "instruction": instruction,
                    "code": code,
                    "language": self.language,
                    "timestamp": datetime.now().isoformat()
                })
            
            # Print progress
            progress = int(50 * idx / total)
            sys.stdout.write("\033[K")  # Clear line
            print(f"Progress: [{'=' * progress}{' ' * (50-progress)}] {idx}/{total}", end="\r")
        
        # Convert to DataFrame
        df = pd.DataFrame(results)
        
        # Calculate stats
        elapsed = time.time() - start_time
        samples_generated = len(df)
        
        # Clear progress line
        sys.stdout.write("\033[K")
        
        # Print completion message with stats
        print("\n\033[32m✨ Generation complete!\033[0m")  # Green color
        print(f"\n📊 Statistics:")
        print(f"   • Time elapsed: {elapsed:.1f}s")
        print(f"   • Instructions processed: {total}")
        print(f"   • Code samples generated: {samples_generated}")
        print(f"   • Success rate: {samples_generated/(total*self.generator.sample_k)*100:.1f}%")
        
        # Save results
        if not df.empty:
            df.to_json("output.jsonl", orient="records", lines=True)
            print(f"\n💾 Saved {len(df)} code samples to output.jsonl")
        else:
            print("\n⚠️  No valid code samples generated")
            
        return df
