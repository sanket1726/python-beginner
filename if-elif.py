# If & Elif
age = input('Enter your age:')
age = int(age)

if age >= 18:
    print('You\'re an adult')
elif 18 >= age >= 16:
    print('Teenager')
else:
    print('You\'re not an adult')
