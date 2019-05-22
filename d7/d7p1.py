with open('d7input', 'r') as myfile:
  input = myfile.read()

splitInput = input.splitlines()

blockers = [[] for i in range(26)]

for line in splitInput:
	blockers[ord(line[36])-65].append(line[5])

output = []

while len(output) < len(blockers):

	for thisStepIndex in range(len(blockers)):

		if len(blockers[thisStepIndex]) == 0 and not (chr(thisStepIndex+65) in output):
			output.append(chr(thisStepIndex+65))
			for otherSteps in blockers:
				if chr(thisStepIndex+65) in otherSteps: otherSteps.remove(chr(thisStepIndex+65))
			break
			

print output