# fhr = open("data.txt", "r")
# line1 = fhr.readline()
# print(len(line1), end="")
# line2 = fhr.readline()
# print(line2, end="")
# line3 = fhr.readline()
# print(line3, end="")

# fhr = open("data.txt", "rb+")
# print(fhr.tell())
# fhr.seek(12)  # navigates to 12th position
# # from beginning of the file
# print(fhr.tell())
# fhr.seek(3, 1)  # navigates to 3rd position from current
# # position of the file object position
# print(fhr.tell())
# fhr.seek(-3, 2)
# # navigates to 3rd position from
# # end of the file in backward direction
# print(fhr.tell())
# fhr.close()


# fhw = open("data.txt", "w")
# fhw.write("written some thing")
# print(fhw.tell())
# print("closed", fhw.closed)
# fhw.close()
# print("after:", fhw.closed)

# print(len(("written some thing")))
