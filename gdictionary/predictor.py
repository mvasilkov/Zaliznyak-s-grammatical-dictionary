import shlex, subprocess, re, os

def analyze(train_noun, test_noun, train_verb, test_verb):
    """
    Launches Weka for each available test set, gets predicted tags for each"""
    if train_noun != 0:
        command_noun = 'java -Dfile.encoding=utf-8 -cp \
        weka.jar weka.classifiers.meta.FilteredClassifier \
        -F "weka.filters.unsupervised.attribute.Remove -R 1" \
        -W weka.classifiers.trees.J48 -t ' + train_noun + ' -T ' + test_noun + ' -classifications \
        weka.classifiers.evaluation.output.prediction.PlainText -- \
        -C 0.25 -M 2'
        args_noun = shlex.split(command_noun)
        out_noun = subprocess.check_output(args_noun)
        lines_noun = [re.sub("\s+", ' ', line).strip(" ") for line in out_noun.decode('utf8').split('\n')]

        pred_noun = [line.split(" ")[2] for line in lines_noun[5:-2]]
        pred_noun = [re.sub('[0-9][:]', '', elem) for elem in pred_noun]
        os.remove("newtrainingnumbers.noun.arff")
    else:
        pred_noun = 0
    #########################
    #########################

    if train_verb != 0:
        command_verb = 'java -Dfile.encoding=utf-8 -cp \
        weka.jar weka.classifiers.meta.FilteredClassifier \
        -F "weka.filters.unsupervised.attribute.Remove -R 1" \
        -W weka.classifiers.trees.J48 -t ' + train_verb + ' -T ' + test_verb + ' -classifications \
        weka.classifiers.evaluation.output.prediction.PlainText -- \
        -C 0.25 -M 2'
        args_verb = shlex.split(command_verb)
        out_verb = subprocess.check_output(args_verb)
        lines_verb = [re.sub("\s+", ' ', line).strip(" ") for line in out_verb.decode('utf8').split('\n')]

        pred_verb = [line.split(" ")[2] for line in lines_verb[5:-2]]
        pred_verb = [re.sub('[0-9][:]', '', elem) for elem in pred_verb]
        os.remove("newtrainingnumbers.verb.arff")
    else:
        pred_verb = 0

    os.remove(test_noun)
    os.remove(test_verb)
    return pred_noun, pred_verb