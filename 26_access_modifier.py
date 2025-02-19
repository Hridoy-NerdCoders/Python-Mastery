class Modifiers:
    def __init__(self,public,private,protected):
        self.public = public
        self.__private = private
        self._protected = protected
        
    

    @property
    def private(self):
        raise AttributeError("Private attribute is read-only")

    @private.setter
    def private(self, private):
        self.__private = private
            
    
    
obj = Modifiers("Public","Private","Protected")

print(obj.public)
# print(obj.__private)
# print(dir(obj))
print(obj._Modifiers__private)#Name Mangling
print(obj._protected)
        