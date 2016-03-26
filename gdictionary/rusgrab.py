import os
import re
from subprocess import call
import gdictionary.freq as fq
import gdictionary.write_freq as wfq
import gdictionary.morph as morph
import gdictionary.postprocessing as postp
import gdictionary.recalculation as calc
import gdictionary.targetdata as data
import gdictionary.ARFFconversion as conversion
import gdictionary.postARFF as postconversion
import gdictionary.predictor as pred
import gdictionary.getfinal as gf

word_restriction = 4
outfile_name = "rus_text.txt" # contents passed to mystem

def catch_rus(input):
        """
        Prepares data for analysis: tokenize and send to mystem for POS-tagging.
        Takes in a string, returns a list of unknown words
        """
        outfile = open(outfile_name, 'w', encoding = 'utf-8')
        tokenization(input, outfile)
        outfile.close()
        stemfile = stem(outfile_name)
        words = bastards()
        # if no new words, then signalize to do nothing
        if words == 0:
            return 0
        newwrd = kill_small(words, word_restriction)
        os.remove(outfile_name)
        os.remove(stemfile)
        return newwrd

def tokenization (text, outfile):
        """
        A simple tokenizer: looks for words, ignores everything else.
        """    
        tokens=text.split()
        stripped_tokens = [] # a list of data
        for token in tokens:
                token = token.replace('\ufeff', '')
                stripped_tokens.append(token.strip(":;,()\"'.?!«»—"))
        stripped = helper(stripped_tokens) # cleaned text
        lowercase = re.findall(r'\b[а-яё]{1,}?\b', stripped)
        capital = re.findall(r'\b[А-ЯЁ][а-яё]{1,}?\b', stripped)
        russian = lowercase + capital
        russian = helper(russian)
        outfile.write(russian)

def stem(outfile_name, stemfile='output.txt'):
        """
        Calls mystem for tagging, writes the output in a file.,
        """
        output = open (stemfile, 'w', encoding = 'utf-8')
        file = open(outfile_name,'r', encoding = 'utf-8')
        call(['mystem', '-n', '--eng-gr'], stdin=file, stdout=output)
        file.close()
        output.close()
        return stemfile


def bastards(stemfile= 'output.txt'):
        """
        Looks for unknown words in the mystem output file, returns a list of them.
        """
        text = open(stemfile, encoding = "utf-8")
        full_found = ''
        for line in text:
                found = re.findall('[А-Я|а-я]{1,}\{[а-я]{1,}\?', line) #bastrards
                found = helper(found)
                full_found = full_found + found
        clean = re.findall('[А-Я|а-я]{1,}\{', full_found) #clean bastards
        clean = helper(clean)
        words = re.findall('[А-Я|а-я]{1,}', clean) #clean data
        words.sort()
        if not words:
            return 0
        return words

def kill_small(words, word_restriction):
        """
        Removes too frequent words
        """
        newwrd=[]
        for word in words:
                if len(word) >= word_restriction:
                        newwrd.append(word)
        return newwrd

        
def finalize(data, finfile):
        """
        Gets frequencies for unknown words, and writes them to a specially designated file.
        """
        frequency = fq.freq(data)
        numbers, writtenwords = wfq.write_freq(frequency, finfile)
        return numbers, frequency, writtenwords

def helper(data):
        """
        Joins given data in a column
        """
        data = '\n'.join(data)
        return data
       
       
def main(input):
    """
    Main method of the script.
    Launches the whole pipeline: analyze the input, return the predicted tags where possible.
    Takes a text string as an input.
    """
    input = re.sub("^\s+", '', input)
    input = re.sub("\s+$", '', input)
    word = catch_rus(input)
    if word == 0:
        return ["Header\n", "No new words!"]
    numbers, frequency, writtenwords = finalize(word, 'frequency.csv')
    lemma = morph.mrph(writtenwords)
    target_lemmas, newfreq = postp.lemmas_done(writtenwords, lemma)
    writtenwords=calc.recalculate_me(target_lemmas, numbers, newfreq)

    toARFF_noun, finalLEM_noun, toARFF_verb, finalLEM_verb = data.targetdata(writtenwords)
    # if we can't analyze the input, we need to return some warning
    if finalLEM_noun == 0:
        return ["Header\n", "We can't analyze this!"]
    test_noun, test_verb = conversion.main(toARFF_noun, toARFF_verb)
    train_noun, train_verb = postconversion.final_arffs()

    index_noun, index_verb = pred.analyze(train_noun, test_noun, train_verb, test_verb)
    return gf.adding(finalLEM_noun, toARFF_noun, index_noun, finalLEM_verb, toARFF_verb, index_verb)

if __name__ == "rusgrab":
    result = main("Звендевели бряцколки")
    print(result)





        
