# Dictionary is combination of key and value
people = {"Sanket": 27, "Abhi": 31, "Aniket": 29}
print(people)

# you can access value by providing key. if key not present throws error
# print(people["Sanket"])

# dictionaries are mutable
people["Abhi"] = 32

# adding key:value pair in dictionary
people["Rudra"] = 10
# print(people)

# deleting entry from dictionary
del people["Rudra"]
# print(people)

# fetches value of given key. if key not present simply return None
# print(people.get("Rudra"))

# ------------------------------------------
# update dictionaries with new values
prices = {'iphone': 500, 'ipad': 400, 'stylus': 100}
new_prices = {'iphone': 400, 'ipad': 350, 'imac': 700}

prices.update(new_prices)

# popping given item from dict
v = prices.pop('stylus')
# prices.pop('stylus')
# print(v)
# print(prices)

# keys and Items methods
print(prices.values())
print(prices.keys())
print(prices.items())


# adding products to dictionary
products = {'phone': 100, 'tablet': 200, 'laptop': 400, 'journal': 40}
print(products)
# product = input('enter product you want to check the price: ')
# print(f'value of product {product} is ${products[product.lower()]}')

# adding item into dict
# product = input('enter product you want to add to list: ')
# product_price = input('enter product price you want to add to list: ')
# products[product] = product_price
# print(f'product {product} added with price {product_price} to product list {products}')

# deleting element from dict
# product = input('enter product you want to delete from products: ')
# del products[product.lower()]
# print(f'new products list is : {products}')

# Updating dict
product = input('enter product you want to change price from products: ')
product_price = input('enter new product price : ')
products[product.lower()] = product_price
print(f'updated products list is : {products}')
