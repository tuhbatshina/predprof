import csv
##with open("students.csv", "r", encoding = "utf-8", newline = "") as f:
##    reader = csv.DictReader(f, delimiter = ",")
##    for line in reader:
##        print(line)

with open("students.csv", "r", encoding = "utf-8", newline = "") as f:
    reader = csv.reader(f, delimiter = ",")
##    for line in reader:
##        print(line)
    rows = list(reader)[1:]
for pers_id, name, project_id, level, score in rows:
    if "Хадаров Владимир" in name:
        print(f"Ты получил {score}, за проект - {project_id}")
        break
count_class = {}
sum_class = {}
for x in rows:
    count_class[x[-2]] = count_class.get(x[-2], 0) + 1
    sum_class[x[-2]] = sum_class.get(x[-2], 0) + (int(x[-1]) if x[-1] != "None" else 0)
for x in rows:
    if x[-1] == "None":
        x[-1] = round(sum_class[x[-2]] / count_class[x[-2]], 3)
                
with open("students_new.csv", "w", newline = "", encoding = "utf-8") as f2:
    writer = csv.writer(f2)
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(rows)




































    
