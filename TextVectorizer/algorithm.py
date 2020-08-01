from numpy import mean, max, min, multiply

def strategies(vector, strategy='average'):
    ''' Returns aggragated vector based on given startegy

    Args:
        vector (List[Float]): List of word vectors
        strategy (str) :  Strategy to aggregate the vector
    
    Returns:
        Array : Sentence Vector 
    '''
    if strategy == 'average':
        return mean(vector, axis=0)
    elif strategy == 'min':
        return min(vector)
    elif strategy == 'max':
        return max(vector)
    else:
        return multiply(vector)


def get_similarity(doc1, doc2, vectorizer):
    ''' Returns simlarity score of two documents

    Args:
        doc1 (str): Document to be compared 
        doc2 (str) :  Document to be compared with
    
    Returns:
        Float : Similarity Score 
    '''

    return vectorizer(doc1).similarity(vectorizer(doc2))

def get_annotation(sent,vectorizer):
    ''' Returns the Annotation of given senetence.This includes POS Tag
        NER, Dependecy etc.

    Args:
        sent (str): sentence to be tagged
    
    Retruns 
        spacy.token : Tagged iterator object.
    '''
    return vectorizer(sent)
