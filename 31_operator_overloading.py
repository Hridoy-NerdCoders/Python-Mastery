class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,v):
        # print(self.__repr__)
        return Vector(self.i + v.i, self.j + v.j, self.k + v.k)
        
v1 = Vector(2,3,2)
print(v1)
v2 = Vector(2,1,1)
print(v2)
# print(repr(v1))
print(v1 + v2)

print(type(v1 + v2))