# boarding_call = "Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
# if boarding_call.startswith("Good Evening"):
#     print(boarding_call.replace("Good Evening", "Good Morning"))
# if (boarding_call.find("AL")) >= 0:
#     print("Welcome to Air Lines.")
# if boarding_call.endswith("A.M."):
#     print("Passengers are requested to have their breakfast.")
# a = boarding_call.split(" ")
# for i in a:
#     if i.isdigit():
#         print("Flight Number is specified to the passengers.")
# print(
#     "Total number of times flight service name is specified in the boarding call:",
#     boarding_call.count("AL"),
# )
# message = "Thank you all..Have a nice journey!"
# print(message.upper())
# print(message.lower())


# def len_of_st(name):
#     count = 0
#     for i in name:
#         count += 1
#     print(count)


# name = input("Enter name")
# len_of_st(name)


# def swap(name):
#     return name[-1:] + name[1:-1] + name[:1]


# str2 = input("Enter name ")

# print(swap(str2))
# -----------------------------------------------------------------
# def rev(d, n):
#     a = list(d)
#     s = 0
#     e = n - 1
#     while s < e:
#         temp = a[s]
#         a[s] = a[e]
#         a[e] = temp

#         s += 1
#         e -= 1
#     a = "".join(a)
#     return a


# st = "Sudhanshu"
# n = len(st)
# print(rev(st, n))


# def valid(ch):
#     if (
#         (ch >= "a" and ch <= "z")
#         or (ch >= "A" and ch <= "Z")
#         or (ch >= "0" and ch <= "9")
#     ):
#         return 1
#     else:
#         return 0


# def Is_pali(s):
#     # faltu char hatane hai
#     a = list(s)
#     print(a)
#     i = 0
#     temp = ""

#     for i in range(0, len(a)):
#         if valid(a[i]):
#             # temp.append(a[i])
#             temp = temp + a[i]
#             print(temp)

#     # lower case
#     # temp = "".join(temp)
#     lower = temp.lower()
#     print(lower)

#     # pali check
#     b = list(lower)
#     p = 0
#     e = len(b) - 1

#     while p < e:
#         if b[p] != b[e]:
#             return 0
#         else:
#             p += 1
#             e -= 1
#     return 1


# s = "Noon"

# if Is_pali(s):
#     print("hai")
# else:
#     print("ni hai")

# from collections import Counter

# test_str = "Sudhanshu"

# count = Counter(test_str)

# print("Count is : " + str(count))

s = "abcabcabbc"
part = "abc"
while part in s:
    s = s.replace(part, "", 1)
print(s)
