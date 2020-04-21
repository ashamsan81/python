#########################################
#            --- Tuple ---
# ---------------------------------------
# [1] Tuples itmes are enclosed in parentheses or not
# [2] Tuples are odered, to use index to access items
# [3] Tuples are immutable => you can NOT add, Edit or Delete
# [4] Tuples itmes are not unique
# [5] Tuples can have different data types
# [6] Operators used in strings and lists available here too

myATuple = "Mongo", "Apple"
MyBTuple = ("Mongo", "Apple")
MyCTuple = {"Mongo", "Apple"} # this is set
oneItemTuple = "One", #without , it will be considered as string

#MyBTuple[1] = "Banana"

print(type(myATuple))
print(type(MyBTuple))
print(type(MyCTuple))
print(myATuple)
print(MyBTuple[-1])

# concatenation
conTuple = myATuple + oneItemTuple
print(conTuple)
conTuple2 = MyCTuple + "Two", "Tree" + oneItemTuple
print(conTuple2)
