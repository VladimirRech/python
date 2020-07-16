# conditions.py
# Conditions on Python

# The comparison operators in and not in check whether a value occurs 
# (does not occur) in a sequence. The operators is and is not compare whether  
# two objects are really the same object; this only matters for mutable objects 
# like lists. All comparison operators have the same priority, which is lower 
# than that of all numerical operators.

str1, str2, str3 = '', 'Vladimir', 'Rech'
non_null = str1 or str2 or str3
print(non_null)
print()

print("Comparing sequences")
seq = [1, 2, 3, 4, 6, 7]
print(seq)
print("Is 5 in sequence?")
print(5 in seq)

seq2 = [1, 2, 3, 4, 5, 6]
print(seq < seq2)
print()

seq3 = [1,2,3,4,5,6]
print(seq3 < seq)
print()

seq4 = ['PR', 2, 'SC']
# error
# print(seq4 < seq3)
print(seq4 == seq3)
print()
