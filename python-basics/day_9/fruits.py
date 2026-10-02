fruits = ['banana', 'orange', 'mango', 'lemon']
user = input("Enter the fruit: ")

if user in fruits:
    print("it is already presented")

else:
    fruits.append(user)
    print(fruits)