##########################################
# -------------- Formatting --------------
# formatting reference can be found here: https://pyformat.info/
# What is place holder?
# placeholder, usually in a print function to reserve a spot for this variable before explicitly saying what the variable is.
# old way formating
# %s place holder for string %.#s to concatenate strings by number in replaces #
# %d place holder for number (integer)
# %f place holder for floating point %.#f limit the digits after . by #. i.e %.2f => 1.00

# New way formating
# instead of %s you use {} or {:s} or {:.5f} see above to compare then .format(vars)
station = "FM"
frequancy = 99
program = "Good morning World"
host = "Andy Paul"
section = 3
# old
print("Welcom to %s you always can find us on frequency %f this is %s presneting %s and we are now presnting section %d" % (station,frequancy,host,program,section))
print("Welcom to %s you always can find us on frequency %.3f this is %s presneting %.5s and we are now presnting section %d" % (station,frequancy,host,program,section))
# new Version 3
print("Welcom to {:s} you always can find us on frequency {:.3f} this is {:s} presneting {:.5s} and we are now presnting section {:d}".format(station,frequancy,host,program,section))
# changing orders
num1 = 1
num2 = 2
num3 = 3
print("correct order {} {} {}".format(num1,num2,num3))
print("changing order {2},{0},{1}".format(num1,num2,num3)) # order is like index starts with 0
print("changing order with type of data {2:.2f} {0:.2f} {1:.2f}".format(num1,num2,num3))

# format currency 
amount = 30030030281

print("amount = {:,d}".format(amount)) # will put a comma every 3 digits starting from units

# 3.6 formatting 
print(f"correct order {num1} {num2} {num3}")

