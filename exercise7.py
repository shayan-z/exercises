f = open("football_players.csv")
fw = open("football_players.txt","w")
for player in f:
	row = player.strip().split(",")
	name_player = row[0]
	club = row[1]
	price = row[2]
	price = int(price + "000000")
	
	sentence = name_player + " is a player of " + club + " and has cost €" + str(price) + " mil "
	fw.write(sentence + "\n")
	print(sentence)
f.close()

name_player = 	input("What is the name of the player? ")
club 		= 	input("Which club did he/she join? ")
price 		= 	input("How much did the club pay for him?(e.g 200, 300)")

add_new_player = name_player + " " + club + " " + price

fw.write(add_new_player + "\n")
f.close()
print(add_new_player)
