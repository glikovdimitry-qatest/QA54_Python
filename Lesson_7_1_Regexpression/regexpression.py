import re

text = "The status is passed"
result = re.search("passed",text)
print(result)
print(result.group())

text2 = "passed: test registration"
text3 = "test registration: passed"
print(re.match("passed",text2))
print(re.match("passed",text3))

print(re.match("Passed: test registration",text2))
print(re.match("Passed: test registration ",text2))

print()

print(re.search("d.g","dog"))
print(re.search("d.g","dig"))
print(re.search("d.g","dg"))
print(re.search("d..g","doog"))

print(re.search("^Test","Test is start"))
print(re.search("^Test","Start is test"))

print(re.search("Test$","Start is Test"))
print(re.search("Test$","Test Start is"))

print()

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","green"))

print(re.search("[a-z]","Dimitry"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","kristina"))
print(re.search("[A-Za-z]","kristina"))

print()

print(re.search("[^0-9]","123456a"))
print(re.search("[^0-9]","123456"))
