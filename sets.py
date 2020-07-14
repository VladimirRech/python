# set.py
# 'Set' samples on python

# set lists remove duplicated ones
print('Set remove duplicated values')
set1 = { 'Dog', 'Cat', 'Parrot', 'Cat', 'Lion' }
print(set1)

# It works with words to, just initialize in the corret maner
set2 = set('Abracadabra')
print(set2)

# It's possibile to find values in a set
print('Dog' in set1)
print('Girafe' in set1)

# some operations
set3 = { 'Girafe', 'Dog', 'Cow', 'Ox'}
print(set1 - set3)      # unique elements
print(set1 & set3)      # common elements (in both)
print(set1 | set3)      # elements in first, seccond or both
print(set1 ^ set3)      # elements in first, secconed but not in both

# initalizing in another way
set4 = { x for x in set1 if x not in set3}
print(set4)