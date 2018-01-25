import re
from cltk.tokenize.line import LineTokenizer
tokenizer = LineTokenizer('latin')

#erase contents of projector file, start fresh
open('projector.txt', 'w').close()

def clean_benner(file):
    '''prepare cleaned Benner OCR text for
    projector display (Greek only)'''

    #get text
    infile = open(file, 'r')
    text = infile.read()
    infile.close()

    #tokenize into lines
    text = tokenizer.tokenize(text)

    #remove all English
    english_text = []
    for line in text:
        if line.startswith('//'):
            english_text.append(line.replace(line, ''))
        else:
            english_text.append(line)

    #remove notes
    numbers = '123456789'
    notes_text = []
    for line in english_text:
        if line.startswith(r'[0-9]'):
            print(line)
            notes_text.append(line.replace(line, ''))
        else:
            notes_text.append(line)

    final_text = '\n\n\n\n'.join(notes_text)
    final_text = final_text.replace('\n\n\n\n\n\n', '\n\n\n\n')

    return final_text

display = clean_benner('files/plain_text/1-30_1.101-162.txt')

outfile = open('projector.txt', 'w')
outfile.write(display)
outfile.close()