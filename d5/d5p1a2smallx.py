
with open('d5inputsmall.dat', 'r') as myfile:
  input = myfile.read()


input = list(input)

input = map(lambda x: ord(x), input)

print input


clean = False

# dabAcCaCBAcCcaDA

# until done
while clean == False:

	clean = True


	# for char in input
	for char in input:
		
			
		

		
		if (char == input[input.index(char) + 1] + 32) or (char == input[input.index(char) + 1] - 32):
			# input = input[:char] + input[(char+2):]
			input.pop(input.index(char) + 1)
			input.pop(input.index(char))
			clean = False
			

input = map(lambda x: chr(x), input)

print input



