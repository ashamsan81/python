# --------------------------------
#     ---- Dictionary ----
# --------------------------------
# [1] dict items are enclosed in curly braces {}
# [2] dict items are key: values pair with , comma separator between each pair
# [3] dict key MUST be Immutable => numbers, string, tuples, List is NOT Allowed
# [4] dict values can have any data types
# [5] dict key MUST be unique, NO Error though, but it will take the last value assigned
# [6] it is not Index base but it is key based
# [7] can be nested

user = {
    "name": "user1",
    "home": "/etc/shell",
    "skills": ["html", "css","js"],
    "rating": 10
}

print(user)
print(user["skills"])
print(user.get("rating"))
print(user.keys()) # print all dict keys
print(user.values()) # print all values

# Two diminsions dict
lang = {
    "one": {
        "name": "html",
        "progress": "90%"
    },
    "two": {
        "name": "csss",
        "progress": "95%"
    }
}

#you can also put sub dict separatly and join them all in one later like below
#lang1 = {
    #key1: value,
    #key2: value
# }
#lang2 = {
    #key2: value,
    #key2: value
# }
#lang = {
    #one: lang1,
    #two: lang2
# }
print(lang)
print(lang["one"])
print(lang["two"]['name'])

print(len(lang))
print(len(lang["one"]))
print(len(lang["two"]['name']))
