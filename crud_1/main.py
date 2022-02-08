from crud_1.create_1 import create_user
from crud_1.read_1 import user_info, all_users_info


user_emails =[]
user_storage = {}
users_storage = {}


while True:

    action = input('Please, enter create or read_all, or read_user, or update, or delete: ')

    if action == 'create':
        print('action = ', action)

        email = input('Email: ')
        name = input('Name: ')
        password = input('Password: ')
        phone = input('Phone: ')

        create_user(email,
                    name,
                    password,
                    phone,
                    user_emails,
                    users_storage)
        print('user_emails = ', user_emails)
        print('users_storage = ', users_storage)

    elif action == 'read_all':
        print('action = ', action)
        all_users_info(users_storage)

    elif action == 'read_user':

        user_e = input('Enter user email:')
        message = user_info(user_e, user_emails, users_storage)

        print('action = ', action)
        print('User = ', message)

    elif action == 'update':
        print('action = ', action)

    elif action == 'delete':
        print('action = ', action)

    else:
        print('Please, re-enter: ')
