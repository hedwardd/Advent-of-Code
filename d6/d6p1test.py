
with open('d6input', 'r') as myfile:
  input = myfile.read()

splitInput = input.splitlines()

xCords = map(lambda x: int(x.split(",")[0]), splitInput)
yCords = map(lambda x: int(x.split(",")[1]), splitInput)
cords = zip(yCords,xCords)

print(max(xCords))
print(max(yCords))