from decimal import Decimal


class Calculator:

    def add(self, a: int, b: int) -> int:
        return a + b

    def mod(self, a: int, b: int) -> float:
        return a % b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def divide(self, a: int, b: int) -> Decimal:
        return Decimal(str(a / b))
