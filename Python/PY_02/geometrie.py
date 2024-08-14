# geometrie.py

# vypočet obvodu trojuhelniku

hodnoty = input("Zadejte hodnoty trojuhelnika: ")
data = hodnoty.split(' ')

a, b, c = data

print(a + b + c)
print(int(a) + int(b) + int(c))
print(list(map(int, data)))


