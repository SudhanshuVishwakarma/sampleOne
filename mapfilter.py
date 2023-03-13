# def myFunc(a, b):
#     return a + b


# x = map(myFunc, ())
# print(list(x))

# age = [1, 2, 3, 4, 5, 6, 7, 8]


# def channi(x):
#     if x <= 5:
#         return False
#     else:
#         return True


# adults = filter(channi, age)

# for x in adults:
#     print(x)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))
