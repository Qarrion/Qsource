class MyClass:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print(f"Entering {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting {self.name}")
        
    def __call__(self, arg):
        print(f"Calling {self.name} with argument {arg}")

with MyClass("object") as obj:
    obj("argument")