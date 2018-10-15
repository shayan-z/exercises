import json

json.load

with open("movies.json") as f:
	movies = json.load(f)

choose_year = input("What year do you like to show? ")
choose_year = int(choose_year)

choose_duration = input("Length of the movie? ")
choose_duration = int(choose_duration)

for movie in movies:
	title = movie["title"]
	year = movie["year"]
# 	choose_year = input("What")

	if year == choose_year:	
		print(title)