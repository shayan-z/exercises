# Make a list
users = []

count = 0
while (count < 3):
	name_input = input("What is your friends name? ") # Asking for friends name
	users.append([name_input]) # Adding friends name to the list
	name_friend = users[count] # Counting whitch number
	name_friend = "".join(name_friend) # taking out of the list
	snack_input = input("what is " + name_friend + " favor snack? ") # Asking for friends snack
	users[count].append(snack_input) # Adding to the list
	count += 1
print(users)

	





