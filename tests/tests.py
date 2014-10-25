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

    def test_classify_en(self):
        lang = self.l.classify(u'hello world')
        self.assertEqual(lang,'en')

    def test_classify_es(self):
        lang = self.l.classify(u'hola mis amigos')
        self.assertEqual(lang,'es')

             
if __name__ == '__main__':
    unittest.main()
