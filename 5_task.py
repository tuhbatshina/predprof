import csv

def hash_create(s, d):
    """
    Вычисление значения хеш-функции
    s - строка из поля "Name"
    d - словарь соответствия символ алфавита: номер номер символа (с 1)
    """
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value

"""
Создание словаря
"""
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
d = {}
for i in range(len(alph)):
    d[alph[i]] = i+1

with open("students.csv", encoding = "utf-8") as f:
    data = list(csv.reader(f, delimiter = ","))[1:]
"""
Замена элемента "id" на значение хеш-функции
"""
for i in range(len(data)):
    data[i][0] = hash_create(data[i][1], d)

with open("students_with_hash.csv", "w", newline = "", encoding = "utf-8") as f2:
    writer = csv.writer(f2)
    writer.writerow(["id", "Name", "titleProject_id", "class", "score"])
    writer.writerows(data)
    



































        
