def double(x):
    return x*2

double_lambda = lambda x:x*2
double_lambda2 = lambda x:x*2 if x>0 else -x

print(double(4))
print(double_lambda(4))
print(double_lambda2(-3))

print()

add = lambda x,y:x+y
print(add(3,4))

is_even = lambda p: p%2==0
print(is_even(8))
print(is_even(5))
print()

grades = [90,75,88,63,100,81]
even = list(filter(lambda x:x%2==0,grades))
odd = list(filter(lambda x:x%2!=0,grades))

print("Чётные оценки: ",even)
print("Не чётные оценки: ",odd)
print()