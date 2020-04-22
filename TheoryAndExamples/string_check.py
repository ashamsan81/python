#### functions to check your string

stringToCheck1 = "Can You Check What Am I 3D"

print(stringToCheck1.istitle())
print(stringToCheck1.isupper())
print(stringToCheck1.islower())
print(stringToCheck1.isnumeric()) # false as it is not numeric
print(stringToCheck1.isalpha())   # false as it contains spaces
print(stringToCheck1.isalnum()) #alphaptic and numeric  false as it contains spaces
print ("-----------------------------")
stringToCheck2 = "Chatwithoutspaces"
print(stringToCheck2.isnumeric())
print(stringToCheck2.isalpha())
print(stringToCheck2.isalnum()) #alphaptic and numeric 
print ("-----------------------------")
stringToCheck3 = "Chatwithoutspaces123"
print(stringToCheck3.isnumeric())
print(stringToCheck3.isalpha())
print(stringToCheck3.isalnum()) #alphaptic and numeric will be true if it has either alpha or numeric or both without spaces
print ("-----------------------------")
stringToCheck4 = "1 2 3 4 5"
print(stringToCheck4.isnumeric()) # also false as it contains spaces
print(stringToCheck4.isalpha())
print(stringToCheck4.isalnum()) #alphaptic and numeric 

print ("-----------------------------")
stringToCheck5 = "12345"
print(stringToCheck5.isnumeric()) # also false as it contains spaces
print(stringToCheck5.isalpha())
print(stringToCheck5.isalnum()) #alphaptic and numeric 



