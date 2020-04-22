################################
#  --- list ---
# [1] list of items are enclosed in square brackets
# [2] list are mutable => you can add,delete and edit
# [4] list items are not unique, you can list the same item more than ones
# [5] can contains more than one data type

myAwesomeList = ["one", "two", "one", 1, 100.5, True]

print(myAwesomeList[-1])
print(myAwesomeList[0:2])
print(myAwesomeList[::2])

print(myAwesomeList)
print("--------------------")
myAwesomeList[-1] = "Two"
print(myAwesomeList)
print("--------------------")
myAwesomeList[:] = "Two", False, -100.5
print(myAwesomeList)
print("--------------------")
