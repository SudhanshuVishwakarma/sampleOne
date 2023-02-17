def ar_of_circle(*r):

 pie=3
 area = pie*r[1]**2
 return area

print(ar_of_circle(10,2,13))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-3','Asabeneh','Brook','David','Eyob'))

You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9

Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


list = [2, 3, 4, 6, 7, 8]


def p_list(list):
    for i in range(5, -1, -1):
        print(list[i])


p_list(list)

list = ["a","s","c","e","g"]

def p_list(list):
    for i in list:
        print(i.upper())


p_list(list)


def add_item(food_staff,a):
    food_staff.append(a)
    print(food_staff)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))

Declare a function named evens_and_odds .
It takes a positive integer as parameter and it counts number of evens and odds in the number.


def evens_and_odds(n):
    count_odd = 0
    count_even = 0
    for i in range(1, n):
        if i % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
    print("Even count :", count_even)
    print("odd count :", count_odd)


evens_and_odds(10)

Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
5= 1*2*3*4*5


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


print(fact(20))


def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1

# Driver Code
lis1 = []
if Enquiry(lis1):
    print("The list is not empty")
else:
    print("Empty List")


