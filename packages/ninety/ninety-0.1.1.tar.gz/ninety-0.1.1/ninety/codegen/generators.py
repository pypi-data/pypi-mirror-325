"""Code generation components using OpenAI."""

from openai import OpenAI
from typing import List, Optional
import os

class ModelLoader:
    """Singleton model loader to ensure efficient model sharing."""
    
    _instances = {}
    
    def __new__(cls, model_name: str = "gpt-3.5-turbo"):
        if model_name not in cls._instances:
            cls._instances[model_name] = super(ModelLoader, cls).__new__(cls)
            cls._instances[model_name]._initialize_model(model_name)
        return cls._instances[model_name]
        
    def _initialize_model(self, model_name: str):
        """Initialize the OpenAI model.
        
        Args:
            model_name: OpenAI model to use
        """
        self.model_name = model_name
        
        # Set API key from environment
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        self.client = OpenAI(api_key=api_key)
        
    def get_model(self) -> str:
        """Get the loaded OpenAI model name.
        
        Returns:
            OpenAI model name
        """
        return self.model_name

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
            sample_k: Number of samples to generate per instruction
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum tokens to generate
            api_key: Optional OpenAI API key. If not provided, 
                     will use the default from environment
        """
        self.model_loader = ModelLoader(model_name)
        self.model_name = self.model_loader.get_model()
        self.sample_k = sample_k
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # Set API key if provided
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = self.model_loader.client
        
    def generate_batch(self, instructions: List[str]) -> List[List[str]]:
        """Generate multiple outputs for a batch of instructions.
        
        Args:
            instructions: List of instruction strings
            
        Returns:
            List of lists containing generated outputs
        """
        all_outputs = []
        
        for instruction in instructions:
            outputs = []
            for _ in range(self.sample_k):
                completion = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": "You are a code generation assistant. Generate only the code, without any explanation."},
                        {"role": "user", "content": instruction}
                    ],
                    temperature=self.temperature,
                    max_tokens=self.max_tokens
                )
                outputs.append(completion.choices[0].message.content)
            all_outputs.append(outputs)
            
        return all_outputs
