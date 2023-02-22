# def calculate_sum(list_of_expenditure):
#     total = 0
#     try:
#         for expenditure in list_of_expenditure:
#             total += expenditure
#         print("Total:", total)
#         avg = total / no_values
#         print("Average:", avg)
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")


# try:
#     list_of_values = [100, 200, 300, 400, 500]
#     num_values = len(list_of_values)
#     calculate_sum(list_of_values)
# except NameError:
#     print("Name error occured")
# except:
#     print("Some error occured")

# balance = 1000
# amount = "300Rs"


# def take_card():
#     print("Take the card out of ATM")


# try:
#     if balance >= int(amount):
#         print("Withdraw")
#     else:
#         print("Invalid amount")
# except TypeError:
#     print("Type Error Occurred")
# except ValueError:
#     print("Value Error Occurred")
# except:
#     print("Some error Occurred")
# finally:
#     take_card()


# def find_common_characters(msg1, msg2):
#     newSet = set(msg1.replace(" ", "")) & (set(msg2.replace(" ", "")))
#     for ch in newSet:
#         print(ch, end="")


# find_common_characters("I am not defined", "I dont know why")


# def find_pairs_of_numbers(num_list, n):
#     c = 0
#     for i in range(len(num_list)):
#         for j in range(i + 1, len(num_list)):
#             if num_list[i] + num_list[j] == n:
#                 c += 1
#     return c


# print(find_pairs_of_numbers([1, 2, 7, 4, 5, 6, 0, 3], 6))
# print(find_pairs_of_numbers([3, 4, 1, 8, 5, 9, 0, 6], 9))
# list1=[10,20,30,40]
# list1.insert(7,25)
# print(list1)


# def sample(value):
#     sum1 = 0
#     for i in value:
#         if i % 2 != 0:
#             sum1 += value[i]
#         else:
#             sum1 -= i
#     print(sum1)


# dict1 = {1: 2, 2: 4, 3: 6, 5: 8}
# sample(dict1)


# def ml(arg_list):
#     arg_list = arg_list + [60, 70, 80]
#     print("IF:", arg_list)


# i_list = [10, 20, 30, 40, 50]
# print("bf:", i_list)
# ml(i_list)
# print("af", i_list)

# list1 = [10, 20, 30, 40, 50]
# list1.insert(7, 25)
# print(list1)

# sd = {"a": "apple"}
# print(sd.get("a"))

# ml = [0] * 5
# for index in range(1, 5):
#     ml[index] = (index - 1) * index
# print(ml)

