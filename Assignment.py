import math


# def make_amount(rupees_to_make, no_of_five, no_of_one):
#     five_needed = 0
#     one_needed = 0

#     # Start writing your code here
#     # Populate the variables: five_needed and one_needed
#     if rupees_to_make / 5 <= no_of_five:
#         five_needed = math.floor(rupees_to_make / 5)
#     else:
#         five_needed = no_of_five
#     rupees_to_make = rupees_to_make - five_needed * 5

#     if rupees_to_make <= no_of_one:
#         one_needed = rupees_to_make

#     else:
#         print("-1")
#         return 0

#     print("No. of Five needed :", five_needed)
#     print("No. of One needed  :", one_needed)


# make_amount(105, 21, 5)

# ----------------------------------------------------------------------------------------------------------------
# def solve(heads, legs):
#     error_msg = "No solution"
#     chicken_count = 0
#     rabbit_count = 0

#     if heads >= legs:
#         print(error_msg)
#     elif legs % 2 != 0:
#         print(error_msg)
#     else:
#         rabbit_count = (legs - 2 * heads) / 2
#         chicken_count = heads - rabbit_count
#         print(int(chicken_count), int(rabbit_count))


# # Provide different values for heads and legs and test your program
# solve(20, 60)

# marks = ["fa1", 80, "fa2", 85, "fa3", 95]
# report = marks[-4:]
# report = report[:1] + marks[5:]
# print(report)

# 0,10 se 4,6

# print(11 % 10)


# def fun(sample, res, key, val):
#     if key in sample:
#         res = True
#         sample.update({key: val})
#     res = False


# res = None
# sample = {"XS": 1, "X": 0, "XL": 3, "XXL": 4}
# fun(sample, res, "X", 2)
# print(sample["X"], res)

# for var1 in range(1, 6):
#     for var2 in range(1, 6):
#         if var1 % var2 != 0:
#             pass
#         elif var2 < var1:
#             continue
#         else:
#             print(var1 * var2)

# my_str = "All3 that4 glitters8 is2 not3 gold4"
# my_lst = []
# for char in my_str:
#     if char.isdigit():
#         my_lst.append(char)
#         my_str.replace(char, " ")
# print(my_str, my_lst)
# ------------------------------------------------------------
# temp = "Hello? how are you?"
# if temp.isdigit():
#     temp += "fine"
# else:
#     for var1 in range(len(temp)):
#         if temp[var1] == "?":
#             final_val = temp[:var1]
#             break
# if final_val.endswith("u"):
#     final_val.replace("you", "u")
# else:
#     final_val = final_val.upper()
# print(final_val)
# ----------------------------------------
# final_val = math.ceil(len("Bangalore") / len("Pune"))
# print(final_val)

# a = 1
# b = 2


# def swap(a, b):
#     temp = a
#     a = b
#     b = temp


# print(a, b)
# swap(a, b)
# print(a, b)

# var1 = 0
# var2 = 10
# while var1 <= 10 and var2 >= 1:
#     print(var1, var2)
#     var2 = var2 - 1
#     var1 = var1 + 1
#     if var1 == var2:
#         break

# list1 = [1, 2, 1, 3, 3, 1, 2, 1, 2, 1]
# tuple1 = ("A", "B", "C", "D")
# tuple1 += ("E",)
# list2 = []
# for var1 in range(5, len(list1)):
#     list2.append(list1[var1 - 5] + list1[var1])
# for var1 in range(0, len(list2)):
#     print(tuple[var1], list2[var1])


# def check_loss(game_history, game_points, total):
#     if game_history[1] == 0:
#         game_points[1] -= 1
#     else:
#         loss_points = game_history[1] * 2
#         game_points[1] -= loss_points

#     total = game_points[0] + game_points[1] + game_points[2]


# game_history = [4, 0, 2]
# game_points = [12, -4, 2]
# total = 0
# check_loss(game_history, game_points, total)
# game_history = [5, 2, 2]
# check_loss(game_history, game_points, total)
# print(total, game_points)


