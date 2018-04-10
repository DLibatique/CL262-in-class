'''
Written by Daniel Libatique (@DLibatique10).
A module to prepare text files for projection onto a blackboard/whiteboard.
'''

import re
from cltk.tokenize.line import LineTokenizer
TOKENIZER = LineTokenizer('latin')

def clean_benner(file):
    '''prepare cleaned Benner OCR text for
    projector display (Greek only)'''

    #get text
    infile = open(file, 'r')
    text = infile.read()
    infile.close()

    #tokenize into lines
    text = TOKENIZER.tokenize(text)

    #remove lines with Roman characters
    display_text = [line.replace(line, '') if re.search(r'[a-zA-Z]', line) else line for line in text]

    final_text = '\n\n\n\n'.join(display_text)
    while '\n\n\n\n\n\n' in final_text:
        final_text = final_text.replace('\n\n\n\n\n\n', '\n\n\n\n')

    return final_text

def write_to_projector(old_file, new_file='projector.txt'):
    '''
    overwrite projector file with new cleaned up text
    '''

    #erase contents of projector file, start fresh
    open(new_file, 'w').close()

    #prep new text to write to file
    display = clean_benner(old_file)

    #write new text to file
    outfile = open(new_file, 'w')
    outfile.write(display)
    outfile.close()

write_to_projector('files/plain_text/4-10_22.168-237.txt')
