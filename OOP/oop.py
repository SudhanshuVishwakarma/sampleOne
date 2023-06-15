class Dog:
    def __init__(self, name) -> None:
        self.name = name
        print(name)

    def add(self, x):
        return x + 1

    def bark(self):
        print("bark")


d = Dog("Muse")
# print(d.add(3))
# d.bark()
