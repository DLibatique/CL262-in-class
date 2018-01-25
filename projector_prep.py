import re
from cltk.tokenize.line import LineTokenizer
tokenizer = LineTokenizer('latin')

def clean_benner(file):
    '''prepare cleaned Benner OCR text for
    projector display (Greek only)'''

    #get text
    infile = open(file, 'r')
    text = infile.read()
    infile.close()

    #tokenize into lines
    text = tokenizer.tokenize(text)

    #create display text
    display_text = []
    for line in text:
        #remove all English and notes
        if re.search(r'[a-zA-Z]', line):
            display_text.append(line.replace(line, ''))
        else:
            display_text.append(line)

    final_text = '\n\n\n\n'.join(display_text)
    while '\n\n\n\n\n\n' in final_text:
        final_text = final_text.replace('\n\n\n\n\n\n', '\n\n\n\n')

    return final_text

def write_to_projector(old_file, new_file='projector.txt'):

    #erase contents of projector file, start fresh
    open(new_file, 'w').close()

    #prep new text to write to file
    display = clean_benner(old_file)

    #write new text to file
    outfile = open(new_file, 'w')
    outfile.write(display)
    outfile.close()