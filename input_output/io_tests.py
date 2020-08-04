# io_tests.py
# Doing I/O testes with python

# To start string literals formatting (Java Script Style), use 'f' at beginning
print("Formatted string literals")
year = 1970
month = 2
day = 18
print(f'My birth date is {month}, {day} from {year}')
print()

# It's possibile use str.format() in the way bellow
# More about formatting numbers on:
# https://mkaz.blog/code/python-string-format-cookbook/
costPrice = 10 ; freight = 1.0
package = 0.5
taxes = 1.0
totalCost = costPrice + freight + package + taxes
print('Product cost: {:4}'.format(costPrice))
print('Additional expenses: ')
print('\tFreight: {:.2f}'.format(freight))
print('\tPackaging: {:.3f}'.format(package))
print('\tTaxes: {:.2f}'.format(taxes))
print('\tTotal {:.2f}'.format(totalCost))
print()

print("It's possibile represent string literals with repr()")
phrase = "Mary had\ta litle lamb\n\r"
print("This is the normal result, formatted:")
print(phrase)
print("And this, is the literal value:")
print(repr(phrase))
print()

print("Using formatting with a fixed number of decimal places (6f)")
import math
print(f"The value of pi is approximately {math.pi:.15f}.")
print()

print("Formatting with fixed spaces to numbers:")
phones = { 'Joe': 4399223311, 'Ann': 4199112345, 'Carol': 1198765432 }
for name, phone in phones.items():
    print(f'{name:10} ==> {phone:10d}')
    
print()

print("Using positional and named arguments to String.format():")
print('\tThe {0} of the {fruit} is {price:.2f} without {1}'.format('costs'
        , 'packaging', fruit='guava', price=4.5))
print()

print('There is another useful function: rjust, it right align text.')
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
    
print()

words = enumerate(['Apple', 'Avocado', 'Berries', 'Banana', 'Coconut',
                    'Pineapple'])
for w in words:
    print(repr(w).center(80))
print()