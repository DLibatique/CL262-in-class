def read(file):
    
    infile = open(file, 'r')
    text = infile.read()
    infile.close()

    return text

def rewrite(text,file):

    open(file, 'w').close()

    outfile = open(file, 'w')
    outfile.write(text)
    outfile.close()

rewrite(read('files/plain_text/3-15_6.305-368.txt'),'../dlibatique.github.io/files/plain_text/3-15_6.305-368.txt')