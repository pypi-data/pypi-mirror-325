"""文本处理工具模块"""
import re
from typing import List, Optional

def split_text(
    text: str,
    max_length: int = 2000,
    overlap: int = 200,
    separator: str = "\n"
) -> List[str]:
    """
    将长文本分割成小段落
    
    Args:
        text: 输入文本
        max_length: 每段最大长度
        overlap: 重叠长度
        separator: 分割符
        
    Returns:
        List[str]: 分割后的文本段落列表
        
    Examples:
        >>> text = "这是一段很长的文本..."
        >>> segments = split_text(text, max_length=1000)
    """
    if len(text) <= max_length:
        return [text]
        
    segments = []
    start = 0
    
    while start < len(text):
        end = start + max_length
        
        if end >= len(text):
            segments.append(text[start:])
            break
            
        # 在最大长度位置寻找最近的分隔符
        split_pos = text.rfind(separator, start, end)
        if split_pos == -1:
            split_pos = end
            
        segments.append(text[start:split_pos])
        start = split_pos - overlap  # 保持重叠
        
    return segments

def clean_text(
    text: str,
    remove_urls: bool = True,
    remove_numbers: bool = False,
    remove_punctuation: bool = False
) -> str:
    """
    清理文本
    
    Args:
        text: 输入文本
        remove_urls: 是否删除URL
        remove_numbers: 是否删除数字
        remove_punctuation: 是否删除标点符号
        
    Returns:
        str: 清理后的文本
        
    Examples:
        >>> text = "访问 https://example.com 了解更多。123"
        >>> clean_text(text)
        '访问 了解更多。123'
    """
    if remove_urls:
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    if remove_numbers:
        text = re.sub(r'\d+', '', text)
    
    if remove_punctuation:
        text = re.sub(r'[^\w\s]', '', text)
    
    return text.strip() 