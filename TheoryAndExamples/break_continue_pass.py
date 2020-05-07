# -----------------------------------
# break: break the loop and don't continue
# continue: escape the current loop eteration
# pass: can consider as a work around to fill  a code block that is not yet deployed so we don't get errors

myList = [1, 3, 5, 7, 9, 11, 13, 15]
for number in myList:
    if number == 11:
        continue
    print(number)

print("=" * 40)
for number in myList:
    if number == 11:
        break
    print(number)

print("=" * 40)
for number in myList:
    print(number) # the number will show is you print it before the condition
    if number == 11:
        break

print("=" * 40)
for number in myList:
    if number == 11:
        pass # if you don't put pass here you will get an error as print should be in if indentation
    print(number)
