movies = {
	"title" : "Billal jan",
	"release year" : 1962,
	"duration" : 120,
	"director" : "Shanba",
	"actors" : ["Bob", "billy", "yahood"]
}
movies["duration"] = f'{movies["duration"]} min'
movies["actors"] = ", ".join(movies["actors"])

for key, value in movies.items():
	print(f'{key} : {value}')
	
# print(f'My fav move is {movies["title"]} the release year was in {movies["release year"]}. The duration of the movie is {movies["duration"]}min and the director is {movies["director"]}')


	
	