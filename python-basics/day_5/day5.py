# lst = list()

# fruits = ['Mango', 'banana', 'apple']

# print("fruits: ", fruits)
# print("Number of fruits: ", len(fruits)) # good way of using len() and finding number of fruits.


# ages = [19, 22, 19, 24, 20, 26, 16, 24, 25, 24]

# ages.sort()
# small = min(ages)
# large = max(ages)

# print(small)
# print(large)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(len(it_companies))

it_companies.insert(3, 'IT company')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

all_companies = it_companies[3:5]

print(all_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
full_stack = front_end.copy()
print(full_stack)

front_end.insert(5, 'Python')
front_end.insert(5, 'SQL')


print(front_end)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(ages)