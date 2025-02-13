"""Validation components for generated code."""

import ast
import sqlparse
from pyverilog.vparser.parser import parse
from openai import OpenAI
from typing import Optional
import os

class SyntaxChecker:
    """Validates syntax for different programming languages."""
    
    @staticmethod
    def check(code: str, lang: str) -> bool:
        """Check if code has valid syntax for given language.
        
        Args:
            code: Code string to validate
            lang: Programming language to validate against
            
        Returns:
            True if syntax is valid, False otherwise
        """
        try:
            if lang.lower() == "python":
                ast.parse(code)
            elif lang.lower() == "sql":
                sqlparse.parse(code)
            elif lang.lower() == "verilog":
                parse([code])
            return True
        except:
            return False

class JudgeLLM:
    """Uses OpenAI to judge code correctness."""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        """Initialize judge LLM.
        
        Args:
            model_name: OpenAI model to use
        """
        self.model_name = model_name
        
        # Try to get API key from environment
        env_api_key = os.environ.get("OPENAI_API_KEY")
        if not env_api_key:
            raise ValueError(
                "OpenAI API key not found. Either set OPENAI_API_KEY environment variable "
                "or pass api_key parameter to Pipeline."
            )
        self.client = OpenAI(api_key=env_api_key)
        
    def judge(self, instruction: str, code: str) -> str:
        """Judge if generated code correctly solves instruction.
        
        Args:
            instruction: Original instruction
            code: Generated code to evaluate
            
        Returns:
            'pass' or 'fail' judgment
        """
        prompt = (
            f"Does this code correctly solve the instruction?\n\n"
            f"Instruction: {instruction}\n"
            f"Code:\n{code}\n\n"
            f"Answer only with 'pass' or 'fail'."
        )
        
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a code review assistant. Evaluate if the code correctly solves the given instruction. Only respond with 'pass' or 'fail'."},
                {"role": "user", "content": prompt}
            ]
        )
        
        judge_response = completion.choices[0].message.content.lower().strip()
        return "pass" if "pass" in judge_response else "fail"
