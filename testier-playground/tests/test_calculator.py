from production_code.calculator import Calculator


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
