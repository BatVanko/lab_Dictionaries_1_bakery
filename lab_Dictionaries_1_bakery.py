products = input().split()
bakery = {}

for i in range(0, len(products), 2):
    product = products[i]
    quantity = int(products[i+1])

    bakery[product] = quantity

print(bakery)



