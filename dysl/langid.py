import sys
import codecs

#from dyslib.lm import LM
from social import SocialLM as LM
from corpora.corpuslib import Train

class LangID(LM):

    def __init__(self, unk=False):

        # Shall we mark some text as unk,
        # if top languages are too close?
        self.unk = unk
        self.min_karbasa = 0.08

        # LM Parameters
        ngram = 3
        lrpad = u' '
        verbose = False
        corpus_mix = 'l'

        self.lm = LM(n=ngram, verbose=verbose, lpad=lrpad, rpad=lrpad,
                smoothing='Laplace', laplace_gama=0.1,
                corpus_mix=corpus_mix)

        self.trainer = None

    def _readfile(self, filename):

        f = codecs.open(filename, encoding='utf-8')
        filedata = f.read()
        f.close()
        tokenz = LM.tokenize(filedata, mode='c')
        #print tokenz
        return tokenz

    def train(self, root=''):

        self.trainer = Train(root=root)
        corpus = self.trainer.get_corpus()

        # Show loaded Languages
        #print 'Lang Set: ' + ' '.join(train.get_lang_set())

        for item in corpus:
            self.lm.add_doc(doc_id=item[0], doc_terms=self._readfile(item[1]))

    def add_training_sample(self, text=u'', lang=''):
   
        self.trainer.add(text=text, lang=lang)

    def save_training_samples(self, domain='', filename=''):

        self.trainer.save(domain=domain, filename=filename)

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

    if len(sys.argv) > 1:
        text = u' '.join(sys.argv[1:])
    else:
        text = u'hello, world'

    lang = l.classify(text)
    print text, '[ Language:', lang, ']'

