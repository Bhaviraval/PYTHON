import csv

with open("C:\\Users\\lab\\Desktop\\Book1.CSV","a",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Roll No","CP"])
    writer.writerow(["Bhavi","24bit003","25"])
