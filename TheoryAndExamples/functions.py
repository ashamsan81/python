#####################################################
#                 --- Functions ---                 #
#####################################################
# def <function_name>(arg1 [= default_value][,arg2,arg3,..]):
#       what to do
# Remember if you gonna set a default value, Last arg MUST have default value


def math_ops(num1 = 0,num2 = 0,oper = '+'):
    if type(num2) != int or type(num2) != int:
        print("one entry is not valid")
    else:
        if "oper" in ("+","-","*","/"):
            print("Not a valid operator")
        else:
            if oper == "+":
                print(f"The result is {num1 + num2}")
            elif oper == "-":
                print(f"The result is {num1 - num2}")
            elif oper == "*":
                print(f"The result is {num1 * num2}")
            else:
                print(f"The result is {num1 / num2}")


math_ops()

# function packing, unpacking, *args and **args(For dict key: value pairs)
# when you don't know how many arguments should pass to funtion
def skills(*skills):
    for skill in skills:
        print(f"Ahmed's Skills are: {skill}")

skills("php","html","css","python")

# you can also pass one argument long side with *args
def adv_skills(name,*skills):
    for skill in skills:
        print(f"{name}'s Skills are: {skill}")

adv_skills("Ali","php","html","css","python")