import os
import codecs

class Train:

    def __init__(self, root=''):

        #print 'Training'
        if root:
            self.root = root
        else:
            self.root = 'corpora/corpus-esaren'

    def get_corpus(self):
        self.corpus = []
        self.load()
        return self.corpus

    def visit(self, arg, dirname, names):
        path = dirname.split('/')

        if len(path) == 4:
            lang = path[-1]
            names = [name for name in names if not name.startswith('.')]

            for name in names:
                self.corpus.append((lang, dirname + '/' + name)) 
                #print lang, path, dirname + '/' + name

    def load(self):
        os.path.walk(self.root, self.visit, '') 