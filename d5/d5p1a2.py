
with open('d5input.dat', 'r') as myfile:
  input = myfile.read()


input = list(input)

for char in range(len(input)):
	input[char] = ord(input[char])


clean = False

# dabAcCaCBAcCcaDA

# until done
while clean == False:

	clean = True


	# for char in input
	for char in range(len(input)):
		
			
		

		# if last character, done = True
		if char == len(input)-1:
				print ("hey")

		# elif input[char] == input[char+1] +/- hex value (32), delete both and start over
		elif (input[char] == input[char+1] + 32) or (input[char] == input[char+1] - 32):
			# input = input[:char] + input[(char+2):]
			input.pop(char)
			input.pop(char)
			clean = False
			

for char in range(len(input)):
	input[char] = chr(input[char])
print input




