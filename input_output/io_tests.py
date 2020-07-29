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