# class MyClass:
#     x = 5


# p1 = MyClass()  # object
# print(p1.x)


class computer:
    def __init__(self) -> None:
        print("in it")

    def config(self):
        print("i5,16gb,1tb")


com1 = computer()
com2 = computer()
# computer.config(com1)

com1.config()
com2.config()
