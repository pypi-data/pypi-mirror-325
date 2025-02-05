"""LLM Factory module"""
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from py_artisan.utils.config import Config

class LLMFactory:
    @staticmethod
    def create_llm(provider: str = None):
        """Create LLM instance"""
        provider = provider or Config.get_env('LLM_PROVIDER', 'LLM provider (openai/ollama/local)')
        provider = provider.lower()
        
        if provider == 'openai':
            return LLMFactory._create_openai_llm()
        elif provider == 'ollama':
            return LLMFactory._create_ollama_llm()
        elif provider == 'local':
            return LLMFactory._create_local_llm()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")
    
    @staticmethod
    def _create_openai_llm():
        """Create OpenAI LLM"""
        return ChatOpenAI(
            api_key=Config.get_env('OPENAI_API_KEY', 'OpenAI API Key'),
            model=Config.get_env('OPENAI_API_MODEL', 'OpenAI model name'),
            temperature=float(Config.get_env('OPENAI_TEMPERATURE', 'Temperature for OpenAI')),
            request_timeout=int(Config.get_env('OPENAI_TIMEOUT', 'Timeout for OpenAI requests'))
        )
    
    @staticmethod
    def _create_ollama_llm():
        """Create Ollama LLM"""
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        return ChatOllama(
            base_url=Config.get_env('OLLAMA_BASE_URL', 'Ollama service URL'),
            model=Config.get_env('OLLAMA_MODEL', 'Ollama model name'),
            temperature=float(Config.get_env('OLLAMA_TEMPERATURE', 'Temperature for Ollama')),
            callback_manager=callback_manager,
            streaming=True
        )
    
    @staticmethod
    def _create_local_llm():
        """Create local LLM"""
        from langchain_community.llms import LlamaCpp
        
        return LlamaCpp(
            model_path=Config.get_env('LOCAL_MODEL_PATH', 'Path to local model file'),
            temperature=float(Config.get_env('LOCAL_MODEL_TEMPERATURE', 'Temperature for local model')),
            max_tokens=int(Config.get_env('LOCAL_MODEL_MAX_TOKENS', 'Max tokens for local model')),
            n_ctx=2048,
            verbose=False
        ) 