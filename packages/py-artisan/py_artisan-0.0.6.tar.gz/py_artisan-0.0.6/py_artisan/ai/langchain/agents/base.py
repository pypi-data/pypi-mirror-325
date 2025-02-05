from abc import ABC, abstractmethod
from typing import Any
from py_artisan.ai.langchain.llm_facetory import LLMFactory

class BaseAgent(ABC):
    def __init__(self, provider: str = None):
        self.llm = LLMFactory.create_llm(provider)
    
    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """执行 agent 的主要功能"""
        pass