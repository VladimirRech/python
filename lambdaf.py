# Samples on lambda funcions on pyton

def makeincrementor(n):
    return lambda x: x + n;
    
def another(n):
    # we can run another lines
    n *= -1
    # but the "lambda" must be the last one
    return lambda x: x + n
      
f = makeincrementor(42)
print("Sample on passing argument")
print(f(0))     # dont't add any values
print(f(42))    # add 42
print(f(-42))   # returns zero

print("Another sample")
l = another(42)

print (l(1))

# using lambda direct
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4,'four')]
# sort by the second column
pairs.sort(key=lambda pair: pair[1])
print("Using lambda directly")
print(pairs)

pairs.append((5, 'five'))
pairs.append((42, 'forty two'))
# sort by the first column
pairs.sort(key=lambda pair: pair[0])
print(pairs)