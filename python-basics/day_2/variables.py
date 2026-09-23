# Day 2: 30 days of Python Programming

first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
full_name = first_name + " "+ last_name
country = input("Which Country You live: ")
city = input("Which city: ")
age = input("What's your age: ")
is_married =  False

first_name, last_name, age, is_married = {'Arvaj', 'Ahmad', '20', 'False'}

print(full_name)
print(first_name)
print(last_name)
print(country)
print(city)
print(age)
print(is_married)

# checking their types 
print(type(full_name))
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))

print(len(first_name))

num_one = 5
num_two = 4

num_add = num_one + num_two
num_sub = num_one - num_two
num_mul = num_one * num_two
num_div = num_one / num_two
num_square = num_one ** num_two
num_floor = num_one // num_two
num_modulus = num_one % num_two

print(num_add)
print(num_sub)
print(num_mul)
print(num_div)
print(num_modulus)
print(num_floor)
print(num_square)

# Area and circumferance of the circle 
radius = float(input("Enter the radius: "))
area_of_circle = (3.14 * radius ** 2 )
print (area_of_circle)

circumferance = (2 * 3.14 * radius)
print(circumferance)