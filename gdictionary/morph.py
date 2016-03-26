import pymorphy2

def mrph(lemmas):
    """
    Guesses lemmas for unknown words, using pymorphy analyzer, returns list of lemmas.
    """
    morph = pymorphy2.MorphAnalyzer()
    lemma = []
    for elem in lemmas:
            tag_token = morph.parse(elem)[0].normal_form
            lem = [tag_token]
            lemma.extend(lem)
    return lemma
