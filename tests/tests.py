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
        self.l = LangID(unk=False)
        self.l.train()

    def test_lang_set(self):
        lang_set = self.l.get_lang_set()
        lang_set.sort()
        expected_lang_set = ['en','es','ar','pt']
        expected_lang_set.sort()       
        self.assertEqual(lang_set,expected_lang_set)

    def test_classify_en(self):
        lang = self.l.classify(u'hello world')
        self.assertEqual(lang,'en')

    def test_classify_es(self):
        lang = self.l.classify(u'hola mis amigos')
        self.assertEqual(lang,'es')

             
if __name__ == '__main__':
    unittest.main()
