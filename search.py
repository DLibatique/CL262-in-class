# -*- coding: utf-8 -*-

#from cltk.tokenize.word import WordTokenizer
from cltk.tokenize.sentence import TokenizeSentence
import re

#word_tokenizer = WordTokenizer('greek')
tokenizer = TokenizeSentence('greek')

infile = open('files/plain_text/1-30_1.101-162.txt')
text = infile.read()
infile.close()
'''
for word in word_tokenizer.tokenize(text):
	if word.endswith('εαι'):
		print(word)
'''
for sent in tokenizer.tokenize_sentences(text):
	if re.search('εαι',sent):
		print(sent)