import csv

def write_freq(frequency, filename):
    """
    Write new words and their frequencies to a file.
    """        
    outfile = open(filename, 'w') #write to csv
    writer = csv.writer(outfile, lineterminator='\n', delimiter=';')
    writer.writerow(['Word', 'Frequency']) #csv format
    b=list(frequency.items())
    b.sort(key=lambda item: item[1])
    b.reverse()
    writtenwords=[] # separate words from frequencies
    numbers=[]
    for item in b:
        writer.writerow([item[0], str(item[1])])
        written=[item[0]]
        writtenwords.extend(written)
        number=[item[1]]
        numbers.extend(number)
    outfile.close()
    return numbers, writtenwords
