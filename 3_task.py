import csv

with open("students.csv", "r", encoding = "utf-8") as f:
    data = list(csv.DictReader(f, delimiter = ","))
#print(data)
num = input("Введите номер проекта ")
while num != "СТОП":
    for person in data:
        if person['titleProject_id'] == num:
            surname, name, middlename = person["Name"].split()
            print(f"Проект № {person['titleProject_id']} делал {name[0]}. {surname}, он(а) получил(а) оценку {person['score']}")
            break
    else: print("Ничего не найдено")    
    num = input("Введите номер поекта ")

