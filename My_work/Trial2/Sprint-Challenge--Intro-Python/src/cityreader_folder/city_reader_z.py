# importing csv module
import csv

# csv file name
cvsfile = "cities.csv"

import csv
with open('cities.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))
