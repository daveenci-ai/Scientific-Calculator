class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b

    def calculate(self, operation: str, a: float, b: float) -> float:
        if operation == 'add':
            return self.add(a, b)
        elif operation == 'subtract':
            return self.subtract(a, b)
        elif operation == 'multiply':
            return self.multiply(a, b)
        elif operation == 'divide':
            return self.divide(a, b)
        else:
            raise ValueError('Invalid operation')
