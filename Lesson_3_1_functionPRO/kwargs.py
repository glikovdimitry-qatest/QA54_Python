def print_configuration(**kwargs):
    print(type(kwargs),kwargs)


print_configuration(browser="safari",headless=True,timeout=10)
print_configuration()

def create_user3(**data):
    return data

user = create_user3(name="Kristina",role="student")
print(user)

# user=create_user3("name": "Kris")
def for_example(a,b=15,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

for_example(2,3,4,5,name="Alex")