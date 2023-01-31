# print(len('sudhanshu'))


# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# fname = "sudhanshu"
# lname = "Vishwakarma"

# full_name = fname + lname

# print(full_name)

# fname = "Valo"
# lname = "Sage"
# lang = "python"
# age = 23

# format = '{} {} {} {}'.format(fname,lname,lang,age)
# print(format)

# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleH

# language = 'Python'
# pto = language[0:6:4] #
# print(pto) # Pto

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 16
# print(challenge.find('th')) # 17

# octal, binary and hexadecimal format
# print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# challenge = '12.3'
# print(challenge.isdecimal())  # True

# company = "coding for all"
# print(len(company))
# print(company,len(company),company.upper(),company.lower())

# String = "codeing" + " " + "for" + " " + "all"
# print(
#     (String.capitalize, String.title, String.swapcase),
#     String[0:6],
#     String.index("codeing"),
#     String.replace("codeing", "python"),
# )
def acro(stng):
   
    output = stng[0]
         
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
                
            output += stng[i]
   
    output = output.upper()
    return output
 
 
inpt1 = "Codeing For All"
# inpt1 = "Riya Kumari"
 
print(acro(inpt1))
 
