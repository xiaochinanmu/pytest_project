import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator():
    """提供一个计算器实例作为测试 fixture"""
    return Calculator()

@pytest.fixture
def sample_string():
    """提供一个测试字符串"""
    return "hello pytest"