it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))

it_companies.add('Twitter')
it_companies.update(['item5','item6','item7'])

print(len(it_companies))
print(it_companies)

it_companies.remove('item5')
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

# Difference in discard() & remove():
    # both used to remove element from the set
    # but in remove if element doesn’t exist it will give KEYERROR

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

c = A.union(B)

A.intersection(B)
print(A.intersection(B))

print(B.isdisjoint(A))

print(c)

print(A.symmetric_difference(B))

del A, B


sentence = ('I am a teacher and I love to inspire and teach people.')
sentence.split()

print(set(sentence.split()))