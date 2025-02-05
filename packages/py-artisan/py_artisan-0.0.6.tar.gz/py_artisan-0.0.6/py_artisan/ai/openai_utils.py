"""OpenAI API 工具模块"""
import os
import json
from typing import List, Dict, Any, Optional
import requests

class OpenAIClient:
    """OpenAI API 客户端"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        初始化 OpenAI 客户端
        
        Args:
            api_key: OpenAI API密钥，如果为None则从环境变量OPENAI_API_KEY获取
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        
        self.base_url = "https://api.openai.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Dict[str, Any]:
        """
        调用 OpenAI Chat Completion API
        
        Args:
            messages: 对话消息列表
            model: 模型名称
            temperature: 温度参数 (0-1)
            max_tokens: 最大生成token数
            
        Returns:
            Dict: API 响应结果
            
        Examples:
            >>> client = OpenAIClient()
            >>> messages = [
            ...     {"role": "system", "content": "你是一个助手"},
            ...     {"role": "user", "content": "你好"}
            ... ]
            >>> response = client.chat_completion(messages)
        """
        url = f"{self.base_url}/chat/completions"
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json() 