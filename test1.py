import nltk

text = nltk.word_tokenize('what does the fox say')
print(text)

Tag = nltk.pos_tag(text)
print(Tag)