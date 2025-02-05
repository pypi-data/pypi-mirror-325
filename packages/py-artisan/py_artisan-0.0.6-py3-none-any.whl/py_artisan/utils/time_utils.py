"""时间处理工具模块"""
from datetime import datetime
import time

def format_timestamp(timestamp=None, format_str="%Y-%m-%d %H:%M:%S"):
    """
    将时间戳转换为指定格式的时间字符串
    
    Args:
        timestamp: 时间戳（秒），如果为None则使用当前时间
        format_str: 时间格式字符串，默认为 "%Y-%m-%d %H:%M:%S"
    
    Returns:
        str: 格式化后的时间字符串
    
    Examples:
        >>> format_timestamp(1640995200)  # 2022-01-01 00:00:00
        >>> format_timestamp(format_str="%Y年%m月%d日")  # 当前时间，格式：2024年01月01日
    """
    if timestamp is None:
        timestamp = time.time()
    return datetime.fromtimestamp(timestamp).strftime(format_str)

def get_datetime_range(days=0, hours=0, minutes=0, seconds=0):
    """
    获取指定时间范围的起止时间戳
    
    Args:
        days: 天数
        hours: 小时数
        minutes: 分钟数
        seconds: 秒数
    
    Returns:
        tuple: (start_timestamp, end_timestamp) 起止时间戳
    
    Examples:
        >>> start, end = get_datetime_range(days=7)  # 获取最近7天的起止时间戳
        >>> start, end = get_datetime_range(hours=24)  # 获取最近24小时的起止时间戳
    """
    end_time = time.time()
    seconds_delta = days * 86400 + hours * 3600 + minutes * 60 + seconds
    start_time = end_time - seconds_delta
    return start_time, end_time 