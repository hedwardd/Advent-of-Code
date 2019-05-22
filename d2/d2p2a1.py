import difflib

with open('d2input.dat', 'r') as myfile:
  input = myfile.read()


input = input.splitlines()



## for every line
for thisLine in input:

	# print("line = ", thisLine)


	for thatLine in input:

		diffCount = 0

		output_list = [li for li in list(difflib.ndiff(thisLine,thatLine)) if li[0] != ' ']
		if len(output_list) == 2:
			print(thisLine,thatLine)

		# for i,s in enumerate(difflib.ndiff(thisLine, thatLine)):
		# 	if s[0]==' ': continue
	 #        else:
	 #        	diffCount += 1

  #   	if diffCount == 1:
		# 	print(thisLine, " ", thatLine)
	            





		# value = { k : thatLineCnt[k] for k in set(thatLineCnt) - set(thisLineCnt) }
		# if len(value) == 1:
		# 	print(thisLine, thatLine)
		


		# unmatched_item = set(thisLineCnt.items()) ^ set(thatLineCnt.items())
		# if len(unmatched_item) == 2:
		# 	print(thisLine, " ", thatLine)







	




