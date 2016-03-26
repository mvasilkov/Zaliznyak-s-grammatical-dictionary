import csv
import pymorphy2

def targetdata(words):
    """
    Beginning of preparations the test set for analysis: creates stubs for arff files of lemmas and default tags
    for each POS considered.
    Returns names of files that will be used later and lists of lemmas.
    """
    toARFF_noun = 'targetdata.noun.csv'
    toARFF_verb = 'targetdata.verb.csv'
    outfile_noun = open(toARFF_noun, 'w', encoding = 'utf-8')
    outfile_verb = open(toARFF_verb, 'w', encoding = 'utf-8')
    writer_noun = csv.writer(outfile_noun, lineterminator='\n', delimiter=',')
    writer_verb = csv.writer(outfile_verb, lineterminator='\n', delimiter=',')
    writer_noun.writerow(['Word', 'Len', '2let', 'Gender', 'Class']) #csv format
    writer_verb.writerow(['Word', '5let', 'Class']) #csv format
    morph = pymorphy2.MorphAnalyzer()

    counter_noun = counter_verb = 1
    lemmaZZZ_noun = []
    lemmaZZZ_verb = []
    isNoun = isVerb = False

    for elem in words:
        word = elem.strip()
        p = morph.parse(word)[0]

        if p.tag.POS == 'VERB' or p.tag.POS == "INFN":
            isVerb = True

            word1 = str(counter_verb)
            lastlet = word[-5:]
            classify = '1а'

            writer_verb.writerow([word1, lastlet, classify])

            counter_verb += 1
            lemmaZZZ_verb.append(word)

        elif p.tag.POS == 'NOUN': # if it is a noun
            isNoun = True
            
            if p.tag.animacy == 'anim' and ('Ms-f' in p.tag) == True:
                gender = 'мо-жо'
            elif ('GNdr' in p.tag) == True and word.istitle() == True:
                if p.tag.gender == 'masc':
                    gender = 'мо'
                elif p.tag.gender == 'femn':
                    gender = 'жо'
                elif p.tag.gender == 'neut':
                    gender = 'со'
            elif p.tag.animacy == 'anim' and ('Ms-f' in p.tag) == False:
                if p.tag.gender == 'masc':
                    gender = 'мо'
                elif p.tag.gender == 'femn':
                    gender = 'жо'
                elif p.tag.gender == 'neut':
                    gender = 'со'
            else:
                if p.tag.gender == 'masc':
                    gender = 'м'
                elif p.tag.gender == 'femn':
                    gender = 'ж'
                elif p.tag.gender == 'neut':
                    gender = 'с'
                                    
            if len(word) > 2:
                lastlet = word[-2:]
            else:
                lastlet = word
            lgth = len(word)
            classify = '1а'
            word1 = str(counter_noun)
            writer_noun.writerow([word1, lgth, lastlet, gender, classify])
            counter_noun +=1
            lemmaZZZ_noun.append(word)

    outfile_noun.close()
    outfile_verb.close()

    if not isVerb and not isNoun: # if it is not a noun
            toARFF_noun = 0
            lemmaZZZ_noun = 0
    return toARFF_noun, lemmaZZZ_noun, toARFF_verb, lemmaZZZ_verb


            






