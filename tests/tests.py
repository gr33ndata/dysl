#!/usr/bin/env python

import os
import sys
import unittest

tests_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(tests_path + '/../')

from dysl.corpora.corpuslib.train import Train
from dysl.langid import LangID
from dysl.social import SocialLM

 
class TestLangID(unittest.TestCase):

    def setUp(self):
        self.lm1 = LangID(unk=False)
        self.lm2 = LangID(unk=True)
        self.lm1.train()
        self.lm2.train()

    def test_lang_set(self):
        lang_set = self.lm1.get_lang_set()
        lang_set.sort()
        expected_lang_set = ['en','es','ar','pt']
        expected_lang_set.sort()       
        self.assertEqual(lang_set,expected_lang_set)

    def test_classify_en(self):
        lang = self.lm1.classify(u'hello world')
        self.assertEqual(lang,'en')

    def test_classify_es(self):
        lang = self.lm1.classify(u'hola mis amigos')
        self.assertEqual(lang,'es')

    def test_classify_unk(self):
        lang1 = self.lm1.classify(u'this is la fiesta del mundo')
        self.assertEqual(lang1,'en')
        lang2 = self.lm2.classify(u'this is la fiesta del mundo')
        self.assertEqual(lang2,'unk')

class TestSocialLM(unittest.TestCase):

    def setUp(self):
        self.lm = SocialLM()

    def test_is_mention_at(self):
        ism = SocialLM.is_mention_line('@gr33ndata')
        self.assertEqual(ism,True)

    def test_is_mention_http(self):
        ism = SocialLM.is_mention_line('http://www.yahoo.com')
        self.assertEqual(ism,True)

    def test_is_mention_https(self):
        ism = SocialLM.is_mention_line('https://www.yahoo.com')
        self.assertEqual(ism,True)

    def test_is_not_mention(self):
        ism = SocialLM.is_mention_line('This is https://www.yahoo.com')
        self.assertEqual(ism,False)

    def test_normalize(self):
        norm_txt = self.lm.normalize(u'Dear @user How Are You?')
        self.assertEqual(norm_txt, u'dear how are you?')

if __name__ == '__main__':
    unittest.main()
