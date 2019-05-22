
with open('d6smallinput', 'r') as myfile:
  input = myfile.read()

splitInput = input.splitlines()

xCords = map(lambda x: int(x.split(",")[0]), splitInput)
yCords = map(lambda x: int(x.split(",")[1]), splitInput)
cords = zip(yCords,xCords)

cordNums = list()

for i in range(len(cords)):
	cordNums.append(i)

cords = zip(cordNums,cords)

print(cords)

## max X 356, max Y = 355

# create array of 400 x 400

array = [[0 for i in range(10)] for j in range(10)]


# walk through array and calculate closest coordinate, storing a number for each, -1 if two are equidistant

for rowIndex in range(len(array)):

	for colIndex in range(len(array[rowIndex])):

		minDistance = 99
		minDistanceCount = 0

		# for every coordinate in the list
		for thisCord in cords:

			# print("At coordinates: ", rowIndex,",",colIndex,"  comparing ",thisCord[1]," with minDistance: ",minDistance)

			# calculate distance from this spot to this coordinate
			thisDistance = abs(rowIndex - thisCord[1][0]) + abs(colIndex - thisCord[1][1])

			# print("thisDistance is ", thisDistance)

			# if this distance is zero, this is the coordinate.  Record and break.
			if thisDistance == 0:
				array[rowIndex][colIndex] = thisCord[0]
				break

			# if this distance is the same as another distance already recorded, record a -1 and stop
			elif thisDistance == minDistance:
				print("At coordinates: ", rowIndex,colIndex," collision between ", array[rowIndex][colIndex], " and ",thisCord[0])
				array[rowIndex][colIndex] = -1
				minDistanceCount += 1
				

			# if this distance is less than a previously record minimum distance, update the new minimum
			elif thisDistance < minDistance:
				array[rowIndex][colIndex] = thisCord[0]
				minDistance = thisDistance
				minDistanceCount = 0




for row in array: print(row)

totals = [0 for i in range(len(cords))]

for rowIndex in range(len(array)):

	for colIndex in range(len(array[rowIndex])):

		if (array[rowIndex][colIndex] != -1): totals[array[rowIndex][colIndex]-1] += 1

print totals

for firstRowIndex in range(len(array)): totals[array[firstRowIndex][0]] = 0

for lastRowIndex in range(len(array)): totals[array[firstRowIndex][-1]] = 0
for firstColIndex in range(len(array)): totals[array[0][firstColIndex]] = 0
for lastColIndex in range(len(array)): totals[array[-1][firstColIndex]] = 0

print totals
print max(totals)