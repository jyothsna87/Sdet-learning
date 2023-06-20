class Person:
    def __init__(self, name):
        self.name = name
        print("Hello")

    def greet(self):  # Method - Class - Methods are functions that are associated with an object or a class.
        print("Hello" + self.name)