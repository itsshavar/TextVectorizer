# TextVectorizer
A Library for representation learning of Text using Transformers such as BERT, AlBERT, RoBERTA and spacy

# Text Annotation
```
>>> from TextVectorizer import Vectorizer
>>> from TextVectorizer import Vectorizer
>>> vec = Vectorizer()
>>> for i in vec.annotate('Hi I am Rahul'):
...     print(i.text,i.pos_)
Hi INTJ
I PRON
am AUX
Rahul PROPN
````

# Document Similarity
```
>>> from TextVectorizer import Vectorizer
>>> vec = Vectorizer('bert')
>>> doc1  = 'Apple is a company'
>>> doc2 = 'Apple is fruit'
>>> vec.similarity(doc1,doc2)
0.622238214831199
```

# Create Vector
```
>>> from TextVectorizer import Vectorizer
>>> vec = Vectorizer('bert')
>>> doc1  = 'Apple is a company'
>>> vec.create_vector(doc1)
array([ 1.86449289e-01, -4.55981702e-01, -5.55467248e-01, -1.63073212e-01,
        ...
        7.34284699e-01,  5.51161587e-01, -2.69515336e-01, -2.89130598e-01],
      dtype=float32)

```
