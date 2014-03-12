import os
import codecs

class Train:

    def __init__(self, root=''):

        #print 'Training'
        if root:
            self.root = root
        else:
            #self.root = 'corpora/corpus-esaren'
            self.root = __file__.rsplit('/',2)[0] + '/corpus-esaren'
        #print self.root
        self.root_depth = len(self.root.split('/')) 
           
    def get_corpus(self):
        self.corpus = []
        self.load()
        return self.corpus

    def visit(self, arg, dirname, names):
        #print dirname
        path = dirname.split('/')
        #print 'path:', path, len(path)

        if len(path) == self.root_depth + 2:
            lang = path[-1]
            names = [name for name in names if not name.startswith('.')]

            for name in names:
                self.corpus.append((lang, dirname + '/' + name)) 
                #print lang, path, dirname + '/' + name

    def load(self):
        os.path.walk(self.root, self.visit, '') 