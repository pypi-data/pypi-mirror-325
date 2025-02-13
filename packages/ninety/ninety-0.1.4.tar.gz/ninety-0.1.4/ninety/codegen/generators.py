"""Code generation using OpenAI API."""

from typing import List, Optional
import os
import openai
from openai import OpenAI

class CodeGenerator:
    """Generates code using OpenAI API."""
    
    def __init__(
        self, 
        model_name: str = "gpt-3.5-turbo",
        sample_k: int = 1,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        api_key: Optional[str] = None
    ):
        """Initialize code generator.
        
        Args:
            model_name: OpenAI model to use
            sample_k: Number of samples to generate per prompt
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum tokens to generate
            api_key: Optional OpenAI API key. If not provided, 
                     will use the default from environment
        """
        # Prioritize passed API key, then environment variable
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            # Try to get API key from environment
            env_api_key = os.environ.get("OPENAI_API_KEY")
            if not env_api_key:
                raise ValueError(
                    "OpenAI API key not found. Either pass api_key parameter "
                    "or set OPENAI_API_KEY environment variable."
                )
            self.client = OpenAI(api_key=env_api_key)
        
        self.model = model_name
        self.sample_k = sample_k
        self.temperature = temperature
        self.max_tokens = max_tokens
        
    def generate_batch(self, prompts: List[str]) -> List[List[str]]:
        """Generate code for a batch of prompts.
        
        Args:
            prompts: List of natural language prompts
            
        Returns:
            List of lists, where each inner list contains generated samples for one prompt
        """
        all_outputs = []
        
        for prompt in prompts:
            outputs = []
            
            for _ in range(self.sample_k):
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful coding assistant. Generate only code without any explanation."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens
                )
                outputs.append(response.choices[0].message.content)
                
            all_outputs.append(outputs)
            
        return all_outputs
