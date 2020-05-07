#############################################
#           ##### for Loop #####          #
#############################################
# for <var> in <list>: # the difference between while is 
# while depends on conditions while here depends on a list of values
#   do something
# [else:] #optional
#   do something

myList = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for number in myList:
    if int(number) % 2 == 0 :
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")
else:
    print("loop is finished")


sStr="Ahmed"
for letter in sStr:
    print(letter.upper())

# range funtion range(start:int,stop:int,step:int)
# myRange = range(0,100,2)
# for number in myRange:
#     print(number)

# display dictionary
mySkills = {
    "html" : "100%",
    "CSS" : "90%",
    "JS" : "50%"
}
