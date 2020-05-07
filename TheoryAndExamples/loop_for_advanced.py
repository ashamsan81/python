# advanced for loop is where you use two counters
# in dictionary you may use myDict.items()
# examples

mySkills = {
    "html" : "100%",
    "CSS" : "90%",
    "JS" : "50%"
}

# old way
# for skill in mySkills:
#     print(f"Skill Evaluation for {skill} = {mySkills[skill]}")

#advance way
for skills, value in mySkills.items():
    print(f"{skills} --> {value}")