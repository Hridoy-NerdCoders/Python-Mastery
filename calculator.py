class Operation:
    def execute(self, num_1, num_2):
        pass

class Addition(Operation):
    def execute(self, num_1, num_2):
        return num_1 + num_2

class Subtraction(Operation):
    def execute(self, num_1, num_2):
        return num_1 - num_2

class Calculator:
    def __init__(self, num_1, operator, num_2):
        self.num_1 = num_1
        self.operator = operator
        self.num_2 = num_2

    def calculate(self):
        return self.operator.execute(self.num_1, self.num_2)

print(__name__)

num_1 = 10
num_2 = 5
if __name__ == "__main__":
    addition = Addition()
    calculator = Calculator(num_1, addition, num_2) 
    print(calculator.calculate())  

    subtraction = Subtraction()
    calculator = Calculator(num_1, subtraction, num_2)
    print(calculator.calculate()) 
        
