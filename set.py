# ####################
#     --- Sets ---
# --------------------
# [1] items are enclosed in curly braces { }
# [2] un-ordered and un-indexed
# [3] Indexing, Slicing can't be performed
# [4] Has only immutable data types (numbers, strings, tubles)
#     Lists and Dict can't be used #immutable = means can't added, editted or deleted
# [5] Set items are unique

#myWorngSet = {"Osama", "One", 100, 1, [5, 6, 7]}
#print(myWorngSet)

myRepeatedSet = {"Osama", "One", 100, 1, 100, "one", "One"}
print(myRepeatedSet)
myMixedSet = {"Osama", "One", 100, 1, ("tup1", "tup2", "tup2")}
print(myMixedSet)

