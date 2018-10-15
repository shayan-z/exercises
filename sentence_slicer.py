sentence = input("Enter a sentence ")

sentence_len = len(sentence)

list(sentence)

sentence_word = sentence.split(" ")

calculate1 = sentence_len * 0.25
calculate2 = sentence_len * 0.75

calculate1 = round(calculate1)
calculate2 = round(calculate2)

sentence_word = " ".join(sentence_word)

print(sentence_word[calculate1:calculate2])

