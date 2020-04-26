# ------------------------------------------
#       -------- Type Coversion -------- 
# ------------------------------------------
# str() convert to string
# int() convert to integer 
# tuple() convert to tuple
# list() convert to list
# set() convert to set
# dict() covert to dictionary


# examples

sStr = "Ahmed"
lList = ["A", "B"]
# print(set(sStr)) # string can't be converted to dict
#print(dict(lList)) # only nested lists or tuples can be coverted to dict
nList = [["A", 1],["B",2],["C",3]]
print(dict(nList))
