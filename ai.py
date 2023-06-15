# import sys


# class Solution:
#     def dataTypeSize(self, str):
#         # Code here

#         data_types = {"Character": 1, "Integer": 4, "Float": 4, "Double": 8, "Long": 8}

#         if str in data_types:
#             return data_types.get(str)


# x = dataTypeSize("sudhanshu")
# print(x)

# 'lesser' if n < m
# 'equal' if n == m
# 'greater' if n > m


class Solution:
    def compareNM(self, n: int, m: int) -> str:
        if n < m:
            print("lesser")
        if n > m:
            print("greater")
        elif n == m:
            print("Equal")

        return


compare = Solution()
compare.compareNM(4, 8)
