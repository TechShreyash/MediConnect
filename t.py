# with open("med.csv", "r",encoding='utf-8') as file:
#     text = file.read()

# a = []
# for i in text.split("\n"):
#     a.append(i.replace("\xa0", "").replace("₹", "").strip(",").split(","))
# print(a)


#read data/shops.csv file
import csv

def read_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row)
    return data

# print all items of all lines
data = read_csv('data/med.csv')
print(data)