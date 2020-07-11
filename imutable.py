# Default values are imutable, even in multiple instances.
# This is true to object like lists, dictionaries and instances of classes
# See this examples.

def mut0(number, li = []):
    # In this example, values are agregated
    li.append(number)
    return li


def mut1(number, li = None):
    # in this case, we bypass the limitation using None value
    
    if li is None:
        li = []

    li.append(number)
    return li

print("""\
        First the imutable values:
            print(mut0(1))
            print(mut0(2))
            print(mut0(3))

        Second the mutable values:
            print(mut1(1))
            print(mut1(2))
            print(mut1(3))"""
)

print(mut0(1))
print(mut0(2))
print(mut0(3))

print("")

print(mut1(1))
print(mut1(2))
print(mut1(3))
