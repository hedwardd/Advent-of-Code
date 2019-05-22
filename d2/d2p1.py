from collections import Counter;

with open('d2input.dat', 'r') as myfile:
  input = myfile.read()

cnt = Counter()

input = input.splitlines()

twos = 0
threes = 0

## for every line
for line in input:

	print("line = ", line)

	cnt = Counter()

	for char in line:
		# print("hello")
		cnt[char] += 1

	hasTwo = False
	hasThree = False

	for char in cnt:
		if cnt[char] == 2:
			hasTwo = True
		if cnt[char] == 3:
			hasThree = True

	if hasTwo == True:
		twos += 1

	if hasThree == True:
		threes += 1

print twos
print threes
print twos * threes
	

    # for k, v in store.iteritems():
	


# ## count occurences of letter in the string

# list = ('a', 'a', 'b', 'c', 'c')
#     for data in list:
#         countoccurrences(store, data)
#     for k, v in store.iteritems():

## iterate counters








# for i in input:
# 	for j in i:
# 		if j == "n": ns += 1
# 		if j == "s": ns -= 1
# 		if j == "e": ew += 1
# 		if j == "w": ew -= 1
# 	if abs(ns) > abs(maxns): maxns = ns
# 	if abs(ew) > abs(maxew): maxew = ew


# if (ns > ew): print ns
# else: print ew

# if (maxns > maxew): print maxns
# else: print maxew
