import csv
f=open("C:\\Users\\lab\\Desktop\\Book1.CSV","r")
reader=csv.DictReader(f)

for row in reader:
    print(row)

f.close()
