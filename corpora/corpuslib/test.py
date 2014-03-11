import os
import codecs

class Test:

    def __init__(self, root='', langid=None, accuracy=None):

        #print 'Testing'
        if root:
            self.root = root
        else:
            self.root = '../corpora/corpus-esaren.test'
        self.langid = langid
        self.a = accuracy

    def visit(self, arg, dirname, names):
        path = dirname.split('/')

        if len(path) == 3:
            #print names
            for i in range(len(names)-1,0,-1):
                if names[i].startswith('.'):
                    del names[i]
            #print names
        else:
            lang = path[-1]
            #print arg, dirname, names
            names = [name for name in names if not name.startswith('.')]
            for name in names:
                filename = dirname + '/' + name
                #print 'filename:', filename
                fd = codecs.open(filename, encoding='utf-8')
                #fd = open(filename,'r')
                lines = fd.read()
                #for line in fd.readlines():
                for line in lines.split('\n'):
                    res = self.langid.classify(line)
                    #print lang, ':', res
                    if lang == res[0]:
                        self.a.update(correct=True)
                    else:
                        print 'incorrect:', lang, res, line
                        self.a.update(correct=False)
                fd.close()

    def start(self):
        os.path.walk(self.root, self.visit, '')    

class Accuracy:

    def __init__(self):
        self.correct = 0
        self.incorrect = 0

    def update(self, correct=True):
        if correct:
            self.correct += 1
        else:
            self.incorrect += 1
        #print 'updates', self.correct, self.incorrect

    def evaluate(self):
        total_cases = self.correct + self.incorrect
        accuracy = self.correct * 100.0 / total_cases
        print 'Accuracy = %f %% (%d of %d test cases)' % (accuracy, self.correct, total_cases)

