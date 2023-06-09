# list1 = [56, 3, 2, 76, 6, 0]
# # Min Max value
# # using min() max() method
# print(list1)
# print()
# # swap the numbers
# for i in range(len(list1)):
#     min_value = max(list1[i:])
#     min_index = list1.index(min_value)
#     list1[i], list1[min_index] = list1[min_index], list1[i]
# print(list1)

# # For the duplicate value
# list1 = [56, 0, 2, 2, 6, 0]

# for i in range(len(list1)):
#     min_value = min(list1[i:])
#     min_index = list1.index(min_value, i)
#     if list1[i] != list1[min_index]:
#         list1[i], list1[min_index] = list1[min_index], list1[i]

#     print(list1)


list1 = [56, 0, 2, 2, 6, 0]

for i in range(len(list1)):
    min_value = list1[i]

    for j in range(i + 1, len(list1)):
        if list1[j] > min_value:
            min_value = list1[j]

    min_index = list1.index(min_value, i)
    if list1[i] != list1[min_index]:
        list1[i], list1[min_index] = list1[min_index], list1[i]

print(list1)
