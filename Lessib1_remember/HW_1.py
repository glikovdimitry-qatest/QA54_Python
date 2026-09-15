#HomeWork
#1.
from operator import truediv


def clean_name(name):
    return name.strip().title()

print(clean_name("   anna smith   "))
print(clean_name("DAVID COHEN"))
print()


#2.
def normalize_email(email):
    return email.strip().lower()

print(normalize_email("  Anna.Smith@Example.COM  "))
print()


#3.
def is_python_file(filename):
    return filename.strip().lower().endswith(".py")

print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("notes.txt"))
print()


#4.
def fix_message(message):
    return message.replace("bad","good")

message = "bad weather, bad mood"
result = fix_message(message)
print(result)
print(message)
print()


#5.
def count_letter(text, letter):
    return text.strip().lower().count(letter.strip().lower())

print(count_letter("Programming", "g"))
print(count_letter("Mississippi", "I"))
print()


#6.
def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    return first_name + "." + last_name

print(create_login("  Anna ", " SMITH  "))
print()


#B1.
def split_name(full_name):
    return full_name.strip().split()

print(split_name("  Anna   Smith  "))
print()


#b2.
def check_password(password):
#1.Checks that the password is at least 8 characters long.
    if len(password) < 8:
        return False
#2.Checks that the password contains no spaces.
    for char in password:
        if char.isspace():
            return False
#3.Check that the password consists not only of letters.
    if password.isalpha():
        return False

    return True

print(check_password("python123"))
print(check_password("python"))
print(check_password("python 123"))


