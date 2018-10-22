import requests
import json



def wiki_api(title, value):
	wiki = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"				
	r = requests.get(wiki)
	return r	
	data = json.loads(r.text)

	if r.status_code != 200:
		#index = wiki_language.index(lan)
		#complet = wiki_language_complet[index]
		return f"Error, We cant find any article in {complet}"
	else:
		if value == "extract":
			return data["title"] + "\n" + "\n" + data["extract"]
			
		elif value == "description":
			return data["title"] + "\n" + data["description"] 



title = input("Enter the article you are searching: ").strip('').replace(" ", "_")
value = input("Do you want description or extract: ").strip('').lower()


print(wiki_api(title, value))