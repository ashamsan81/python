# -------------------------------------
#    ---- dictionary methods
# -------------------------------------
# 
# clear()
# update()
# copy()
# setdefault(): to set a default value 
user = {
    "name": "User1"
}
user.setdefault("age", 36)
print(user) # note that age will be added to user dict
print("-" * 50)
# popitem(): will get the last itme added to dictionary
print(user.popitem())
print("-" * 50)
# to create new dict with values of another dict
linkedItems = user # is it going to add the default value # no
copiedItems = user.copy()
print(linkedItems)
print("-" * 50)
user["home"] = "/etc/shell" # another way to add item to dict
print(user)
print(linkedItems)
print(copiedItems) # note the different between linkedItems and copied items
print("-" * 50)

#fromkeys() to create dict from lists keys
list1 = ("key1","key2","key3")
list2 = ("value1","value2")
string1 = "default_value"

print(dict.fromkeys(list1, string1))
print(dict.fromkeys(list1,list2))