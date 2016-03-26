import gdictionary.write_freq as wfq

def recalculate_me(finallemmas, freq_main, newfreq):
    """
    Recalculates frequencies from the existing file after predicting lemmas.
    """
    freq_addit = [1]*newfreq
    freq = freq_main + freq_addit 

    recalc = {}
    
    for i in range(len(finallemmas)):
        if not finallemmas[i] in recalc:
            recalc[finallemmas[i]] = freq[i]
        else:
            recalc[finallemmas[i]] += freq[i]
             
    numbers, writtenwords = wfq.write_freq(recalc, 'frequency.csv')
    return writtenwords

