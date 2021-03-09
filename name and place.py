import csv
csv_col=['ID','name','place']
dict_data=[{'ID':1,'name':'Ebin','place':'thrikalathoor'},
           {'ID':2,'name':'Alan','place':'thrissur'},
           {'ID':3,'name':'Jerin','place':'nellad'},
           {'ID':4,'name':'Basil','place':'kothamangalam'},
           {'ID':5,'name':'Ajmal','place':'Adimali'},
           {'ID':6,'name':'murshid','place':'thrissur'},
           {'ID':7,'name':'Najmal','place':'Malapuram'},
           {'ID':8,'name':'Joseph','place':'kuttampuzha'},
           {'ID':9,'name':'mahendran','place':'Nellikuzhi'},
           {'ID':10,'name':'Ameeen','place':'Kannur'}]
try:
  with open("names.csv",'w')as file1:
    writer1=csv.DictWriter(file1,fieldnames=csv_col)
    writer1.writeheader()
    for data1 in dict_data:
      writer1.writerow(data1)
except IOError:
      print("I/O error")
data1=csv.DictReader(open("names.csv"))
print("csv file as a dictionary:\n")  
for row in data1:
    print(row)
