import csv
"""
Считываем данные из файла без первой строки в список data
"""
with open("students.csv", "r", encoding = "utf-8", newline = "") as f:
    data = list(csv.reader(f, delimiter = ","))[1:]# список строк без заголовка
    
"""
Определение оценки Хадарова Владимира
"""
for row in data:
    if "Хадаров Владимир" in row[1]:
        print(f"Ты получил {row[4]} за проект - {row[2]}")
        break
"""
Вычисление средней оценки по классам.
При вычислении учитываются только ученики, имеющие оценку
"""
count_class = {}
sum_class = {}
for row in data:
    if row[-2] in count_class:
        if row[-1] != "None":
            count_class[row[-2]] += 1
            sum_class[row[-2]] += int(row[-1])
    else:
        if row[-1] != "None":
            count_class[row[-2]] = 1
            sum_class[row[-2]] = int(row[-1])       
"""
Замена "None" на средние оценки
"""
for row in data:
    if row[-1] == "None":
        row[-1] = round(sum_class[row[-2]] / count_class[row[-2]], 3)
"""
Печать данных в файл
"""
with open("students_new.csv", "w", newline = "", encoding = "utf-8") as f2:
    writer = csv.writer(f2)
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(data)




































    
