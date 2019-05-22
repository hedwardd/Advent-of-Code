from functools import reduce

with open('d7inputsmall', 'r') as myfile:
  input = myfile.read()

splitInput = input.splitlines()

# letters = [chr(i+65) for i in range(6)]
# print (letters)

# ints to characters: chr(i+65)
# characters to ints: ord(i-65)

blockers = [[] for i in range(6)]

print blockers

for line in splitInput:

	# Step C must be finished before step A can begin.
	# line[5] == C <-- Blocker
	# line[36] == A <-- Blocked
	print(blockers[ord(line[36])-65])
	print(line[36])
	blockers[ord(line[36])-65].append(line[5])
	print(blockers[ord(line[36])-65])

print("Blockers: ",blockers)

output = []

# while reduce((lambda x, y: len(x)), blockers) != 0:
while len(output) < len(blockers):
	print("output: ",output)
	print("blockers: ",blockers)
	print("len(output): ",len(output))
	print("len(blockers): ",len(blockers))

	for thisStepIndex in range(len(blockers)):
		print("thisStepIndex: ",blockers[thisStepIndex])
		if len(blockers[thisStepIndex]) == 0 and not (chr(thisStepIndex+65) in output):
			output.append(chr(thisStepIndex+65))
			for otherSteps in blockers:
				if chr(thisStepIndex+65) in otherSteps: otherSteps.remove(chr(thisStepIndex+65))
			break
			

print output
