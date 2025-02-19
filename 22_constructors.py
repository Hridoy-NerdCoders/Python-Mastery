class Person:
    def __init__(self,name,occupation):
        print('Constructor is Called!')
        self.name = name
        self.occupation = occupation
    
    def info(self):
        print(f'{self.name} is a {self.occupation}')
        
a = Person(name='Hridoy',occupation='Python Developer')
# a.name = 'Dio'
# a.occupation = 'Python Developer'
a.info() 

b = Person(name='Druv', occupation='HR')
b.info()       
