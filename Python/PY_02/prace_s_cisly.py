# prace_s_cisly.py

cisla = input("Zadej cisla: ")
data = cisla.split(' ')
data = list(map(int, data))

suma = sum(data)
pocet = len(data)
prumer = suma / pocet

print('min:', min(data))
print('max:', max(data))
print('sum:', suma)
print('prumer:', prumer)
