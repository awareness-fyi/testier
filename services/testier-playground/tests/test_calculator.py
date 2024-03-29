from decimal import Decimal

from src.calculator import Calculator


class TestCalculator:
    def test_add(self):
        calculator = Calculator()

        assert calculator.add(1, 1) == 2

    def test_subtract(self):
        calculator = Calculator()

        assert calculator.subtract(2, 1) == 1

    def test_mod(self):
        calculator = Calculator()

        assert calculator.mod(20, 4) == 0

    def test_divide(self):
        calculator = Calculator()

        assert calculator.divide(20, 4) == Decimal(5)

    def test_pow(self):
        calculator = Calculator()

        assert calculator.pow(2, 3) == 8

    def test_assembly(self):
        calculator = Calculator()

        calculator.assembly(1, 2)
