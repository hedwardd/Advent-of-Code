input = "424 players; last marble is worth 71482 points"

# number of players
numPlayers = 9

# last marble's worth
lastMarb = 25

# players' scores
playerScores = []

# next marble's worth
currentMarb = 2

# location of current marble
currentLoc = 1

# current player
currentPlayer = 0

# circle of marbles
circle = [0, 1]

while currentMarb <= lastMarb:
	print circle
	if currentMarb % 23 == 0:
		print ("hey it's 23")
		# add the current marble to that player's score
		# remove the marble 7 spots counter clock-wise and add it to that player's score
		# current location becomes marble immediately to the right of the removed one
	else:
		# add the current marble to the correct spot
		# "into the circle between the marbles that are 1 and 2 marbles clockwise of the current marble"
		print("Currentlocation: ", currentLoc, "Inserting ", currentMarb, " at location ", currentLoc + 2 % len(circle))
		circle.insert((currentLoc + 2) % (len(circle) - 1), currentMarb)
		currentLoc = circle.index(currentMarb)


	currentMarb += 1


print currentMarb


# print("highscore is: ", max(playerScores))

