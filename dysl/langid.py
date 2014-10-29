import sys
import codecs

#from dyslib.lm import LM
from social import SocialLM as LM
from corpora.corpuslib import Train

#class LangID(LM):
class LangID:

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
        self.training_timestamp = 0

    def _readfile(self, filename):
        """ Reads a file a utf-8 file,
            and retuns character tokens.

            :param filename: Name of file to be read. 
        """
        f = codecs.open(filename, encoding='utf-8')
        filedata = f.read()
        f.close()
        tokenz = LM.tokenize(filedata, mode='c')
        #print tokenz
        return tokenz

    def train(self, root=''):
        """ Trains our Language Model.

            :param root: Path to training data. 
        """

        self.trainer = Train(root=root)
        corpus = self.trainer.get_corpus()

        # Show loaded Languages
        #print 'Lang Set: ' + ' '.join(train.get_lang_set())

        for item in corpus:
            self.lm.add_doc(doc_id=item[0], doc_terms=self._readfile(item[1]))

        # Save training timestamp
        self.training_timestamp = self.trainer.get_last_modified()

    def is_training_modified(self):
        """ Returns `True` if training data 
            was modified since last training.
            Returns `False` otherwise, 
            or if using builtin training data. 
        """

        last_modified = self.trainer.get_last_modified()
        if last_modified > self.training_timestamp:
            return True
        else:
            return False

    def add_training_sample(self, text=u'', lang=''):
        """ Initial step for adding new sample to training data.
            You need to call `save_training_samples()` afterwards.

            :param text: Sample text to be added.
            :param lang: Language label for the input text.
        """
        self.trainer.add(text=text, lang=lang)

    def save_training_samples(self, domain='', filename=''):
        """ Saves data previously added via add_training_sample().
            Data saved in folder specified by Train.get_corpus_path().

            :param domain: Name for domain folder.
                           If not set, current timestamp will be used.
            :param filename: Name for file to save data in.
                             If not set, file.txt will be used.

            Check the README file for more information about Domains
        """
        self.trainer.save(domain=domain, filename=filename)

    def get_lang_set(self):
        """ Returns a list of languages in training data.
        """
        return self.trainer.get_lang_set()

    def classify(self, text=u''):
        """ Predicts the Language of a given text.

            :param text: Unicode text to be classified.
        """

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

