import sys
from argparse import ArgumentParser
from dysl.langid import LangID

def main():

    parser = ArgumentParser(description='Do you speak London? A library for Natural Language Identification.')
    parser.add_argument('--unk', choices=['y','n'], default='y', help='Input text to classify')
    parser.add_argument('input', nargs='*', help='Input text to classify')
    args = parser.parse_args()
    #print args

    unk = False if args.unk == 'n' else True
    l = LangID(unk=unk)
    l.train()

    if len(args.input):
        text = u' '.join(args.input)
    else:
        parser.print_help()
        sys.exit('\nPlease input some text to classify')

    lang = l.classify(text)
    print 'Input text:', text
    print 'Language:', lang
    

if __name__ == '__main__':
    main()