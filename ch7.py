a = ['a', 'b', 'c', 'd', 'e']
del a[0:2]
print(a)

a.append('f')
print(a)

a.insert(2, 'g')
print(a)

a.extend(['a', 'b'])
print(a)

print(a.count('c'))
print(a.index('a'))

a.remove('e')
print(a)

a = [3, 1, 4, 5, 2]
print(a)

a.sort()
print(a)

print(a.reverse())
print(a)