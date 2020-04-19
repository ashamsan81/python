msg = "Hello"
lang = "python"
number = "1" # this will be treated as string as it is inside quotations
number_without_quotations = 1 # this will be treated as number 
number2_without_quotations = 3

#concatenation in python + 
print(number + " " + msg + " " + lang)
print(number_without_quotations + number2_without_quotations) # will add them and result will be 4
#print(number_without_quotations + " " + msg + " " + lang) # will get an error, you can only concatenate data of the same type
#print(number2_without_quotations + " " + number_without_quotations) # error, space is string/different data type

## see the formating section to join different data types in the same sentance
