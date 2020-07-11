#
# func_mult.py
# Testing funcion with variable arguments in Python
#
def myF(*args, sep = "/"):
    return sep.join(args);

print("variable arguments")
print(myF("test", "if", "it", "works"))
print(myF("test", "if", "it", "works", "with", "a", "custom", "separator", sep="..."))
print(" ")

#
# Unpacking argument lists
#
def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.", end=" ")
    print("E's", state, "!")

# Using a dictionary to store the variant args
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM" }

# Printing
print("Variable arguments with dictionary")
parrot(**d)

#
# Testing another sample
#
def invoice(product, totalValue=0, date="01/07/2020"):
    print("** You've bought a ", product, "in our site", end=" ")
    print("with the cost of $", totalValue, end=" ")
    print("the delivery will be on ", date, end=" ")


print("Custom variable arguments")
d = {"product": "dog food", "totalValue": 100, "date": "20/07/2020"}
invoice(**d)
