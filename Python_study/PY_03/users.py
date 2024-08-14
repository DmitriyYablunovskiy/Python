# users.py

import os

def get_user_data():
    username = input('zadejte username: ')
    password = input('zadejte heslo: ')
    return [username, password]

def get_user_filename(username):
    filename = username + '.txt'
    filename = os.path.join(user_folder, filename)
    return filename

def do_user_exists(filename):
    return os.path.isfile(filename)

def login():
    pass

def registr():
    pass


user_folder = '/Users/dmitriy/Documents/itstep/Python/PY_03/users'

volba = input('Pro prihlaseni zadejte 1, pro registraci zadejte 2: ')

if volba == '1':
    print('chcete se prihlasit')

    username, password = get_user_data()
    filename = get_user_filename(username)
    user_exists = do_user_exists(filename)

    success = False


    if user_exists:
        with open(filename) as file:
            content = file.read()

            if content == password:
                success = True
    if success:
        print('uspesne prihlaseni')
    else:
        print('prihlaseni se nepodarilo')

elif volba == '2':
    print('chces se registrovat')
    
    username, password = get_user_data()
    filename = get_user_filename(username)
    user_exists = do_user_exists(filename)

    if user_exists:
        print("zvolte prosim jiny username")
    else:
        with open(filename, mode='w') as file:
            file.write(password)
            print("registrace uspesna")

else: 
    print('NEPLATNA VOLBA')


