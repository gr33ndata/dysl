import sys
import argparse
from dysl.langid import LangID

def main():

    l = LangID(unk=False)
    l.train()

    if len(sys.argv) > 1:
        text = u' '.join(sys.argv[1:])
    else:
        text = u'hello, world'

    lang = l.classify(text)
    print text, '[ Language:', lang, ']'
    

if __name__ == '__main__':
    main()