from collections import Counter;

with open('d2input.dat', 'r') as myfile:
  input = myfile.read()


input = input.splitlines()



## for every line
for thisLine in input:
	thisLineCnt = Counter()

	# print("line = ", thisLine)

	

	for char in thisLine:
		thisLineCnt[char] += 1

	for thatLine in input:
		thatLineCnt = Counter()

		for char in thatLine:
			thatLineCnt[char] += 1

		value = { k : thatLineCnt[k] for k in set(thatLineCnt) - set(thisLineCnt) }

		if len(value) == 1:
			print(thisLine, thatLine)
		


		# unmatched_item = set(thisLineCnt.items()) ^ set(thatLineCnt.items())
		# if len(unmatched_item) == 2:
		# 	print(thisLine, " ", thatLine)







	




