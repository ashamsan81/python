# example of nexted for loop

teamSkils = {
    "Ahmed" : {
        "html" : "90%",
        "Linux" : "80%",
        "Ansible" : "90%"
    },
    "Faris" : {
        "html" : "0%",
        "football" : "90%",
        "Tennis" : "100%"
    },
    "Faras" : {
        "footback" : "100%"
    },
    "Rahaf" : {
        "basketball" : "100%"
    }
}

for team in teamSkils:
    print("-" * 40)
    print(f"Team Memeber {team} has the following Skills : ")
    print("-" * 40)
    for skills in teamSkils[team]:
        print(f" - {skills} ==> {teamSkils[team][skills]}")