# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n

# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleH

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0


# challenge = 'thirty days of python'
# sub_string = 'da'
# # print(challenge.index(sub_string))  # 7
# print(challenge.index(sub_string, 9)) # error

# company = "Coding For All"
# print(company)
# print(len(company))
# print(company.upper())
# print(company.lower())
# print(company.capitalize())
# print(company.swapcase())
# print(company.title())

# slicing = company[1:]# slicing the index 0
# print(slicing) 

# print(company.find("Coding"))
# print(company.replace("Coding", "Python"))

# companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

# print(companies.split(","))
# print(companies[10])


text = "Python For All"
# # words = text.split()

# print(words) # returns list

# acronym = ""

# for word in words:
#     acronym += word[0]

# print(acronym)

# print(text.rfind("I"))

# text = "You cannot end a sentence with because because because is a conjunction"
# text = " ".join(text.replace("because", "").split())
# print(text)

# print(text.isidentifier()) # True if all characters have no space between them

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

result = "# ".join(libraries)
print(result)

line = "I am enjoying this challenge.\nI just wonder what is next."
print(line)

tab_seq = "Name\t Age\t Country\t City"
tabseq = "Asabeneh\t250\tFinland\tHelsinki"
print(tab_seq)
print(tabseq)

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

a = 8
b = 6

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')