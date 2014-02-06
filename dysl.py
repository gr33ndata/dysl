import sys
import codecs

from dyslib.lm import LM

corpora = {
    'en': 'corpora/en.txt',
    'es': 'corpora/es.txt',
    'fr': 'corpora/fr.txt',
}

def term2ch(text):
    return [ch for ch in text]

# f = codecs.open('unicode.rst', encoding='utf-8')
# lm.add_doc(doc_id='apple', doc_terms=term2ch('the tree is full or apples'))

def readfile(filename):
    f = codecs.open(filename, encoding='utf-8')
    tokenz = term2ch(f.read())
    f.close()
    print tokenz
    return tokenz


def main():
    
    ngram = 2
    lrpad = ' '

    lm = LM(n=ngram, verbose=True, lpad=lrpad, rpad=lrpad, 
            smoothing='Laplace', laplace_gama=0.1, 
            corpus_mix='l')
    for lang in corpora:
        lm.add_doc(doc_id=lang, doc_terms=readfile(corpora[lang]))

    intxt = u' '
    for u in sys.argv[1:]:
        intxt = intxt + u' ' + u.decode('utf-8')
    print term2ch(intxt)
    result = lm.calculate(doc_terms=term2ch(intxt))
    print result

if __name__ == '__main__':
    main()