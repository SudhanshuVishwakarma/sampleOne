import re

# input_data = "Flight Savana Airlines a222134FGV"

# re.search(r"Airlines", input_data)


# if re.search(r"a\d", input_data) != None:
#     print("Pattern found")
# else:
#     print("Pattern not found")


# if re.search(r"A\d?i", "A23irline") != None:
#     print("Pattern found")
# else:
#     print("Pattern not found")

# flight_details = "Flight Savana Airlines a2134"
# print(flight_details)
# print(re.sub(r"Flight", r"udan khatola", flight_details))

ip = "the sun rises in the east"

def encrypt_sentence(msg):
    x = msg.split(" ")
    for i in range(0, len(x)):
        if i % 2 == 0:
            x[i] = x[i][::-1]
        else:
            a = ""
    for j in x[i]:
        if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
            x[i] = x[i].replace(j, "")
            a += j
            x[i] += a

    print(" ".join(x))


encrypt_sentence(ip)
