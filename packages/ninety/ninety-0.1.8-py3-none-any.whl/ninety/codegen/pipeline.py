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
        """Initialize pipeline components."""
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        
        self.instructions = pd.read_csv(instructions_path)["instruction"].tolist()
        self.generator = CodeGenerator(
            model_name=output_model,
            sample_k=samples,
            temperature=0.7,
            api_key=api_key
        )
        self.language = language
        self.syntax_check = syntax_check
        if syntax_check:
            self.syntax_checker = SyntaxChecker()
            self.judge = JudgeLLM(judge_model)
        else:
            self.syntax_checker = None
            self.judge = None
            
    def run(self) -> pd.DataFrame:
        """Run the pipeline and return results as a DataFrame."""
        # Print cool ASCII art
        print("\033[36m" + NINETY_ASCII + "\033[0m")  # Cyan color
        print("\033[1mStarting code generation pipeline\033[0m\n")  # Bold
        
        results = []
        total = len(self.instructions)
        start_time = time.time()
        
        # Stats tracking
        total_samples = total * self.generator.sample_k
        generated = 0
        syntax_failed = 0
        judge_failed = 0
        
        for idx, instruction in enumerate(self.instructions, 1):
            # Print current stage
            sys.stdout.write("\033[K")  # Clear line
            print(f"[{idx}/{total}] Generating code: {instruction[:60]}..." + "\r", end="")
            
            # Generate code
            outputs = self.generator.generate_batch([instruction])
            generated += len(outputs[0])
            
            for code in outputs[0]:
                code = CodeExtractor.extract_code(code, self.language)
                
                # Validate if requested
                if self.syntax_check:
                    sys.stdout.write("\033[K")  # Clear line
                    print(f"[{idx}/{total}] Syntax validation..." + "\r", end="")
                    
                    if not self.syntax_checker.check(code, self.language):
                        syntax_failed += 1
                        continue
                        
                    sys.stdout.write("\033[K")  # Clear line
                    print(f"[{idx}/{total}] Correctness check..." + "\r", end="")
                    
                    if self.judge.judge(instruction, code) != "pass":
                        judge_failed += 1
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
        print("\n\033[32mGeneration complete\033[0m")  # Green color
        print(f"\nPipeline Statistics:")
        print(f"Time elapsed: {elapsed:.1f}s")
        print(f"Instructions processed: {total}")
        
        print(f"\nSample Breakdown:")
        print(f"Total samples attempted: {total_samples}")
        print(f"Successfully generated: {generated}")
        if self.syntax_check:
            print(f"Failed syntax check: {syntax_failed}")
            print(f"Failed correctness check: {judge_failed}")
        print(f"Final valid samples: {samples_generated}")
        
        success_rate = samples_generated/total_samples * 100
        print(f"\nSuccess Rates:")
        print(f"Generation rate: {generated/total_samples*100:.1f}%")
        if self.syntax_check:
            syntax_pass = generated - syntax_failed
            judge_pass = syntax_pass - judge_failed
            print(f"Syntax pass rate: {syntax_pass/generated*100:.1f}%")
            print(f"Correctness pass rate: {judge_pass/syntax_pass*100:.1f}%")
        print(f"Overall success rate: {success_rate:.1f}%")
        
        # Save results
        if not df.empty:
            df.to_json("output.jsonl", orient="records", lines=True)
            print(f"\nSaved {len(df)} code samples to output.jsonl")
        else:
            print("\nNo valid code samples generated")
            
        return df
