names = []
count = 0
while (count < 3):
	name = input("What is your name? ")	
	count = count + 1
	names.append(name)
	
print(names)


snacks = []
#count = 0
for name in names:
	snack = input(name + ", what is your favor snack? ")
	snacks.append(snack)
	#count = count + 1
	
print(snacks)

