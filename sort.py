import csv
from email import header
data=[]
with open("dataset_2.csv") as f :
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planetdata=data[1:]
for data in planetdata :
    data[2]=data[2].lower()
planetdata.sort(key=lambda planetdata:planetdata[2])
with open("dataset_2_new.csv","a+") as f :
    csvwriter=csv.writer(f)
    csvwriter.writerows(headers)
    csvwriter.writerows(planetdata)