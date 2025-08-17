'''
if condition:
    statements
elif condition:
    another statements
else:
    another statements
'''

age = int(input('Enter your age : '))
if age >= 18:
    print('you can vote!')
elif age <= 0:
    print('invalid age')
else:
    print('you are <18')