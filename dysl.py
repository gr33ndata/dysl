import sys
from argparse import ArgumentParser
from dysl.langid import LangID

def decode_input(text_in):
    return u' '.join(text_in)
    if type(text_in) == list:
        text_out = u' '.join([t.decode('utf-8') for t in text_in])
    else:
        text_out = text_in.decode('utf-8') 
    return text_out

def main():

    parser = ArgumentParser(description='Do you speak London? A library for Natural Language Identification.')
    parser.add_argument('--unk', choices=['y','n'], default='y', help='Input text to classify')
    parser.add_argument('--corpus', default='', help='Specify path to custom training-set')
    parser.add_argument('--lang', help='Add training sample for the language specified')
    parser.add_argument('input', nargs='*', help='Input text to classify')
    args = parser.parse_args()
    #print args

    unk = False if args.unk == 'n' else True
    l = LangID(unk=unk)
    l.train(root=args.corpus)

    input_text = decode_input(args.input)
    
    if args.lang and input_text:
        l.add_training_sample(text=input_text, lang=args.lang)
        l.save_training_samples()
        sys.exit('Training Sample for "%s" added successfully.\n' % args.lang)
    elif input_text:
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