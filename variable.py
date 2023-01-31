person_info = {"name": "sudhanshu", "company": "infosys", "city": "sagar"}

print(person_info)

print(type(person_info))
# print(type(person_info))

mini = min(23, 123, 652, 3, 5, 67, 88, 55)
print(mini)


first_name = input("what is you name:")
last_name = input("last name :")

fname = len(first_name)
print(fname)
lname = len(last_name)
print(lname)

if fname == lname:
    print("lucky")
else:
    print("do something ")


one = list(first_name)
print(one)

length = (len(first_name))
if length >= 10:print('great')
else :print("grow yourself")

f_name = "sudhanshu"
l_name = "vishwakarma"

print("lucky!!") if f_name == l_name else print("sed life!!")

a, b, c = input("Enter three Sides: ").split()
perimeterOftriangle =a+b+c
print(perimeterOftriangle)


a, b, c = [int(x) for x in input("Enter three values: ").split()]
perimeter = a + b + c
print(perimeter)

x, y, z = input("Enter three values: ").split()
sum = x+y+z
print(sum)

print( 'python' == 'dargon')

print(not(not 'on' in 'dragon' and 'python'))


even%2 = 0

num =int(input('enter a number: -')); print("badhai ho even no. hua hai") if (num % 2 == 0) else print("na hoga tumse !!") 


