#Ask what her/his name is and what what her/his lovers name is
name_1 = input("What is your name? ")
name_2 = input("What is your lovers name? ")

#add both names togheter and make them lowercase and strip it.
both_names = name_1.lower().strip() + name_2.lower().strip()

#Check the length of the names
names_length = len(both_names)


if names_length >= 10:
	#If the length is 10 or more
	print("Go marry now!")	
elif names_length >= 5:
	#If the length is 5 or more
	print("You guys are awesome!")
else:
	print("Break with each other")