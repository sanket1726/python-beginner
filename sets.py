# Sets: list with unique values (cannot have duplicate values) | sets are unordered

# both numbers & numbers2 are set DS
numbers = set([1, 2, 3, 4, 5, 6])
numbers2 = {1, 2, 3, 4, 5, 6}
# print(numbers)
# print(numbers2)

# set orders or sorts given elements
num3 = {2, 5, 1, 3, 5, 8, 10}
# print(num3)

# this declaration for set is wrong with this type of declaration it becomes dictionary
empty = {}
print(type(empty))
# this is correct type of declaration for empty set
emptySet = set()
print(type(emptySet))

strSet = {'aniket', 'rudra', 'sanket', 'prem', 'abhi'}
strSet2 = {'sanket', 'rudra', 'tanmay'}
print(strSet)
print(strSet2)
# set operations
# print('aniket' in strSet)
# print('aniket' not in strSet)

# union of sets => all the elements from both sets
print(strSet | strSet2)

# intersection of sets => present in both
print(strSet & strSet2)

# difference operation
print(strSet - strSet2)
print(strSet2 - strSet)

# symmetric difference => present either in strSet or strSet2 not in both
print(strSet ^ strSet2)

# add and remove methods
setA = {1,2,3,4,5}
setA.add(10)
setA.add(1)
# removes the element from set if presents or throws error
setA.remove(4)

# to avoid throwing error we use discard
setA.discard(3)
setA.discard(15)
print(setA)

# removes elements from set in random manner
print(setA.pop())
print(strSet.pop())

# removes all the elements from set
setA.clear()
print(setA)
