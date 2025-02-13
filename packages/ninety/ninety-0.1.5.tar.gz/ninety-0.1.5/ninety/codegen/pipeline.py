"""Pipeline for generating and validating code."""

import json
from typing import List, Dict, Any, Optional, Literal
from tqdm import tqdm
import pandas as pd
import openai
import os

from .generators import CodeGenerator
from .validators import SyntaxChecker, JudgeLLM
from .utils import CodeExtractor

# Supported languages
SUPPORTED_LANGUAGES = Literal["Python", "SQL", "Verilog"]

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
            
    def run(self) -> pd.DataFrame:
        """Run the pipeline and return results as a DataFrame."""
        results = []
        
        print("\nGenerating code...")
        for instruction in tqdm(self.instructions):
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
                    "language": self.language
                })
                
        # Convert to DataFrame
        df = pd.DataFrame(results)
        
        # Save results
        if not df.empty:
            df.to_json("output.jsonl", orient="records", lines=True)
            print(f"\nSaved {len(df)} code samples to output.jsonl")
        else:
            print("\nNo valid code samples generated")
            
        return df
