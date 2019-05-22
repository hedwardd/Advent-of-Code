
with open('d5inputsmall.dat', 'r') as myfile:
  input = myfile.read()




done = False

# dabAcCaCBAcCcaDA

# until done
while done == False:



	# # for char in input
	for char in range(len(input)):
		print input
			
		

		#   # if last character, done = True
		if char == len(input)-1:
				done = True

		# 	# elif input[char] == input[char+1] +/- hex value (32), delete both and start over
		elif (ord(input[char]) == ord(input[char+1]) + 32) or (ord(input[char]) == ord(input[char+1]) - 32):
			input = input[:char] + input[(char+2):]
			break




	
print input
	



