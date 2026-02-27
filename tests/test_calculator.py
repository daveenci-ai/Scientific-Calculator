import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(1, 2) == 3
        assert self.calc.add(-1, 1) == 0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 0) == 0

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-1, 1) == -1

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
        with pytest.raises(ValueError, match='Cannot divide by zero'):
            self.calc.divide(10, 0)

    def test_calculate(self):
        assert self.calc.calculate('add', 1, 2) == 3
        assert self.calc.calculate('subtract', 5, 3) == 2
        assert self.calc.calculate('multiply', 3, 4) == 12
        assert self.calc.calculate('divide', 10, 2) == 5
        with pytest.raises(ValueError, match='Invalid operation'):
            self.calc.calculate('invalid', 1, 2)