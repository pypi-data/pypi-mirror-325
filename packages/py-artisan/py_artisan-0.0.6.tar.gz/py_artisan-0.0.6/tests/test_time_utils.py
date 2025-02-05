import time
from py_artisan.utils import time_utils

def test_format_timestamp():
    # 测试指定时间戳
    timestamp = 1640995200  # 2022-01-01 00:00:00
    assert time_utils.format_timestamp(timestamp) == "2022-01-01 00:00:00"
    
    # 测试自定义格式
    assert time_utils.format_timestamp(timestamp, "%Y年%m月%d日") == "2022年01月01日"
    
    # 测试当前时间
    current = time_utils.format_timestamp()
    assert isinstance(current, str)
    assert len(current) == 19  # 格式：YYYY-MM-DD HH:MM:SS

def test_get_datetime_range():
    # 测试获取时间范围
    start, end = time_utils.get_datetime_range(days=1)
    assert end - start == 86400  # 一天的秒数
    
    start, end = time_utils.get_datetime_range(hours=1)
    assert end - start == 3600  # 一小时的秒数
    
    # 测试组合时间
    start, end = time_utils.get_datetime_range(days=1, hours=1)
    assert end - start == 86400 + 3600  # 一天零一小时的秒数 