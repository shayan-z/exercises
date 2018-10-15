words = ["appel", "oraneg", "poeple", "cumputer", "playstatian", "rainn"]

correct_word = ["apple", "orange", "people", "computer", "playstation", "rain"]
sentence = input("Enter a sentence: ")

list(sentence)

sentence_word = sentence.split(" ")

for word in sentence_word:
    if word in words:
    	sentence_word = " ".join(sentence_word)
    	if word == "appel":
    		correct = "apple" 
    		print(word + " is a wrong word. The correct word is " + correct)	
    		replace = sentence.replace(str(word), str(correct))
    	elif word == "oraneg":
    		correct = "orange"
    		print(word + " is a wrong word. The correct word is " + correct)
    		replace = sentence.replace(str(word), str(correct))
    	elif word == "poeple":
    		correct = "people"
    		print(word + " is a wrong word. The correct word is " + correct)
    		replace = sentence.replace("poeple", "people")
    	elif word == "cumputer":
    		correct = "computer"
    		print(word + " is a wrong word. The correct word is " + correct)
    		replace = sentence.replace(str(word), str(correct))
    	elif word == "playstatian":
    		correct = "playstation"
    		print(word + " is a wrong word. The correct word is " + correct)
    		replace = sentence.replace(str(word), str(correct))
    	elif word == "rainn":
    		correct = "rain"
    		print(word + " is a wrong word. The correct word is " + correct)
    		replace = sentence.replace(str(word), str(correct))
    correct_word = " ".join(correct_word)
print(replace)