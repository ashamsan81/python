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