class Employee:
    def __init__(self,name):
        self.name = name
        
    def __len__(self):
        i = 0
        for c in self.name:
            i+=1
        return i
    
    def __str__(self):
        return f'The name of the employee is {self.name} str.'
    
    def __call__(self, *args, **kwds):
        print(f'Employee name is {self.name}')
    
    #str na thakle repr e fallback kore ba repr theke nei:
    # The goal of __repr__ is to provide a string that, ideally, could be used to recreate the object.
    def __repr__(self):
        return f"Employee('{self.name}')"
        
e = Employee("Hridoy")
print(e)
print(str(e))
print(repr(e))
e()