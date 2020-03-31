import sys
import csv


file = "list.csv"
ports = list(sys.argv)
ports.pop(0)



ports = list(map(int, ports))
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = csvreader.next()

    for row in csvreader:
        try:
            # int(row[1])\
            testport = int(row[1])
            if(testport in  ports):
                print(str(testport) + "\t" + row[2] + '\t' + row[3] + " ("+row[3] + ")")

        except:
            pass