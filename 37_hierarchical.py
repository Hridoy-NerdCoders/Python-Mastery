class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call methods
dog.speak()  # Inherited from Animal
dog.bark()

cat.speak()  # Inherited from Animal
cat.meow()