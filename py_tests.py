#definindo funções em python
def fibPrint(range):
    # This line down is to generate auto documentation
    """ Print a Fibbonacci series up to range """
    a, b = 0, 1
    
    while a < range:
        print(a, end = ' ')
        a, b = b, a + b

    # This statement ends the function
    print()

def fib(range, wantPrint):
    a, b = 0, 1
    result = []
    
    while a < range:
        result.append(a)
        a, b = b, a + b

    return result;

def fib2Print(range):
    fibPrint(range)
    # This is another way to finish a function
    return


print("Funcion fibPrint()")
fibPrint(2000)
print("Function fib()")
fibo = fib(3000,1)
print(fibo)
print("Function fib2Print()")
fib2Print(5000)
