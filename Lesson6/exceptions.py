import json

from Lesson_3_dict.dict import value

#with open("user.json","r",encoding="utf-8") as file:
    #print(file.read())

# print("Hello world")
# result = 10/0
# print(result)
# print("bye world")

# def div_int(a,b):
#     return a/b
# print("Start program")
# result = div_int(10,0)
# print(result)
# print("End program")

#try/except
print("Hello World")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occured: e")

# print("BY")

try:
    number = int(input("Enter a number: "))
    result = 100/number
    print("Result: ",result)
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Number must be higher than 0")



def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Dem"))
print(is_number(None))

print()

try:
    value = int("39")
except ValueError:
    print("An error occurred: ")
else:
    print("An error occurred: ", value)
finally:
    print("End of try")