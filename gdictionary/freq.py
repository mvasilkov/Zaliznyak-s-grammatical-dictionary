def freq(elems):
    """
    Counts word frequencies
    """
    frequency = {} #collecting frequency
    for elem in elems:
            if elem not in frequency:
                    frequency[elem] = 1
            else:
                    frequency[elem] += 1

    return frequency
        

