# Напишите
# функцию
# save_shopping_list(items).
# Функция
# принимает
# список
# строк
# и
# создаёт
# файл
# shopping.txt
# и
# сохраняет
# в
# него
# список
# покупок.
#
# Каждый
# товар
# должен
# быть
# записан
# с
# новой
# строки.
#
# Пример:
#
# items = [
#     "Milk",
#     "Bread",
#     "Apples",
#     "Coffee"
# ]
#
# save_shopping_list(items)
#
# После
# выполнения
# программы
# файл
# должен
# выглядеть
# так:
#
# Milk
# Bread
# Apples
# Coffee
#
# Используйте:
#
# • with open(...)
#
# • режим
# "w"
#
# • цикл
# for
import csv
from pathlib import Path
from idlelib.pathbrowser import PathBrowser


def save_shopping_list(items):
    with open("shopping_list.txt","a",encoding="utf-8") as file:
        for item in items:
            file.write(item+"\n")
items = ["Milk","Bread","Apples","Coffee"]
save_shopping_list(items)

with open("shopping_list.txt","r",encoding="utf-8") as file:
    print(file.read())


#----------------------------------------------------------------
#Read data from a CSV file
#
# Создайте файл students.csv со следующим содержимым:
#
# name,age
# Anna,21
# Tom,19
# Kate,22
#
# Напишите функцию read_students(filename)
# которая выводит информацию в виде
#
# Student: Anna (21)
# Student: Tom (19)
# Student: Kate (22)
#
# Use csv.DictReader().

def read_students(filename):
    with open(filename,"r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']}({row['age']})")
read_students("students.csv")


#----------------------------------------------------------------------
# Save a profile to a JSON file
#
# Напишите функцию save_profile(name, age, city)
# Функция должна создать файл profile.json со следующим содержимым:
#
# save_profile("Maria", 30, "Haifa")
#
# Ожидаемое содержимое файла profile.json:
#
# {
#     "name": "Maria",
#     "age": 30,
#     "city": "Haifa"
# }
#
# Use a dictionary and json.dump().


def create_reports_folder():
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    results_file = reports_dir/"result.txt"
    with open(results_file,"w",encoding="utf-8") as file:
        file.write("Homework completed successfully!")
create_reports_folder()