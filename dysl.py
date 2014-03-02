import sys
import codecs

from dyslib.lm import LM

corpora = {
    'English': 'corpora/en.txt',
    'Spanish': 'corpora/es.txt',
    'French': 'corpora/fr.txt',
    'Arabic': 'corpora/ar.txt',
    'Arabizi': 'corpora/ar-latin.txt',
}

def term2ch(text):
    return [ch for ch in text]

# f = codecs.open('unicode.rst', encoding='utf-8')
# lm.add_doc(doc_id='apple', doc_terms=term2ch('the tree is full or apples'))

def readfile(filename):
    f = codecs.open(filename, encoding='utf-8')
    tokenz = term2ch(f.read())
    f.close()
    #print tokenz
    return tokenz


def main():
    
    ngram = 3
    lrpad = u' '
    verbose=True

    lm = LM(n=ngram, verbose=verbose, lpad=lrpad, rpad=lrpad, 
            smoothing='Laplace', laplace_gama=0.1, 
            corpus_mix='l')
    for lang in corpora:
        print lang
        lm.add_doc(doc_id=lang, doc_terms=readfile(corpora[lang]))

    intxt = u''
    for u in sys.argv[1:]:
        intxt = intxt + u.decode('utf-8')
    
    print term2ch(intxt)
    result = lm.calculate(doc_terms=term2ch(intxt))
    print result['calc_id']

if __name__ == '__main__':
    main()