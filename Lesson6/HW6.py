#HomeWork 6
#1.

def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"

products = ["coffee", "tea", "milk"]
print(get_product(products, 0))
print(get_product(products, 7))
print()



#2.

def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"

settings = {"language": "English","theme": "dark"}

print(get_settings_value(settings, "theme"))
print(get_settings_value(settings, "font"))
print()



#3.

def calculate_total_price(price, quantity):
    try:
        converted_price = float(price)
        converted_quantity = float(quantity)
        result = converted_price * converted_quantity
        return result

    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"

print(calculate_total_price("12.5", "4"))
print(calculate_total_price("coffee", "4"))
print(calculate_total_price(None, 4))
print()



#4.

def read_temperature():
    try:
        user_input = input("Enter temperature: ")
        temperature = float(user_input)
        print("Temperature was entered successfully")
    except ValueError:
        print("Invalid temperature")
    finally:
        print("Program finished")

read_temperature()
print()



#5.

def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    elif discount > 100:
        raise ValueError("Discount cannot be greater than 100")
    return discount

try:
    validate_discount(15)
    validate_discount(-5)
except ValueError as e:
    print(e)

try:
    validate_discount(120)
except ValueError as e:
    print(e)