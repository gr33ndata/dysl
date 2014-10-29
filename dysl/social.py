import unicodedata
from dyslib.lm import LM

class SocialLM(LM):

    @classmethod
    def tokenize(self, text, mode='c'):
        """ Converts text into tokens

            :param text: string to be tokenized
            :param mode: split into chars (c) or words (w)
        """
        if mode == 'c':
            return [ch for ch in text]
        else:
            return [w for w in text.split()]

    def karbasa(self, result):
        probs = result['all_probs']
        probs.sort()
        return float(probs[1] - probs[0]) / float(probs[-1] - probs[0])

    def classify(self, text=u''):
        """ Predicts the Language of a given text.

            :param text: Unicode text to be classified.
        """
        result = self.calculate(doc_terms=self.tokenize(text))
        #return (result['calc_id'], result)
        return (result['calc_id'], self.karbasa(result))

    @classmethod
    def is_mention_line(self, word):
        """ Detects links and mentions
        """
        if word.startswith('@'):
            return True
        elif word.startswith('http://'):
            return True
        elif word.startswith('https://'):
            return True
        else:
            return False

    def strip_mentions_links(self, text):
        #print 'Before:', text
        new_text = [word for word in text.split() if not self.is_mention_line(word)]
        #print 'After:', u' '.join(new_text)
        return u' '.join(new_text)

    def normalize(self, text):
        #print 'Normalize...\n'
        text = text.lower()
        text = unicodedata.normalize('NFC', text)
        text = self.strip_mentions_links(text)
        return text