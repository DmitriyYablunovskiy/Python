# test_vek.py

vek = input('Zadej svuj vek: ')
vek = int(vek)

if vek < 18:
    print("Jsi mladistvy")
elif vek == 18:
     print("Jsi cerstve dospely")
else:
    print("Jsi dospely")

print('Zadal jsi:', vek)
print(type(vek))




