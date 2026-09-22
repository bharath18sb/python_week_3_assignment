class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print("5 + 3 =", calc.add(5, 3))
    print("10 / 2 =", calc.divide(10, 2))
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
