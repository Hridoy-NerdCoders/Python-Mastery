class Person:
    name = 'Hridoy'
    occupation = 'Software Developer'
    networth = 20
    
    def info (self):
        print(f'{self.name} is a {self.occupation}')
    
    
a = Person()
b = Person()
a.name = 'Safi'
a.occupation = 'Doctor'
# print(a.name,a.occupation)
a.info()

b.name = "Nita"
b.occupation = "HR"
b.info()