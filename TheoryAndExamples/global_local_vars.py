x = 1 # this is global var
print(f" this is global value of {x}")
def one():
    x = 22 #local scope, override global scop it assigned with a value
    print(f"this is local value of x {x}")

def two():
    print(f"I'm not assigning any values to x, so guess what is the value {x}")


def three():
    global x
    x = "I'm a new global value"
    #print(f"I'm not assigning any values to x, so guess what is the value {x}")

one()
two()
three()
print(f"yes global value x changed by function three and now x is the string below\n{x}")