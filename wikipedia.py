import requests
import json

article = input("Enter the article you are searching: ").strip('')
article = article.replace(" ", "_")

wiki_language_complet = ["English", "Spanish", "German"]
wiki_language = ["en", "es", "de"]




for lan in wiki_language:
	wiki = f"https://{lan}.wikipedia.org/api/rest_v1/page/summary/"

	url = wiki + article
	
	r = requests.get(url)
	
	data = json.loads(r.text)
	
	if r.status_code != 200:
		index = wiki_language.index(lan)
		complet = wiki_language_complet[index]
		print(f"Error, We cant find any article in {complet}")
	else:
		if "description" not in data:
			print(data["title"] + "\n" + "\n" + data["extract"])
		else:
			print(data["title"] + "\n" + data["description"] + "\n" + data["extract"])





	

	








