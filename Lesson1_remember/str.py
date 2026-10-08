s= "cat"
s.upper()
print(s)

s1 = 'Hello'
s2 = "Hello"
s3 = """Line one
Line two"""
print(s1,s2,s3,sep="\n")
#print(s1)
#print(s2)
#print(s3)

#len()
s = "Hello my group!"
print(len(s))
print(s[0])
print(s[4])
print(s[14])
print(s[-1])
#print(s[100])
print()

#len()1 2 3 4 5 6
s1 = "P y t h o n"
#ind  0 1 2 3 4 5 -> Index of last element = len()-1 or -1

#slicing -> my_string[start:end:step]
text ="automation"
      #0123456789

print(text[2:6])
print(text[:4]) #From start to ind 4 exclusive
print(text[4:])  #From 4 to end of string
print(text[:])
print(text[::2]) #Every 2 symbol
print(text[::-1]) #Reverse
print(text[5:100])
print()

name = "Maria"
last_name = "Ivanova"
age = 25
print(name + " " + last_name + " - " + str(age))
print(f"Hi my name is {name} and my last name is {last_name} and i'm {age}")
print()

#upper()/lower()
raw = "   Automation QA   "
print(raw.upper())
print(raw.lower())
#strip()
print(raw.strip().upper())
print()

#split()/join()
cvs_line = "Login:Cart,Checkout,Mama,Papa"
parts = cvs_line.split(",")
print(parts) #['Login:Cart', 'Checkout', 'Mama', 'Papa']
print(" - ".join(parts))
print()

#replace()
msg = "Test failed: element not found"
print(msg.replace("failed","passed"))
print()

#find() and index()
#find()-->-1 if substring is not found
#index()-->ValueError if substring is not found

s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
#print(s.index("xyz"))
print()

#count()
print(s.count("na"))