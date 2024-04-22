# read txt file 
txt_file = open('random_paragraphs.txt')
txt = txt_file.read(10000)
print(txt)
print('\n')

# remove stop words like a, an, in, but, if, out, .... using spacy library
import spacy
# load spacy english model 
nlp = spacy.load("en_core_web_sm")
doc = nlp(txt)

txt_non_stopwords = ' '.join([token.text for token in doc if not token.is_stop])
print(txt_non_stopwords)
print('\n')

# find frequency of word
listString = txt_non_stopwords.split()

freq = {word: listString.count(word) for word in set(listString)}
print(freq)
print('\n')
