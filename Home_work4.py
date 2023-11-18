def create_user(users: list[dict]) -> None:
    name = input('enter your name: ')
    surname = input('enter your surname: ')
    address = input('enter your address: ')

    age = input('enter your age: ')
    while not age.isdigit():
        age = input('enter valid age: ')

    username = input('enter your username: ')
    while not is_valid_username(users, username):
        print('This username is already exists, enter another username')
        username = input('enter your username: ')

    password = input('enter your password: ')
    while len(password) < 9:
        print('enter valid password, length of a password must be greater than 8 symbols')
        password = input('enter password: ')

    user = {
        'name': name,
        'surname': surname,
        'address': address,
        'age': age,
        'username': username,
        'password': password
    }
    users.append(user)
    if user in users:
        print(f'{username} added to the list')
        return
    print('Something wrong, user not added to the list')
    return


def is_valid_username(users: list[dict], username) -> bool:
    for user in users:
        if user['username'] == username:
            return False
    return True


def print_users(users: list[dict]) -> None:
    if not users:
        print('users list is empty')
        return

    for user in users:
        print(
            f'name: {user["name"]}',
            f'surname: {user["surname"]}',
            f'address: {user["address"]}',
            f'age: {user["age"]}',
            f'username: {user["username"]}',
            sep=', '
        )


def delete_user(users: list[dict]) -> None:
    username = input('enter username: ')
    for user in users:
        if user['username'] == username:
            users.remove(user)
            print(f'{username} was removed from list')
            return
    print(f'{username} not found in list')


def authorization(users: list[dict]) -> None:
    username = input('enter username: ')
    for user in users:
        if user['username'] == username:
            password = input('enter your password: ')
            while user['password'] != password:
                password = input('wrong password, try again: ')
            print('you successfully logged in to the system')
            return
    print(f'{username} not found in list')


def is_valid_option(option: str) -> bool:
    if not option.isdigit():
        return False
    if option not in '12345':
        return False
    return True


users_list = []

while True:
    print(
        'Choose one option',
        '1. Create user',
        '2. Show list of users',
        '3. Delete user from list',
        '4. Authorization',
        '5. Exit',
        sep='\n'
    )
    option = input('enter option: ')
    while not is_valid_option(option):
        print('enter valid option, option must be digit in range from 1 to 5')
        option = input('enter option: ')

    if option == '1':
        create_user(users_list)
    elif option == '2':
        print_users(users_list)
    elif option == '3':
        delete_user(users_list)
    elif option == '4':
        authorization(users_list)
    elif option == '5':
        exit()
    else:
        print('Unexpected error, inform tech support')
    print()
