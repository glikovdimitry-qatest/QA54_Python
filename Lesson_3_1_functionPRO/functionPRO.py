def greet(name):
    return f"Hello,{name}!"

result = greet("Kris!")
print(result)

#result2 = greet()
#print(result2)

def create_user (name,role = "user"):
    return {"name": name, "role": role}

print(create_user("Alex"))
print(create_user("Kristina", "admin"))

print()
def cal_discount(price, discount=20):
    return price - (price * discount/100)

print(cal_discount(2000))
print(cal_discount(3000,25))

#def foo(a=1,b):
#    return a+b
#print(foo(5))

def add_tests(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results

print(add_tests("test_registration"))
print(add_tests("test_login"))


def create_user2(username, email, role):
    return f"{username} ({email}) - {role}"
print(create_user2("Kris","test@gm.com", "teamLead"))

print(create_user2(role="Project",username="Alex",email="Test2@gm.com"))

print(create_user2("Kristina",role="QA",email="qa@gm.com"))
