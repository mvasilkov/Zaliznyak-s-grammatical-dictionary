#Special rules for nouns, to avoid suggesting wrong lemmas. Nothing is done for other POS.
import pymorphy2

blacklist1 = ['ъб', 'ъв', 'ъг', 'ъд', 'ъж', 'ъз', 'ък', 'ъл', 'ъм', 'ън', 'ъп', 'ър', 'ъс', 'ът', 'ъф', 'ъх', 'ъц', 'ъч', 'ъш', 'ъщ', 'йй', 'ьь', 'ъъ', 'ыы', 'чя', 'чю', 'чй', 'щя', 'щю', 'щй', 'шя', 'шю', 'шй', 'жы', 'шы', 'аь', 'еь', 'ёь', 'иь', 'йь', 'оь', 'уь', 'ыь', 'эь', 'юь', 'яь', 'аъ', 'еъ', 'ёъ', 'иъ', 'йъ', 'оъ', 'уъ', 'ыъ', 'эъ', 'юъ', 'яъ']
blacklist2 = ['чьк', 'чьн', 'щьн'] # forbidden
blacklist3 = ['руметь'] 

base1 = ['ло','уа', 'ая', 'ши', 'ти', 'ни', 'ки', 'ко', 'ли', 'уи', 'до', 'аи', 'то'] # unchanged
base2 = ['алз','бва', 'йты','ике','нту','лди','лит', 'вра','афе', 'бле', 'яху','уке', 'дзе', 'ури', 'ава', 'чче','нте', 'нне', 'гие', 'уро', 'сут', 'оне', 'ино', 'йду', 'нью', 'ньо', 'ньи', 'ери', 'ску', 'дье']
base3 = ['иани','льди', 'льде', 'ейру', 'зема', 'хими', 'ками', 'кала', 'мари', 'осси', 'лари', 'тано', 'ризе', 'енте', 'енеи']
base4 = ['швили', 'льяри']

change1 = ['лл','рр', 'пп', 'тт', 'ер', 'ук', 'ун', 'юк', 'ан', 'ян', 'ия', 'ин'] # declines
change2 = ['вец','дюн', 'еув', 'инз', 'ейн', 'лис','лек','бен','нек','рок', 'ргл', 'бих','бус','айс','гас','таш', 'хэм', 'аал', 'дад', 'анд', 'лес', 'мар','ньш', 'рос','суф', 'вик', 'якс', 'веш','анц', 'янц', 'сон', 'сен', 'нен',  'ман', 'цак', 'инд', 'кин', 'чин', 'рем', 'рём', 'дин']
change3 = ['ерит', 'гард', 'иньш', 'скис', 'ллит', 'еней', 'рроз', 'манн', 'берг', 'вист', 'хайм',]


female1 = ['ская', 'ской', 'скую']
female2 = ['овой']
female3 = ['евой']
female4 = ['иной']

middlemale = ['а', 'у']
middlestr1 = ['ии', 'ию'] # for Данелия
middlestr2 = ['ией']

male = ['ов', 'ев', 'ин']
male1 = ['ский', 'ским', 'ском']
male2 = ['ского', 'скому']
male3 = ['е', 'ы']
male4 = ['ым', 'ом', 'ем', 'ой']

side1 = ['авы', 'аве', 'аву', 'фик', 'иол', 'риц', 'икк', 'ест', 'рех', 'тин']
side2 = ['авой']



sname = ['вич', 'вна']
sname1 = ['вн']

