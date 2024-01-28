from decimal import Decimal


class Calculator:

    def add(self, a: int, b: int) -> int:
        print("tested line right here")
        return a + b

    def mod(self, a: int, b: int) -> float:
        print("hi")
        print("hola!")
        return a % b

    def subtract(self, a: int, b: int) -> int:
        print("hola!")
        print("hola!")
        print("hola!")
        print("hola!")
        print("hola!")

        return a - b

    def divide(self, a: int, b: int) -> Decimal:
        return Decimal(str(a / b))

    def pow(self, a: int, b: int) -> int:
        print("added new line that should be tested")
        if a < 0:
            print("this is not covered")
        return a ** b

    def assembly(self, a: int, b: int) -> int:
        return a % b
