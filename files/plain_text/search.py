# -*- coding: utf-8 -*-

#from cltk.tokenize.word import WordTokenizer
from cltk.tokenize.sentence import TokenizeSentence
import re
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('/') if isfile(join('/', f))]

#word_tokenizer = WordTokenizer('greek')
tokenizer = TokenizeSentence('greek')

for file in onlyfiles:
    infile = open(file)
    text = infile.read()
    infile.close()

    for sent in tokenizer.tokenize_sentences(text):
        if re.search('παραδρ',sent):
            print(sent)