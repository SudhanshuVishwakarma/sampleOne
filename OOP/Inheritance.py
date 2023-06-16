class pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}and I am {self.age} yr old")


class cat:
    def speak(self):
        print("meow")


class Dog:
    def speak(self):
        print("Bark")
