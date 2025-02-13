"""Configuration loader for the Codegen SDK."""

import json
import pandas as pd
from typing import Any, Dict, Optional, List

class ConfigLoader:
    """Loads and manages configuration for the codegen pipeline."""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize config loader.
        
        Args:
            config_path: Path to JSON configuration file
        """
        with open(config_path, "r") as f:
            self.config = json.load(f)
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key.
        
        Args:
            key: Configuration key to retrieve
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get("config", {}).get(key, default)
    
    def get_instruction_file(self) -> str:
        """Get path to instruction input file.
        
        Returns:
            Path to instruction file
        """
        return self.config["instructions_file"]
        
    def load_instructions(self) -> List[str]:
        """Load instructions from configured file.
        
        Returns:
            List of instruction strings
        """
        df = pd.read_csv(self.get_instruction_file())
        return df["instruction"].tolist()
