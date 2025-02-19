class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def describe(self):
        fur_status = "has fur" if self.has_fur else "does not have fur"
        print(f"{self.name} is a mammal and {fur_status}")

class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

    def describe_breed(self):
        print(f"{self.name} is a {self.breed}")

dog = Dog("Buddy", True, "Golden Retriever")
dog.speak()
dog.describe()
dog.describe_breed()
