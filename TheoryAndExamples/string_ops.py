######################################
# operations on strings
# [1] All data in pythong are objects
# [2] object contain Elements
# [3] Every Element has its own Index
# [4] Python uses zero based indexing
# [5] Use Squar brackets to access elements 
# [6] enable accessing parts of strings, tuples or lists
#---------------------------------------------------------


#### Indexing
# var[Start(default 0):End(default last index -1):Steps(default 1)]
# start must be before the ends. i.e [3:1] or [-2:-5] this is wrong you won't get an output
# [-1:0] is not wrong, will print out the last character only
myString = "Hi I'm Python"

print(myString[4]) # print index number 4 
print(myString[-2]) # print index 2 starting backwords

print(myString[-5:-2]) # from index 2 backwords  to 5 backwords
print(myString[5:-2])  # is there any different??
print(myString[3:1])

print(myString[-1:])
#### Slicing
print(myString[0::2])

###### String Methods
# get the length of String by len()
print(len(myString))

###### strip(), rstrip(), lstrip() remove spaces by default 
# or any character provided in function arguments between ""
myEditString1 = "        This Edited String         "
print(myEditString1.strip())
print(myEditString1.rstrip())
print(myEditString1.lstrip())

myEditString2 = "%$$%#$String without special Characters $$$#"
print(myEditString2.strip("%$#"))
print(myEditString2.rstrip("%$#"))
print(myEditString2.lstrip("%$#"))

#covert string into a title (Capitalize the first letter or eacho word and after numbers)
myEditString3 = "This IS TITLE 2d. suBject 20r"
print(myEditString3.title())

#Capitalize all letters
print(myEditString3.upper())
# make only the first letter of the string Capital
print(myEditString3.capitalize()) 

#smallize all letters
print(myEditString3.lower())

#zfill : add zeros to the left of the number so all numbers digists are same
a, b , c , d ,e = "1", "2", "99", "100", "9999"
print(a.zfill(4)) # 0001
print(b.zfill(4)) # 0002
print(c.zfill(4)) # 0099
print(d.zfill(4)) # 0100
print(e.zfill(4)) # 9999

#split() and rsplit()
# split provided text into words based on the separator provided, speace is the default separator.
# you can provide max split which means how many splits you looking for
# change the string into a list

myEditString4 = "Hi, Look how you can user-this-separators"
print(myEditString4.split())
print(myEditString4.split("-"))
print(myEditString4.split("-",2))
print(myEditString4.rsplit("-"))
print(myEditString4.split(","))
print(myEditString4.rsplit("-",2)) # the right of the string 

# there is also splitlines() to do the same as split() do but with lines
myLineString =""" First Line
Second Line
Third Line"""

print(myLineString.splitlines())

# center, position a sting into a center of provided characters and places
# by default space is the character
myEditString5 = "This is Managed by Ansible"
print(myEditString5.center(len(myEditString5)+4,"#"))

#rjust(), ljust()
#add spaces (by default) or any provided character either to the right or to the left
print(myEditString5.rjust(len(myEditString5)+4))
print(myEditString5.rjust(len(myEditString5)+4,"#")) # add to right of the line then the string
print(myEditString5.ljust(len(myEditString5)+4))
print(myEditString5.ljust(len(myEditString5)+4,"#")) # add to left the line after the string





# count how many word/char provided in given string
print(myEditString5.count("is"))
print(myEditString5.count("is",10))
print(myEditString5.count("is",1,5))

# swap letters cases
print(myEditString5.swapcase())

# starts with/ end with - check condition if your string starts with provided charcter or ends with it
print(myEditString5.startswith("i"))
print(myEditString5.startswith("is",2))
print(myEditString5.endswith("A"))
print(myEditString5.endswith("A",0,20))

# find and index will return the index number of provided substring (first one to find) 
# with index if the char is doesn't exist will return error while find will return -1
#index/find("substring[,starts_from-index][,ends_at-index]")
print(myEditString5.index("is"))
print(myEditString5.find("is",3))
print(myEditString5.find("AA"))
#print(myEditString5.index("AA")) # will give you an error

#expandtabs(int) to specify the number of spaces to apply for tabs \t
print("This\tis\tnormal\ttabs\tspacing")
print("This\tis\tcustomized\ttabs\tspacing".expandtabs(2))

# replace string (string_to_be_replaced,string_to_replace[,count])
myReplaceString = "one two three one one"
print(myReplaceString.replace("one","1"))
print(myReplaceString.replace("one","1",1)) # will replace the first "one" string to find
print(myReplaceString.replace("one","1",2)) # will replace the first two "one" string to find

#"what_to_use_as_a_separator_between_each_list_item".join(list|tuple)
# the result will be a string type
myList = ["I" , "will" , "become" , "string"]
print("-".join(myList))
print(" ".join(myList))
