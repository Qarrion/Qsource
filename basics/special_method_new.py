class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print("Initializing instance")
        self.name = name

obj = MyClass("example")

# Singleton
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

st = Singleton(30)

# Factory method
class Person:
    def __new__(cls, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return super().__new__(cls)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def create_person(cls, name, age):
        return cls(name, age)

person = Person.create_person("Alice", 30)