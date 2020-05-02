a = 1 # default value of a (add) 
myList = [] # empty list
while a != "0":

    myList.append(input("enter the item: "))
    a = input("Type 0 To Exit or 1 To Add more items:") or "1"
    if a not in ("0","1"):
        print("invalid value - default value is taken")
        a = "1"

print(f"Your list items are {myList}")
