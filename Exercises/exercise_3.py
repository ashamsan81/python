# exercise3 - slice email address
email = input("please enter your email: ")
email = email.strip()
getIndex = email.index("@")
print("username : {}".format(email[:getIndex]))
print("domain : {}".format(email[getIndex+1:]))