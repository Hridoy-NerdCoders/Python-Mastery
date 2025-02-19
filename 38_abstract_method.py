from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):
    def process(self):
        print('Laptop is running!')

# class Whiteboard(Computer):
    
#     def write(self):
#         print("It's writing")
        

class Programmer:
    def work(self,com):
        print('Solving Bugs!')
        com.process()

#Abstract class must have at least one abstract method
#Can't instantiate the Abstract class...
# com = Computer()
com1 = Laptop()
com1.process()

prog1 = Programmer()
prog1.work(com1)

# com2 = Whiteboard()
# prog1.work(com2)