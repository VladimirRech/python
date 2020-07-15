# dic.py
# Dictionaries on Python
# The keyes must have immutable

# It starts with empty braces: {}
firstDic = {}

# It's possible initialize with Key:Value pairs
phones = { "Joe": "99999-1234", "Ana": "32152-3245"}

print(phones)
print()

# Adding
phones["Jessica"] = "89892-3232"    
print (phones)
print()

# The are accessible by keys
print(phones["Joe"])
print()

# Can remove a key
del phones["Ana"]

print(phones)
print()

phones["Te"] = "9-9921-3232"
phones["Josy"] = "9-0232-1112"

# They can be sorted
print('Keys sorted')
print(sorted(phones))
print()
print(phones)
print()

print("Printing only keys")
print(list(phones))
print()

print("Finding <<Jessica>> in dic")
print("Jessica" in phones)
print()

print("Finding <<Nemo>>")
print("Nemo" in phones)
print()

# Another way to build a dictionary
states = dict([('PR', 'Paraná'), ('SC', 'Santa Catarina'), 
              ('RS', 'Rio Grande do Sul')])
print(states)
print()

# It's versatile to initialize on python
prices=dict(banana=1, apple=2.5, avocado=2.3)
print(prices)
print()

# What will happen if the key not in dictionary?
# print(prices['strawberry'])
# print()
# Error...

# Better to check fist
if "strawberry" not in prices:
    print('strawberry not in list')    
else:
    print(prices['strawberry'])