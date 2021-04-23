import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
t1 = "Welcome to programmimg. Programming is fun."
t2 = "More fun is to program with Python."
t3 = "Python is simple yet very fast with multiple functionalities."
t4 = "So, come enjoy programming with Python"
mytext = t1+t2+t3+t4
tokens = [t for t in mytext.split()]
sr = stopwords.words('english')
clean_tokens = tokens[:]
freq = nltk.FreqDist(tokens)
freq.plot(20, cumulative = False)