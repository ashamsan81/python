# ------------------------------
#    ------ User input ------
# ------------------------------
# input("msg to disply to end user")

fName = input("Enter your First Name:")
mName = input("Enter your Middle Name:")
lName = input("Enter your Last name:")

fName = fName.strip().capitalize() # this is called function's chain
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print("Welcome Back {} {:.1s}. {}".format(fName,mName,lName))