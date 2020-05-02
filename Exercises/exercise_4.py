# get user age
print("#"*40)
print(" Age Converter App ".center(40,"#"))
print("#"*40)
age = input("Please enter your age: ")

# validate user's input
if age.isnumeric():
    convTo = input("Please enter your age coversion unit, \n 0: for month \n 1: for weeks \n 2: for days \n :")
    # validate input
    if convTo not in ("0","1","2"):
         convTo = input("Please enter a valid number, \n 0: for month \n 1: for weeks \n 2: for days \n :")
    else:
        if convTo == "0":
            print("your age in months = {}".format(int(age)*12))
        elif convTo == "1":
            print("your age in Weeks = {}".format(int(age)*52))
        else:
            print("your age in days = {}".format(int(age)*365))
else:
    print("Not a valid value, please try again")
    age = input("Please enter your age: ")