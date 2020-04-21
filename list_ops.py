#-----------------------------
# --- List Methods and Ops ---
#-----------------------------

# append()
# extend()
# sort()
# revers()
# clear()
# copy()
# insert(index,object) # insert befor index
# pop()

myAList = ["orange", "Apple", 1, 10, 9.2, 8.5,11]
myBList = ["nuts", True]
myCList = ["TV", "Laptop"]
myDList = [1, 2, 25, 15, 10]
myAcopyList = myAList.copy()
myAList.append("itemToAdd1")
myAList.append(100)
myAList.append(myBList)

myBList.extend(myCList)
myDList.insert(-1,111)

print(myAList)
print("-------------------------------")

print(myAcopyList)
print("-------------------------------")
#myAList.remove(myAList[0:2]) # wrong you have to explicity specify an item not a list
#print(myAList.sort()) # can't sort a list of different data types
print(myDList.sort(reverse=False)) # output will be None, you have to sort it before printing it
print("-------------------------------")
myDList.sort(reverse=False)
print(myDList)
print(myAList[9][0]) # will get the first item of the appended list
print("-------------------------------")
print(myBList)
print("-------------------------------")
print(myAList.reverse()) # none result as well, you have to revers first
print("-------------------------------")
myBList.reverse()
print(myBList)

myCList.clear()
print(myCList)


