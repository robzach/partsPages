"""
Reading a csv and generating a folder of Jekyll-readable parts pages

the csv being read looks a bit like this:

num,binLocation,tags,name,brief,datasheetName,purchaseURL
0421,B4-R3-C3,"Electronics, Power","regulator, 5V step-up voltage regulator, NCP1402",,NCP1402-D.pdf,http://www.pololu.com/product/798


Robert Zacharias for IDeATe at Carnegie Mellon University

released to the public domain by the author

v. 0.1 7-17-17
    * starting to read tsv data in so it can be written out

v. 0.2 7-18-17
    * tsv is unnecssary; csv exported from Google Sheets can handle commas in fields
    (thanks to Garth Zeglin for pointing out what I should've known)
    
v. 0.3 8-8-17
    * changed field headings to match CSV appropriately
    * outputting markdown documents

"""

import csv
import os.path

with open('inventory.csv') as csvfile:
    rows = csv.reader(csvfile)
    headerRow = next(rows)
    print ('headerRow:\n', ','.join(headerRow))

    for row in rows:
        num = row[0]
        binLocation = row[1]
        tags = row[2]
        name = row[3]
        brief = row[4]
        datasheetName = row[5]
        purchaseURL = row[6]

        filename = num + '.md'
        f = open(filename, "w+")
        f.write(
"""---
layout: item
number: """ + num + """
title: """ + name + """
brief: """ + brief + """
datasheet: """ + datasheetName + """
purchaselink: """ + purchaseURL + """
---
""")
        f.close()
        print("just wrote " + filename)
    

        
##    for row in rows:
##        print(' | '.join(row))
        