def lemmas_done(found, lemmatized):
    """
    Check predicted lemmas according to the rules.
    """
    morph = pymorphy2.MorphAnalyzer()

    fix = []
    fixednames = []
    doublefemale =[]

    for i in range(len(lemmatized)):
        p = morph.parse(found[i])[0]
        if p.tag.POS == 'NOUN':
            if (found[i].istitle()) and ((found[i][-2:] in base1) or (found[i][-2:] in male) or (found[i][-3:] in base2) or (found[i][-4:] in base3) or (found[i][-5:] in base4)):
                fixednames.append(found[i])
            elif (found[i].istitle()) and ((found[i][-2:] in change1) or (found[i][-3:] in change2) or (found[i][-4:] in change3)):
                fixednames.append(found[i])
            elif (found[i].istitle()) and (found[i][-4:] in female1):
                fixednames.append(found[i][:-2] + 'ая')
            elif (found[i].istitle()) and (found[i][-4:] in female2):
                fixednames.append(found[i][:-4] + 'ова')
            elif (found[i].istitle()) and (found[i][-4:] in female3):
                fixednames.append(found[i][:-4] + 'ева')
            elif (found[i].istitle()) and (found[i][-4:] in female4):
                fixednames.append(found[i][:-4] + 'ина')
            elif (found[i].istitle()) and (found[i][-4:] in male1):
                fixednames.append(found[i][:-2] + 'ий')
            elif (found[i].istitle()) and (found[i][-5:] in male2):
                fixednames.append(found[i][:-3] + 'ий')
            elif (found[i].istitle()) and (found[i][-1:] in male3) and (found[i][-3:-1] in male):
                fixednames.append(found[i][:-1])
            elif (found[i].istitle()) and (found[i][-2:] in male4) and (found[i][-4:-2] in male):
                fixednames.append(found[i][:-2])
            elif (found[i].istitle()) and (found[i][-1:] in middlemale) and (found[i][-3:-1] in male):
                fixednames.append(found[i][:-1])
                doublefemale.append(found[i][:-1] + 'а')
            elif (found[i].istitle()) and ((found[i][-1:] in male3) or (found[i][-1:] in middlemale)) and (found[i][-3:-1] in change1):
                fixednames.append(found[i][:-1])
            elif (found[i].istitle()) and ((found[i][-1:] in male3) or (found[i][-1:] in middlemale)) and (found[i][-4:-1] in change2):
                fixednames.append(found[i][:-1])
            elif (found[i].istitle()) and ((found[i][-1:] in male3) or (found[i][-1:] in middlemale)) and (found[i][-5:-1] in change3):
                fixednames.append(found[i][:-1])
            elif (found[i].istitle()) and (found[i][-2:] in male4) and (found[i][-4:-2] in change1):
                fixednames.append(found[i][:-2])
            elif (found[i].istitle()) and (found[i][-2:] in male4) and (found[i][-5:-2] in change2):
                fixednames.append(found[i][:-2])
            elif (found[i].istitle()) and (found[i][-2:] in male4) and (found[i][-6:-2] in change3):
                fixednames.append(found[i][:-2])
            elif (found[i].istitle()) and (found[i][-2:] in middlestr1):
                fixednames.append(found[i][:-1] + 'я')
            elif (found[i].istitle()) and (found[i][-3:] in middlestr2):
                fixednames.append(found[i][:-2] + 'я')
            elif (found[i].istitle()) and (found[i][-3:] in side1):
                fixednames.append(found[i][:-1] + 'а')
            elif (found[i].istitle()) and (found[i][-4:] in side2):
                fixednames.append(found[i][:-2] + 'а')
            elif (found[i].istitle()) and (found[i][-4:-1] in side1):
                fixednames.append(found[i][:-1] + 'а')
            elif (found[i].istitle()) and (found[i][-5:-2] in side1):
                fixednames.append(found[i][:-2] + 'а')
            elif (found[i].istitle()) and (found[i][-3:] in sname):
                fixednames.append(found[i])
            elif (found[i].istitle()) and (found[i][-4:-1] in sname) and ((found[i][-1:] in middlemale) or (found[i][-1:] in male3)):
                fixednames.append(found[i][:-1])
            elif (found[i].istitle()) and (found[i][-5:-2] in sname) and (found[i][-2:] in male4):
                fixednames.append(found[i][:-2])
            elif (found[i].istitle()) and (found[i][-3:-1] in sname1) and ((found[i][-1:] in middlemale) or (found[i][-1:] in male3)):
                fixednames.append(found[i][:-1] + 'а')
            elif (found[i].istitle()) and (found[i][-4:-2] in sname1) and (found[i][-2:] in male4):
                fixednames.append(found[i][:-2] + 'а')
            else:
                fixednames.append(lemmatized[i])
        else:
            fixednames.append(lemmatized[i])

    for i in range(len(fixednames)):
        if (fixednames[i][-2:] in blacklist1) or (fixednames[i][-3:] in blacklist2) or (fixednames[i][-6:] in blacklist3):
            fix.append(found[i])
        else:
            fix.append(fixednames[i])
        

    fix = fix + doublefemale
    newfreq = len(doublefemale)

    return fix, newfreq
        
