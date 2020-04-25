###################################
# ---------------------------------
#      --- Set Methods ---
###################################

# clear()
a = {1, 3, 5}
a.clear()
print(a)
#a.add(5, 6) #wrong you can only add an item each time
a.add(5)
a.add(6)
# union without repeat
b = {"one", "two"}
b.add(3)
#b.remove(3) # will get an error if item is not exist
b.discard("two")
print(b.union(a))
print(b | a)

c = {8, 9, 10, 1}
#print(c.update(a)) # union without repeat, you need to update it before print
# you can also update with lists items
c.update(a)
c.update(["html", "css"])
print(c)

print("-" * 50)
#difference() # just get the difference between two sets
#difference_update() # get the difference and update the set as well with the difference
originalSet1 = {1,2,3,4,"Roro", "Romio"}
sSet1 = {4,5,6,"yahoo"}
sSet2 = {1,2,3,4,5}
print(originalSet1.difference(sSet2))
print ("-" * 50)
print(originalSet1)
originalSet1.difference_update(sSet2)
print(originalSet1) # not the difference no and the content after difference_update()
print("-" * 50)
originalSet1.update(sSet2)

#intersection()
#intersection_update()
#matual set's items
print(originalSet1)
print(originalSet1.intersection(sSet2))
print("-" * 50)

#symmetric_difference()
#symmetric_difference_update()
# get items that is exists only in one of the two sets ONLY
print(originalSet1.symmetric_difference(sSet1))

e = {1,2,3,4,5,6,7}
f = {1,2,3,4,5}
#issubset()
print(e.issubset(f))
#issuperset()
print(e.issuperset(f))