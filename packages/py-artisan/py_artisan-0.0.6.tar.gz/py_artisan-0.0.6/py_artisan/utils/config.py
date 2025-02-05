"""Configuration management module"""
import os
from typing import Any, Optional
from dotenv import load_dotenv

class Config:
    """Configuration management class"""
    
    @staticmethod
    def get_env(key: str, description: str = None) -> Any:
        """
        Get environment variable value
        
        Args:
            key: Environment variable name
            description: Environment variable description for error message
            
        Returns:
            Any: Environment variable value
            
        Raises:
            ValueError: When environment variable is not set
            
        Examples:
            >>> api_key = Config.get_env('OPENAI_API_KEY', 'OpenAI API Key')
            >>> base_url = Config.get_env('OLLAMA_BASE_URL', 'Ollama Service URL')
        """
        value = os.getenv(key)
        if value is None:
            desc = f" ({description})" if description else ""
            raise ValueError(f"Environment variable {key}{desc} is not set")
        return value

    @staticmethod
    def load_env(env_path: Optional[str] = None) -> bool:
        """
        Load environment variables from .env file
        
        Args:
            env_path: Path to .env file, defaults to '.env' in current directory
            
        Returns:
            bool: True if .env file was loaded successfully
            
        Examples:
            >>> Config.load_env()  # Load from .env
            >>> Config.load_env('.env.local')  # Load from custom file
        """
        return load_dotenv(env_path, override=True)
