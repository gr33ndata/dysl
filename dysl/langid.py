import codecs

from dyslib.lm import LM
from corpora.corpuslib import Train

class LangID:

    def __init__(self):

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
        tokenz = [ch for ch in filedata]
        #print tokenz
        return tokenz

    def train(self):

        train = Train()
        corpus = train.get_corpus()

        for item in corpus:
            self.lm.add_doc(doc_id=item[0], doc_terms=self._readfile(item[1]))

    
    def classify(self, text=u''):

        tokenz = [ch for ch in text]
        result = self.lm.calculate(doc_terms=tokenz)
        lang = result['calc_id']
        return lang

if __name__ == '__main__':

    l = LangID()
    l.train()
    text = u'Hello, World'
    lang = l.classify(text)
    print text, '[ Language:', lang, ']'