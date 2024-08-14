# read_file.py


cesta = 'PY_02/test_file.txt'

with open(cesta) as file:
    print(file.read())



with open(cesta, mode = 'a') as file:
    file.write("\nHello from Python")