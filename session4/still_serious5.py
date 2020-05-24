prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in prices:
    if key in stock:
        print(key)
        print("price: ",prices[key])
        print("stock: ",stock[key])
        print()

total = 0
for key in prices:
    total += prices[key] * stock[key]
print("total:",total)