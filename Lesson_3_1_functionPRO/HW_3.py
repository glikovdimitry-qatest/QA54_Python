#HomeWork
#1.
def print_list_reverse(lst):
    if not isinstance(lst, list) or not lst:
        print("Wrong list")
    else:
        print(lst[::-1])

print_list_reverse([1, 2, 3, 4, 5])
print()


#2.
def is_valid_point(point):
    if point is None or point == ():
        return None

    if not isinstance(point, tuple) or len(point) != 2:
        return False

    for x in point:
        if type(x) not in (int, float):
            return False

    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
print()


#3.
def print_sublist_reverse(lst, start, finish):
    if not isinstance(lst, list) or not lst:
        print("Wrong args")
        return

    if type(start) is not int or type(finish) is not int:
        print("Wrong args")
        return

    if start < 0 or finish >= len(lst) or start > finish:
        print("Wrong args")
        return

    result = lst[:start] + lst[start:finish + 1][::-1] + lst[finish + 1:]
    print(result)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)
print()


#4.
def get_students_by_grade(students):
    if not isinstance(students, dict) or not students:
        return {}

    result = {}
    for student, grade in students.items():
        if grade not in result:
            result[grade] = []
        result[grade].append(student)

    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))