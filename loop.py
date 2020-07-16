# loop.py
# Looping on python
# Yes!!! My first import
import math

print("It's possible to retrieve both keys and values")
states = dict([('PR', 'Parana'), ('SC', 'Santa Catarina'), 
              ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'),
              ('MT', 'Mato Grosso'), ('GO', 'Goias'), ('TO', 'Tocantins')])
for k, v in states.items():
    print(k, v)
print()

print("Also, with Python, it's easy to do this with arrays")
fruits = enumerate(['Apple', 'Avocado', 'Berries', 'Banana', 'Coconut', 
                    'Pineapple'])
for i, v in fruits:
    print(i, v)
    
print()

print("Looping through two sequences at the same time")
states = ['Parana', 'Santa Catarina', 'Rio Grande do Sul']
capital = ['Curitiba', 'Florianopolis', 'Porto Alegre']

# Use the ZIP function to join two lists
for q, a in zip(states, capital):
    print("What's the capital city of {0} state? It's {1}".format(q, a))

print()

print('Looping reversed')
lst = range(0, 21, 3)
for f in reversed(lst):
    print(f)
    
print()

print("Sorting")
for i in sorted(set(states)):
    print(i)
    
print("Filtering values on a heterogenic list")
raw_data = [1977, 1, float('NaN'), 3.1415, 42, 33.3334]
# array to receive filtered values
filtered = []
 
for value in raw_data:
    if not math.isnan(value):
       filtered.append(value)
       
print(filtered)