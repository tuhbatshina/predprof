from random import choice
import csv
from string import ascii_lowercase, ascii_uppercase

def create_login(s):
    """
    Функция создает логин ученика по строке из поля "Name"
    s - строка 
    """
    names = s.split()
    s1 = names[0] + "_" + names[1][0] + names[2][0]
    return s1

def create_password():
    """
    Функия генерирует пароли из 8 символов.
    Генерирование продолжается до тех пор,пока пароль не будет удовлетворять требованиям
    """
    s = "0123456789" + ascii_lowercase + ascii_uppercase
    password = "".join(choice(s) for i in range(8))
    while password.isdigit() or password.isalpha() or password.lower() == password \
          or password.upper() == password:
        password = "".join(choice(s) for i in range(8))
    return password

with open("students.csv", encoding = "utf-8") as f1:
    data = list(csv.reader(f1, delimiter = ","))[1:]

for  i in range(len(data)):
    new_login = create_login(data[i][1])
    key = create_password()
    data[i] = data[i] + [new_login, key]

#print(person)

with open("students_password.csv", "w", newline = "", encoding = "utf-8") as f2:
    writer = csv.writer(f2)
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    writer.writerows(data)
        
