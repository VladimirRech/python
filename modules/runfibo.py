# runfibo.py
# demonstrate how to use import modules on Python
# Import the fibo.py
import fibo

fibo.fib(1000)
print()

f = fibo.fib2(2000)
print(f)
# print the module name
print(__name__)
print()

# A very interesting thing: you can assign a function to a variable
f = fibo.fib2
print(f(300))