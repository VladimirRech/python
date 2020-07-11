#Testing functions in PHP
import subprocess as sp

class calculus_class:
    number1 = 0
    number2 = 0
    operator = ""
    op_result = 0
    error_message = ""
    has_error = False
 
    def exec_operation(self):
        self.has_error = True
        self.error_message = "Invalid parametersi where found!! Please, try again."
       
        if (self.number1 != None and self.number2 != None and
            self.operator != None and self. operator in ('+', '-', '/', '*')):
            self.has_error = False
            
            if self.operator == "+":
                self.op_result = self.number1 + self.number2
                
            elif self.operator == '-':
                self.op_result = self.number1 - self.number2
                
            elif self.operator == '*':
                self.op_result = self.number1 * self.number2
                
            elif self.operator  == '/':
                if self.number2 > 0:
                    self.op_result = self.number1 / self.number2
                else:
                    self.has_error = True

    def get_parameters(self):
        tmp = sp.call('clear', shell = True)
        print("Basic arithmetic ops in Python")
        print("Please enter some parameters:")
        self.number1 = int(input("Enter number 1: "))
        self.number2 = int(input("Ender number 2: "))
        self.operator = input("Choose an operator(+, -, /, *): ")

obj = calculus_class()
cont = "S"

while cont in ("s", "S"):
    obj.get_parameters()
    obj.exec_operation()

    if obj.has_error:
        print("An error ocurred:")
        print("\t", obj.error_message)
        
    else:
        print("Result of operation is: ", obj.op_result)
        
    cont = input("Continue? [s/[N]): ")
    
print("Good bye!")
