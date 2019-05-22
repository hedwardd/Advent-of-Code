
with open('d3smallinput.dat', 'r') as myfile:
  input = myfile.read()

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

input = input.splitlines()

array = [[0 for i in range(10)] for j in range(10)]

for line in input:
	line = line.split()
	# '#1', '@', '1,3:', '4x4'


	xdistance = int(line[2].split(",")[0])
	ydistance = int(line[2].split(",")[1][:-1])
	xlength = int(line[3].split("x")[0])
	ylength = int(line[3].split("x")[1])
	print(xdistance, ydistance)
	print(xlength, ylength)
	
	for row in range(ylength):
		for column in range(xlength):
			# array[xdistance+column][ydistance+row] = array[ydistance][xdistance] + 1
			array[xdistance+column][ydistance+row] = array[xdistance+column][ydistance+row] + 1


	for x in array:
		print(x)
	print("break")


counter = 0
for x in array:
	for y in x:
		if y > 1: counter += 1
print counter
# print(array)
# for x in array:
# 	print(x)