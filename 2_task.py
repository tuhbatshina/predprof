import csv
"""
Чтение данных из файла в виде списка словарей
"""
with open("students.csv", "r", encoding = "utf-8", newline = "") as f:
    data = list(csv.DictReader(f, delimiter = ","))

for person in data:
    if person['score'] == "None":
        person['score'] = 0
    else: person['score'] = int(person['score'])    
"""
Сортировка вставками по полю "score"
"""

for i in range(1, len(data)):
    x = data[i]
    j = i
    while j > 0 and data[j-1]['score'] < x['score']:
        data[j] = data[j-1]
        j -= 1
    data[j] = x

print("10 класс")
count = 1
for person in data:
    if "10" in person['class']:
        surname, name, middlename = person["Name"].split()
        print(f"{count} место: {name[0]}. {surname}")
        count += 1
        if count > 3:
            break
    
