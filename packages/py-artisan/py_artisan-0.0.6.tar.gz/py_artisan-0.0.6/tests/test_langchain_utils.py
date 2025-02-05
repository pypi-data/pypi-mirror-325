import pytest
from py_artisan.ai.langchain.langchain_utils import (
    ChainConfig,
    BaseChain,
    ConversationChain,
    DocumentChain
)

def test_chain_config():
    # 测试默认配置
    config = ChainConfig()
    assert config.model_name == "gpt-3.5-turbo"
    assert config.temperature == 0.7
    
    # 测试自定义配置
    custom_config = ChainConfig(
        model_name="gpt-4",
        temperature=0.5,
        max_tokens=500
    )
    assert custom_config.model_name == "gpt-4"
    assert custom_config.temperature == 0.5
    assert custom_config.max_tokens == 500

def test_base_chain():
    chain = BaseChain()
    with pytest.raises(NotImplementedError):
        chain.run("测试输入")

def test_conversation_chain():
    chain = ConversationChain()
    
    # 测试对话
    response = chain.run("你好")
    assert isinstance(response, str)
    assert len(response) > 0
    
    # 测试清空历史
    chain.clear_history()
    assert len(chain.history) == 0

def test_document_chain():
    chain = DocumentChain()
    
    # 测试文档处理
    result = chain.run("这是一个测试文档")
    assert isinstance(result, str)
    assert len(result) > 0 