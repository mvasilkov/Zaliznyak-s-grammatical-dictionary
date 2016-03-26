import csv, os

def adding(lemma_noun, file_noun, tags_noun, lemma_verb, file_verb, tags_verb):
    """
    Creates a file with final results: lemmas for unknown words and Zaliznyak's tags for them."""
    outfile = open('predicted.csv', 'w', encoding = 'utf-8')
    writer = csv.writer(outfile, lineterminator='\n', delimiter=',')
    writer.writerow(['Word', 'Class', 'Gender']) #csv format
    infile_noun = open(file_noun, 'r', encoding ='utf-8')

    gen =[]
    for line in infile_noun:
        elems = line.strip()
        elems = elems.split(',')
        gen.append(elems[3])
    gen.remove(gen[0])

    for i, elem in enumerate(lemma_noun):
        one = elem
        three = gen[i]
        two = tags_noun[i]
        writer.writerow([one, two, three])
    
    infile_noun.close()
    os.remove(file_noun)
    
    ##########################
    ##########################
    
    infile_verb = open(file_verb, 'r', encoding ='utf-8')

    for i, elem in enumerate(lemma_verb):
        one = elem
        two = tags_verb[i]
        three = "-"
        writer.writerow([one, two, three])

    infile_verb.close()
    os.remove(file_verb)
    outfile.close()

    return open('predicted.csv', encoding = 'utf-8').readlines()




            






