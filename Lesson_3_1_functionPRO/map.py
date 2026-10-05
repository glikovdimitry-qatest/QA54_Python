numbers = [1,2,3,4,5,6]

squ = map(lambda x:x**2, numbers)
print(squ)
print(list(squ))
print()

def to_upper(s):
    return s.upper()
status = ["passed","failed","skip"]
upper_status = list(map(to_upper,status))
print(upper_status)