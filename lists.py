people = ['Sanket', 'Aniket', 'Abhijit']
# print(people)

mix = [1, 'z', 5, 'dda', 'da', 85]
# print(mix[1:-1])

# in -> checks for element is present in list return boolean True or False
# not in -> checks for element is not present in list return boolean True or False
# print('z' in mix)
# print(85 not in mix)

# print(len(mix))
# print(len(people))

# people.insert(2, 'Prem')

# adds element at end of the list
# people.append('Appended Person')
# people.append((['x1, x2']))

# removes the element provided if element not present throws error
# people.remove('Sanket')

# removes the last element from list
# people.pop()

# return index of provided entry if not present throws error
# print(people.index('Abhijit'))

scores = [1, 5, 6, 8, 5, 212, 1546, 8452, 154, 32, 9]

# print(min(scores))
# print(max(scores))

a = [1, 2, 3]
b = [4, 5, 6]

# simply like concatenating arrays
# print(a+b)

# repeats list 'n' number of times
# print(a*3)
# print(b*10)

# multidimensional/nested lists
mulList = [1, 2, 3, [4, 5, 6], 7, 8, [9, 10, 11]]
# print(mulList)

# mutability of lists
# mutLists = [1, 2, 3]
# mutLists[1] = 100
# mutLists[0:3] = [10, 20, 30]
# print(mutLists)

# Searching Items in a List (search in case is sensitive)
products = ['phone', 'tablet', 'laptop', 'journal']
# item = input('Enter product to search: ')
# print(item.lower() in products)

# removing items from list
print(f"current available products are: {products}")
# itemToRemove = input('Enter product to remove: ')
# products.remove(itemToRemove.lower())
print(f"new products list is {products}")

# adding item to list using append
# itemToAdd = input('Enter product to add: ')
# products.append(itemToAdd)
# print(f"new prod list is {products}")

# adding item to list at specific position
itemToAdd = input('Enter product to add: ')
add_after = input(f'after which product you want to add {itemToAdd}: ')
index = products.index(add_after.lower())
products.insert(index+1, itemToAdd.lower())
print(f"new prod list is {products}")
