import arff
import os
    
def final_arffs():
    """
    Makes final ARFF for weka, by combining features from train and test sets.
    """

    arfftarget_noun = 'targetdata.noun.csv.arff'
    arffmain_noun = 'trainingnumbers.noun.arff'

    arfffirst_noun = arff.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", arffmain_noun), encoding = 'utf-8'))
    arffsecond_noun = arff.load(open(arfftarget_noun, encoding = 'utf-8'))

    if arffsecond_noun['attributes'][2][1]:
        generallist_noun = []
        generallist_noun.extend(arfffirst_noun['attributes'][2][1])
        generallist_noun.extend(arffsecond_noun['attributes'][2][1])
        generallist_noun = list(set(generallist_noun))
        arfffirst_noun['attributes'][2][1].clear()
        arfffirst_noun['attributes'][2][1].extend(generallist_noun)
        arffsecond_noun['attributes'][2][1].clear()
        arffsecond_noun['attributes'][2][1].extend(generallist_noun)

        new_arffmain_noun = arff.dumps(arfffirst_noun)
        new_main_noun = open('new'+arffmain_noun, 'w', encoding = 'utf-8')
        new_main_noun.write(new_arffmain_noun)
        new_main_noun.close()

        new_arfftarget_noun = arff.dumps(arffsecond_noun)
        new_target_noun = open(arfftarget_noun, 'w', encoding = 'utf-8')
        new_target_noun.write(new_arfftarget_noun)
        new_target_noun.close()
    
    ###########################################
    ###########################################
    
    arfftarget_verb = 'targetdata.verb.csv.arff'
    arffmain_verb = 'trainingnumbers.verb.arff'

    arfffirst_verb = arff.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", arffmain_verb), encoding = 'utf-8'))
    arffsecond_verb = arff.load(open(arfftarget_verb, encoding = 'utf-8'))

    if arffsecond_verb['attributes'][1][1]:
        generallist_verb = []
        generallist_verb.extend(arfffirst_verb['attributes'][1][1])
        generallist_verb.extend(arffsecond_verb['attributes'][1][1])
        generallist_verb = list(set(generallist_verb))
        arfffirst_verb['attributes'][1][1].clear()
        arfffirst_verb['attributes'][1][1].extend(generallist_verb)
        arffsecond_verb['attributes'][1][1].clear()
        arffsecond_verb['attributes'][1][1].extend(generallist_verb)

        new_arffmain_verb = arff.dumps(arfffirst_verb)
        new_main_verb = open('new'+arffmain_verb, 'w', encoding = 'utf-8')
        new_main_verb.write(new_arffmain_verb)
        new_main_verb.close()

        new_arfftarget_verb = arff.dumps(arffsecond_verb)
        new_target_verb = open(arfftarget_verb, 'w', encoding = 'utf-8')
        new_target_verb.write(new_arfftarget_verb)
        new_target_verb.close()

    if arffsecond_noun['attributes'][2][1]:
        if arffsecond_verb['attributes'][1][1]:
            return new_main_noun.name, new_main_verb.name
        else:
            return new_main_noun.name, 0
    else:
        return 0, new_main_verb.name






    
