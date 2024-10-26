with open("med.csv", "r",encoding='utf-8') as file:
    text = file.read()

a = []
for i in text.split("\n"):
    a.append(i.replace("\xa0", "").replace("₹", "").strip(",").split(","))
print(a)
