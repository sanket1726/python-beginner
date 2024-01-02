def hello():
    print('Hellow function called')


hello()


# normal arguments

def add(num1, num2):
    return num1 + num2


result = (add(10, 20))

print(result)


# keyword arguments --> order of the arguments passed does not matter

def speed(time, distance):
    return distance / time


finalSpeed = speed(distance=11000, time=120)
print(finalSpeed)


# default parameters

def area(radius, pi=3.14):
    return pi * radius * radius


finalArea = area(10)
print(f'final area is {finalArea} sq/ft')


# Returning multiple values from a function

def properties(num1, num2):
    return num1+num2, num2-num1


addition, sub = properties(10,20)
print(f'addition is {addition} & subtraction is {sub} ')
