import pytest
from src.calculator import Calculator

class TestCalculator:
    def test_add(self, calculator):
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
    
    def test_subtract(self, calculator):
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(10, -5) == 15
    
    @pytest.mark.parametrize("a,b,expected", [
        (3, 4, 12),
        (-2, 5, -10),
        (0, 100, 0)
    ])
    def test_multiply(self, calculator, a, b, expected):
        assert calculator.multiply(a, b) == expected
    
    def test_divide(self, calculator):
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(9, 3) == 3
    
    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(5, 0)