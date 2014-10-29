import sys
from argparse import ArgumentParser

from dysl.version import __version__
from dysl.utils import decode_input
from dysl.langid import LangID

def main():

    parser = ArgumentParser(description='Do you speak London? A library for Natural Language Identification.')
    parser.add_argument('--version', action='store_true', help='Show version')
    parser.add_argument('--list-langs', action='store_true', help='List supported languages in training data')
    parser.add_argument('--unk', choices=['y','n'], default='n', help='Input text to classify')
    parser.add_argument('--corpus', default='', help='Specify path to custom training-set')
    parser.add_argument('--lang', help='Add training sample for the language specified')
    parser.add_argument('input', nargs='*', help='Input text to classify')
    args = parser.parse_args()
    #print args

    unk = False if args.unk == 'n' else True

    input_text = decode_input(args.input)

    if args.version:
        sys.exit(__version__)
    elif args.list_langs:
        l = LangID(unk=unk)
        l.train(root=args.corpus)
        print 'Languages: [' + '-'.join(l.get_lang_set()) + ']'
        sys.exit()
    elif args.lang and input_text:
        l = LangID(unk=unk)
        l.train(root=args.corpus)
        l.add_training_sample(text=input_text, lang=args.lang)
        l.save_training_samples()
        sys.exit('Training Sample for "%s" added successfully.\n' % args.lang)
    elif input_text:
        l = LangID(unk=unk)
        l.train(root=args.corpus)
        lang = l.classify(input_text)
        print 'Input text:', input_text
        print 'Language:', lang
    else:
        parser.print_help()
        sys.exit('\n')

if __name__ == '__main__':

    try:
        main()
    except Exception, e:
        print "Failed to run!"
        print e