# def sum_of_numbers(list_of_num, filter_func=None):
#     if filter_func == None:
#         return sum(list_of_num)
#     else:
#         return sum(filter_func)


# def even(data):
#     e = []
#     for num in data:
#         if num % 2 == 0:
#             e.append(num)
#     return e


# def odd(data):
#     o = []
#     for num in data:
#         if num % 2 != 0:
#             o.append(num)
#     return o


# sample_data = range(1, 11)

# print(sum_of_numbers(sample_data, None))
# def division(value_1, value_2):
#     try:
#         return int(value_1) / value_2
#     except TypeError:
#         print("Type error")
#     except ValueError:
#         print("Value error")
#     finally:
#         print("Finally")
#     print("Done")


# division("A", 10)

# re = 0
# l1 = [10, 20, 30]
# l2 = [1, 2]
# for num in range(len(l1)):
#     for num in range(len(l2)):
#         re += l1[num] + l2[num]
# print(re)


# def fun(var1, var2):
#     try:
#         var3 = (int)(var1)
#         var2 = var3 + "A"
#         print(var2)
#     except TypeError:

#         print("T")
#     finally:
#         print("IF")


# try:
#     fun("R", 13)
# except ValueError:
#     print("V")
# finally:
#     print("Off")


# def fun1(var1=1, var2=2):
#     print(var1, end="")
#     print(var2, end="")


# fun1(100, None)
# fun1(var2=20, var1=10)
# fun1(var2=10)

# try:
#     tupl1 = ([1, 2], [3, 4])
#     list1 = [(1, 2), (3, 4)]
#     list2 = tupl1[0]
#     list2[0] = 5
#     list1[1] = (6, 7)
#     print(tupl1, list1)
# except TypeError:
#     print("err")


# def func1():
#     try:
#         1 / 0
#         return 1
#     except ZeroDivisionError:
#         "ABC" + 1
#         return 2
#     finally:
#         int("A")
#         return 3


# try:
#     result = func1()
#     print(result)
# except:
#     print(4)


# def fun(var1):
#     if var1 < 1:
#         return 0
#     elif var1 % 2 == 0:
#         return fun(var1 - 1)
#     else:
#         return var1 + fun(var1 - 2)


# print(fun(10))


# def func(my_lst, var1):
#     new_lst = []
#     for num in my_lst:
#         if num % var1 == 0:
#             new_lst.append(num // var1)
#         else:
#             new_lst.append(0)
#     return new_lst


# my_lst = [13, 17, 23, 27, 33, 37]
# # my_lst = [2, 5, 8, 11, 14, 17, 21]

# print(func(my_lst, var1=7))

# -====================================================================================================


# def rec(n):
#     for i in range(0, n):
#         for j in range(0, n):
#             print("*", end=" ")
#         print("\n")


# rec(6)


# def rec(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print("\n")


# rec(6)


# def rec(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(j + 1, end=" ")
#         print("\n")

# rec(6)


# def rec(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print(i + 1, end=" ")
#         print("\n")


# rec(6)


# def rec(n):
#     for i in range(n, 0, -1):
#         for j in range(0, i):
#             print("*", end=" ")
#         print("\n")


# rec(6)


# def rec(n):

#     for i in range(n, 0, -1):
#         for j in range(0, i):
#             print(j + 1, end=" ")
#         print("\n")


# rec(6)


# def rec(n):
#     for i in range(0, n):
#         for j in range(0, n - i):
#             print(" ", end=" ")
#         for k in range(0, 2 * i - 1):
#             print("*", end=" ")
#         print("\n")


# rec(6)


# def rec(n):

#     for i in range(n, 0, -1):
#         for j in range(0, n - i):
#             print(" ", end=" ")
#         for k in range(0, 2 * i - 1):
#             print("*", end=" ")
#         print("\n")


# rec(6)


# def rec(n):

#     for i in range(n, 0, -1):
#         for j in range(0, n - i):
#             print(" ", end=" ")
#         for k in range(0, 2 * i - 1):
#             print("*", end=" ")
#         print("\n")


# def find_sum(a, b):
#     try:
#         print(a + c)
#     except ValueError:
#         print("Fun name error")
#     finally:
#         print("sum Finally")


