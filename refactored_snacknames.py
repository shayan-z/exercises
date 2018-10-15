# Name list
names = []

# Snack list
snacks = []

# Loop asking 3 user of there names and add to the names list
for index in range(3):
	name = input("What is your name? ")	
	names.append(name)
	

# Loop asking what kind of snack the user like and add to snack list
for name in names:
	snack = input(name + ", what is your favor snack? ")
	snacks.append(snack)
	print(name + " his favor snack is + snacks " + str(snack[0]))