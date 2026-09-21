#HomeWork
#1.


def clean_cart(cart):
    while "sold out" in cart:
        cart.remove("sold out")
    return cart

print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
print()


#2.


def temperature_report(temperatures):
    new_temps = []
    for temp in temperatures:
        if temp > 25:
            new_temps.append(temp)
    return new_temps

print(temperature_report([21, 28, 19, 31, 25, 27]))
print()


#3.


def fix_balances(balances):
    for i in range(len(balances)):
        if balances[i] < 0:
            balances[i] = 0
    return balances

print(fix_balances([120, -30, 50, -5, 0, 200]))
print()


#4.


def unique_items(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print(unique_items(["red", "blue", "red", "green", "blue"]))
print()


#5.


def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(["cat", "elephant", "python", "coffee"]))