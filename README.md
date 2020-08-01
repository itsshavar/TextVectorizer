# TextVectorizer
A Library for representation learning of Text using Transformers such as BERT, AlBERT, RoBERTA and spacy

# Text Annotation
>>> from TextVectorizer import Vectorizer
>>> from TextVectorizer import Vectorizer
>>> vec = Vectorizer('bert')
>>> for i in vec.annotate('Hi I am Rahul'):
...     print(i.text,i.pos_)
Hi INTJ
I PRON
am AUX
Rahul PROPN

# Document Similarity
>>> from TextVectorizer import Vectorizer
>>> vec = Vectorizer()
>>> doc1  = 'Apple is a company'
>>> doc2 = 'Apple is fruit'
>>> vec.similarity(doc1,doc2)
0.622238214831199

