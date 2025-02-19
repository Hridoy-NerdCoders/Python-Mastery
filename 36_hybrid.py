class Base:
    def base_method(self):
        print("Base method")

class Derived1(Base):
    def derived1_method(self):
        print("Derived1 method")

class Derived2(Base):
    def derived2_method(self):
        print("Derived2 method")

class Hybrid(Derived1, Derived2):
    def hybrid_method(self):
        print("Hybrid method")

# Create an instance of Hybrid class
hybrid_instance = Hybrid()

# Call methods from different classes
hybrid_instance.base_method()
hybrid_instance.derived1_method()
hybrid_instance.derived2_method()
hybrid_instance.hybrid_method()