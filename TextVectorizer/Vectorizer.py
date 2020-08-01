import spacy 
from subprocess import run
import logging
#from TextCalssfier import set_logger
from os.path import basename
from .algorithm import strategies,get_similarity,get_annotation

class Vectorizer:
    def __init__(self,vectorizer_name='spacy'):
        ''' Initialize the vectorizer based on vectorizer name
            Available Transformers are: bert, xlnet, roberta, distilbert

        Args:
            vectorizer_name (str): Name of the vectorizer
        
        '''
        self.vectorizer_name = vectorizer_name.lower()
        self.vectorizer = None
        #self.logger = set_logger(basename(__file__))
        if vectorizer_name =='spacy':
            self.vectorizer = self.load_model('en_core_web_sm')
        elif vectorizer_name =='bert':
            self.vectorizer = self.load_model('en_trf_bertbaseuncased_lg')
        elif vectorizer_name =='xlnet':
            self.vectorizer = self.load_model('en_trf_xlnetbasecased_lg')
        elif vectorizer_name =='roberta':
            self.vectorizer = self.load_model('en_trf_robertabase_lg')
        elif vectorizer_name =='distilbert':
            self.vectorizer = self.load_model('en_trf_distilbertbaseuncased_lg')
        else:
            print('Vectorizer is not avalable please mention name from below list :')
            print('bert, xlnet, roberta, distilbert')
            
    def create_vector(self,text,strategy='average'):
        ''' Creating vector for given text

        Args:
            text (str): Input sentence
            strategy (str): Strategy to aggregate the word vectors. Options are
                            [Average, Min, Max, Multiply]
        
        Returns:
            Array : vector of the input text
        '''
        if len(text.strip().split()) > 1:
            tmp = []
            for i in text.strip().split():
                tmp.append(self.vectorizer(i).vector)
            return strategies(tmp,strategy)
        else:
            return self.vectorizer(text).vector

    def check_model_available(self,model_name):
        ''' Checking if transfomer is present

        Args:
            model_name (str): Transformer name
        
        Returns:
            bool : Availability of model
        '''
        return spacy.util.is_package(model_name)
    
    def load_model(self,model_name):
        ''' Loding the transfomer object in vectorizer
        
        Args:
            model_name (str): Transformer name
        
        Returns:
            `spacy.lang.en.English` : spacy object 
        '''
        if self.check_model_available(model_name):
            #self.logger.info('Loading the model {}'.format(model_name))
            return spacy.load(model_name)
        else:
            #self.logger.info('Downloading the transformer {} Please wait...'.format(model_name))
            try:
                #self.logger.in()
                run(['python','-m','spacy','download',model_name])
                return spacy.load(model_name)
            except Exception as e:
                #self.logger.info('Please check your Internet Connection')
                print(e)
    
    def similarity(self,doc1,doc2):
        return get_similarity(doc1,doc2,self.vectorizer)
    
    def annotate(self,sent):
        tmp = self.load_model('en_core_web_sm')
        return get_annotation(sent,tmp)
'''
def main():
    text1= 'Apple is a company'#,'He is also good']
    text2 = 'Apple is a fruit'
    vec = Vectorizer()
    vec_temp = vec.annotate(text1)
    for token in vec_temp:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
    #print('Similarity of Documents :{}'.format(vec.similarity(text1,text2)))
    print('Length of Vector : {}'.format(len(vec_temp)))

if __name__ == "__main__":
    main()
'''