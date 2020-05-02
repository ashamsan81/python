### exercise 2
myPrimLeagTuple = "Liverpool", "Man City", "Leicester", "Chelsea", "Man Utd", "Wolves", "Sheffield Utd", "Spurs", "Arsenal", "Burnley", "Crystal Palace", "Everton", "Newcastle", "Southampton", "Brighton", "West Ham", "Watford", "Bournemouth", "Aston Villa", "Norwich"
a = 0
myPrimLeagOrderedTuple = sorted(myPrimLeagTuple)
print("Prime League Teams in Alphapet Order")
while a < len(myPrimLeagOrderedTuple):
    print(f"{a + 1} - {myPrimLeagOrderedTuple[a]}")
    a += 1

print("=" * 40)
a = 0
option = input("Please Choose \n [0] For Top Ranked Teams \n [1] For Last Ranked Teams \n")
if option not in ("0","1"):
    print("Invalid Option")
else:
    numberOfTeams = input("please enter how many Teams you want to display: ")
    if option == "0":
        while a < int(numberOfTeams):
            print(f"{a + 1} - {myPrimLeagTuple[a]}")
            a += 1
    else:
        lastRankedTeams = myPrimLeagTuple[-int(numberOfTeams):]
        while a < len(lastRankedTeams):
            print(f"{a + 1} - {lastRankedTeams[a]}")
            a += 1