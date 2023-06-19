class pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}and I am {self.age} yr old")

    def speak(self):
        print("IDK")


class cat(pet):
    def speak(self):
        print("meow")


class Dog(pet):
    def speak(self):
        print("Bark")


class fish(pet):
    pass


p = pet("Tim", 12)
p.show()
c = cat("Bill", 34)
c.show()
d = Dog("SAGE reyna", 23)
d.show()
d.speak()
f = fish("lol", 33)
f.speak()
