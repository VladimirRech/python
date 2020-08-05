# file_io.py
# Input and output with files
# Using "with" grants that the file will properly closed at the end of the 
# operation.

with open('io_tests.py') as f:
    read_data = f.read();
    print(read_data)
    
print('Is the file closed? ', f.closed)
print()

# Reading lines 
with open('io_tests.py') as f:
    lines = f.readlines()
    
digits = 1

if len(lines) > 9 and len(lines) < 100:
    digits = 2
    
else:
    digits = 3
    
li = 1
for l in lines:
    print('{0} {1}'.format(repr(li).rjust(digits), l), end='')    
    li += 1
    
print()