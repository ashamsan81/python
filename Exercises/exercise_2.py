### exercise 2
myPrimLeagTuple = "Liverpool", "Man City", "Leicester", "Chelsea", "Man Utd", "Wolves", "Sheffield Utd", "Spurs", "Arsenal", "Burnley", "Crystal Palace", "Everton", "Newcastle", "Southampton", "Brighton", "West Ham", "Watford", "Bournemouth", "Aston Villa", "Norwich"
print(len(myPrimLeagTuple))
print("=" * 40)
print("The Top 5 are: {}".format(myPrimLeagTuple[0:5]))
print("=" * 40)
print("The Last 4 are: {},{}".format(myPrimLeagTuple[-1],myPrimLeagTuple[-4:]))
print("=" * 40)
print("Prime League Teams in Alpha: {}".format(sorted(myPrimLeagTuple)))
print("=" * 40)
print("Manchester City Porsition is: {}".format(int(myPrimLeagTuple.index("Man City")+1)))
print("=" * 40)
