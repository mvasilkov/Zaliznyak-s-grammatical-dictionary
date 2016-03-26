import csv
import re

def main(toARFF_noun, toARFF_verb):
    """
    Create proper ARFF files from csv's, created in the pipeline"""
    content_noun= csvparse(toARFF_noun)
    content_verb = csvparse(toARFF_verb)
    title_noun, title_verb = arffOutput(content_noun, content_verb, toARFF_noun, toARFF_verb)
    return title_noun, title_verb



def csvparse(toARFF):
    """import CSV
    """
    content = []
    with open(toARFF, 'r', encoding ='utf-8') as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in lines:
           content.append(row)

    return content


def arffOutput(content_noun, content_verb, toARFF_noun, toARFF_verb):
    '''export ARFF
    '''
    title_noun = toARFF_noun + '.arff'
    arff_file_noun = open(title_noun, 'w', encoding = 'utf-8')

    #write relation
    arff_file_noun.write('@relation ' + str(''.join(re.findall('^[a-z]{1,}', title_noun))) + '\n\n')

    #write attribute
    arff_file_noun.write('@attribute Word numeric' + '\n')
    arff_file_noun.write('@attribute Len numeric' + '\n')
    all_items_noun = collecting_items(2, content_noun)
    string_noun = '{' + ','.join(sorted(all_items_noun)) + '}'
    arff_file_noun.write('@attribute 2let ' + string_noun + '\n')
    arff_file_noun.write('@attribute Gender {ж,с,мо,м,жо,мо-жо,со}' + '\n')
    arff_file_noun.write('@attribute Class {4а,1с,8а,1а,3*а,3а,2а,5а,7а}' + '\n')

    #write data
    arff_file_noun.write('\n@data\n')
    del content_noun[0]
    for item in content_noun:
        arff_file_noun.write(','.join(item) + '\n')

    #close file
    arff_file_noun.close()

    ##################################
    ##################################

    title_verb = toARFF_verb + '.arff'
    arff_file_verb = open(title_verb, 'w', encoding = 'utf-8')

    #write relation
    arff_file_verb.write('@relation ' + str(''.join(re.findall('^[a-z]{1,}', title_verb))) + '\n\n')

    #write attribute
    arff_file_verb.write('@attribute Word numeric' + '\n')
    all_items_verb = collecting_items(1, content_verb)
    string_verb = '{' + ','.join(sorted(all_items_verb)) + '}'
    arff_file_verb.write('@attribute 5let ' + string_verb + '\n')
    arff_file_verb.write('@attribute Class {2а, 1а, 6а}' + '\n')

    #write data
    arff_file_verb.write('\n@data\n')
    del content_verb[0]
    for item in content_verb:
        arff_file_verb.write(','.join(item) + '\n')

    #close file
    arff_file_verb.close()
    return title_noun, title_verb

def collecting_items(item, content):
    all_items = []
    for elem in content:
        if elem[item] not in all_items:
            all_items.append(elem[item])
    del all_items[0]
    return all_items
