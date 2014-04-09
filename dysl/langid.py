import codecs

#from dyslib.lm import LM
from social import SocialLM as LM
from corpora.corpuslib import Train

class LangID(LM):

    def __init__(self, unk=False):

        # Shall we mark some text as unk
        # If top languages are too close.
        self.unk = unk
        self.min_karbasa = 0.08

        # LM Parameters
        ngram = 3
        lrpad = u' '
        verbose=False
        corpus_mix='l'

        self.lm = LM(n=ngram, verbose=verbose, lpad=lrpad, rpad=lrpad, 
                smoothing='Laplace', laplace_gama=0.1, 
                corpus_mix=corpus_mix)

    def _readfile(self, filename):

        f = codecs.open(filename, encoding='utf-8')
        filedata = f.read()
        f.close()
        tokenz = LM.tokenize(filedata, mode='c')
        #print tokenz
        return tokenz

    def train(self):

        train = Train()
        corpus = train.get_corpus()

        for item in corpus:
            self.lm.add_doc(doc_id=item[0], doc_terms=self._readfile(item[1]))

    
    def classify(self, text=u''):

        text = self.lm.normalize(text)
        tokenz = LM.tokenize(text, mode='c')
        result = self.lm.calculate(doc_terms=tokenz)
        #print 'Karbasa:', self.karbasa(result)
        if self.unk and self.karbasa(result) < self.min_karbasa:
            lang = 'unk'
        else:
            lang = result['calc_id']
        return lang

if __name__ == '__main__':

    l = LangID(unk=False)
    l.train()
    text = u'hello, world'
    lang = l.classify(text)
    print text, '[ Language:', lang, ']'

    text = u''
    lang = l.classify(text)
    print text, '[ Language:', lang, ']'
