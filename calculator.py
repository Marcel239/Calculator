class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
    
    def subtraction(self, x, y):
        return x -  y
    
    def multiply(self, x, y):
        return x * y

    def divide():
        pass
if __name__ == "__main__":
    calc = Calculator()
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition result:", calc.add(a, b))
    print("Subtraction result:", calc.subtract(a, b))