"""
Reading a tsv (tab-separated file) and generating a folder of Jekyll-readable
parts pages


the tsv being read looks a bit like this:

num    title    brief    date    datasheet    purchaselink
0001    resistor    these resist electrical flow    1-1-2000    datasheet.pdf    buythings.com

(first row is a header row; data is tab-delimited; newlines are new entries)


Robert Zacharias for IDeATe at Carnegie Mellon University

released to the public domain by the author

v. 0.1 7-17-17
    * starting to read tsv data in so it can be written out

"""

import csv
import os.path

with open('partslisttry.tsv') as tsvfile:
    rows = csv.reader(tsvfile, delimiter='\t', quotechar='|')
    headerRow = next(rows)
    print ("headerRow: ", ', '.join(headerRow))

    for row in rows:
        num = row[0]
        title = row[1]
        brief = row[2]
        date = row[3]
        datasheet = row[4]
        purchaselink = row[5]
        
##    for row in rows:
##        print(', '.join(row))

##    for row in rows:
##        print (', '.join(row))
##        fname = row[0] + '.jpg'
##        if os.path.isfile(fname):
##            print (fname + " found")
##            image = Image.open(fname)
####            image.show()
##        else:
##            print (fname + " not found")