# try:
#     find_sum(12, 13)
# except NameError:
#     print("Invocation name error")
# finally:
#     print("Invocation Finally")


# def pattern(n):
#     for i in range(0, n):
#         for j in range(0, n - i):
#             print(" ", end=" ")
#         for k in range(0, 2 * i - 1):
#             print("*", end=" ")

#         print("\n")


# pattern(6)
# rec(6)


# def rec2(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print("\n")


# def rec1(n):
#     for i in range(n, 0, -1):
#         for j in range(0, i):
#             print("*", end=" ")
#         print("\n")


# rec2(6)
# rec1(6


# arr = [12, 23, 45, 6, 5, 70]

# for i in range(20):
#     n = arr.append(0)

# print(arr)

# Program to reverse a string

# gfg = "geeksforgeeks"

# # Reverse the string using reversed and join function
# gfg = "".join(reversed(gfg))

# print(gfg)

# String alignment

# val = "i am a good boy"
# h = "".join(reversed(val))

# print(h)

# s = "the sky is blue"
# str = s.split()
# print(str)
# rev = " ".join(reversed(str))
# print(rev)

# lists = s.split(" ")[::-1]
# newlists = [x for x in lists if x != ""]
# temp = " ".join(newlists)

# Python3 implementation of the approach

# MAX = 26


# def compressString(s, n):

#     freq = [0] * MAX

#     for i in range(n):
#         freq[ord(s[i]) - ord("a")] += 1

#     for i in range(MAX):

#         if freq[i] == 0:
#             continue

#         print((chr)(i + ord("a")), freq[i], end=" ")

#     Max = freq[0]
#     a = 0
#     for i in range(MAX):
#         if Max < freq[i]:
#             a = i
#             Max = freq[i]
#     print("\nmaximum occ :", chr(a + ord("a")))


# if __name__ == "__main__":

#     s = "aabc"
#     n = len(s)

#     compressString(s, n)


# def pattern(n):
#     i = 1
#     count = 1
#     while i <= n:
#         j = 1
#         while j <= n:
#             print(count, end=" ")
#             count += 1
#             j += 1

#         print(end="\n")
#         i += 1

# pattern(4)


# def pattern(n):

#     for i in range(0, n):
#         for j in range(i):
#             print("*")
#             j += 1
#         print(end="")


# pattern(4)


# def parttern(n):
#     i = 1
#     while i <= n:
#         j = 1
#         while j <= n:
#             print(i)
#             j = +1
#         print(end="")
#         i += 1


# parttern(4)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         val = row
#         while col <= row:
#             print(row + col - 1, end=" ")
#             val += 1
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(5)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         while col <= row:
#             print(row - col + 1, end=" ")
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(3)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         while col <= n:
#             print(chr(ord("A") + row - 1), end=" ")
#             col += 1
#         print(end="\n")
#         row += 1

# pattern(5)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         while col <= row:
#             print(chr(ord("A") + row - 1), end=" ")
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(3)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         while col <= row:
#             print(chr(ord("A") + row + col - 1), end=" ")
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(3)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         while col <= row:
#             print(chr(ord("A") + row + col - 1), end=" ")
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(3)


# def pattern(n):
#     row = 1
#     while row <= n:
#         col = 1
#         start = chr(ord("A") + n - row)
#         while col <= row:
#             print(start, end=" ")
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(3)


# def pattern(n):
#     row = 1
#     while row <= n:
#         space = n - row
#         while space:
#             print(end=" ")
#             space = space - 1
#         col = 1
#         while col <= row:
#             print("*", end=" ")
#             col += 1
#         print(end="\n")
#         row += 1


# pattern(5)


# def tri(n):
#     row = 1
#     while row <= n:

#         space = n - row
#         while space:
#             print(" ", end="")
#             space = space - 1

#         col = 1
#         while col <= row:
#             print(col, end="")
#             col = col + 1

#         start = row - 1
#         while start:
#             print(start, end="")
#             start = start - 1

#         print("\n")
#         row += 1


# tri(5)


