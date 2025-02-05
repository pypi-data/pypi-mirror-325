import pytest
from py_artisan.ai import text_utils
from py_artisan.ai.openai_utils import OpenAIClient

def test_split_text():
    text = "这是第一段。\n这是第二段。\n这是第三段。"
    segments = text_utils.split_text(text, max_length=10, overlap=2)
    assert len(segments) > 1
    assert all(len(seg) <= 10 for seg in segments)

def test_clean_text():
    text = "访问 https://example.com 了解更多。123 ！"
    
    # 测试删除URL
    cleaned = text_utils.clean_text(text, remove_urls=True)
    assert "https://example.com" not in cleaned
    
    # 测试删除数字
    cleaned = text_utils.clean_text(text, remove_numbers=True)
    assert "123" not in cleaned
    
    # 测试删除标点
    cleaned = text_utils.clean_text(text, remove_punctuation=True)
    assert "！" not in cleaned

def test_openai_client():
    # 测试缺少API key的情况
    with pytest.raises(ValueError):
        OpenAIClient()
    
    # 测试初始化
    client = OpenAIClient("test_key")
    assert client.api_key == "test_key"
    assert "Authorization" in client.headers 