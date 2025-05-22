class Calculator:
    def operate(self, a, b, operation):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

if __name__ == "__main__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    calc = Calculator()
    result = calc.operate(a, b, operation)
    print("Result:", result)
