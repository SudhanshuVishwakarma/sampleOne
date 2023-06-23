class pet:
    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

    def show(self):
        print(f"I am {self.name}and I am {self.age} yr old of {self.breed}")

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


p = pet("Harbor", 12, "labra")
p.show()
c = cat("M odi", 55, "labra")
c.show()
d = Dog("SAGE reyna", 23, "labra")
d.show()
d.speak()
f = fish("lol", 33, "labra")
f.speak()
