# ---------------------------------------
#      --- Boolean ---
# ---------------------------------------

print(bool("User1")) # true as there is an existing value
print(bool("")) # false as there is no value even on space
print("-" * 50)
print(bool(True)) # true value
print(bool(False)) # false value
print("-" * 50)
print(bool([1,2,3,4])) # true existing values
print(bool([])) # false no existing values
print("-" * 50)
print(bool({})) # false no existing values
print("-" * 50)
print(bool(None)) # false, None value is considered a no value (null value)
print(bool(0)) # zero value still false
print("-" * 50)

age = 30
country = "NZ"
rank = 10

print(age > 36 and country == "NZ"  and rank ==10)
print(not age > 36 or not country == "NZ")
print(not age > 29 or not country == "NZ")
print(age >= 30 and rank <= 10)