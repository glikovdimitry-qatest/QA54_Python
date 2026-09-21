from audioop import reverse

from Lessib1_remember.HW_1 import result

fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(len(fruits))
fruits[1] = "cat"
print(fruits)


#adding methods - append(), insert(), extend()
print("adding methods")
fruits.append("kiwi")
print(fruits)
#fruits.append(["car", "truck"])
#print(fruits)

fruits.extend(["cat", "dog"])
print(fruits)

fruits.insert(4 ,"pear")
print(fruits)

print()

#removing methods - remove(), pop(), del, clear()
print("removing methods")
e = ["apple", "banana", "orange"]
e.remove("banana")
print(e)
print()

f = ["apple", "banana", "orange"]
popped = f.pop(1)
print(popped, f)
print()

h = ["apple", "banana", "orange"]
del h[0]
print(h)
print()

k = ["apple", "banana", "orange"]
k.clear()
print(k)

print()

#search and count methods - index(), count(), in, not in
print("search and count methods")
m = ["apple", "banana", "cherry", "orange"]
print(m.index("cherry")) #2
print(m.count("banana")) #1
print("apple"in m) #True
print("kiwi" not in m) #True

print()

#sorting methods - sort(), sorted(), reverse()
print("sorting methods")
numbers = [3,1,5,2,9,6]
result = numbers.sort()
print(numbers,result)

numbers_2 = [3,1,5,2,9,6]
new_list = sorted(numbers_2)
print(numbers_2,new_list)

numbers_3 = [3,1,5,2,9,6]
numbers_3.reverse()
print(numbers_3)
print()

numbers_4 = [3,1,5,2,9,6]
print(sorted(numbers_4, reverse=True))
print(numbers_4)

print()

#iterating method
print("iterating method")
items = ["apple", "banana", "orange"]

for item in items:
    print(item)

for i in range(len(items)):
    print(i,items[i])

print()

numbers_5 = [-2,3,-1,5,0,-9]
result = []
for n in numbers_5:
    if n >0:
        result.append(n)
print(result)


result2 = [n for n in numbers_5 if n>0]
print(result2)
