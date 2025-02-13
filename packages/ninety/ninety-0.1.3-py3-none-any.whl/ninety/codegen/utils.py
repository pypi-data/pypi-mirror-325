"""Utility functions for code processing."""

import re
import json
from typing import Dict, Any, List

class CodeExtractor:
    """Extracts code from LLM responses."""
    
    @staticmethod
    def extract_code(response_text: str, language: str) -> str:
        """Extract code from markdown-formatted LLM response.
        
        Args:
            response_text: Raw LLM response text
            language: Programming language to extract
            
        Returns:
            Extracted code string
        """
        code_pattern = re.compile(
            r"```" + language.lower() + r"\n(.*?)```", 
            re.DOTALL
        )
        match = code_pattern.search(response_text)
        
        if match:
            return match.group(1).strip()
        return response_text.strip()

class OutputSaver:
    """Saves generated outputs to file."""
    
    @staticmethod
    def save(dataset: List[Dict[str, Any]], output_path: str = "output.jsonl"):
        """Save dataset to JSONL file.
        
        Args:
            dataset: List of data dictionaries to save
            output_path: Path to save output file
        """
        with open(output_path, "w") as f:
            for row in dataset:
                f.write(json.dumps(row) + "\n")
