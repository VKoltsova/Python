def user_info(email, users_emails, users_storage):

    if email in users_emails:
        massage = 'User_email=', email, '\n', 'User_info:', users_storage[email]
        return massage
    else:
        massage = 'No user with email:', email
        return massage

def all_users_info(users_storage):
    for k, v in users_storage.items():
        user_email = 'User_email' + k
        user_info_1 = 'User_info', v
        print(user_email, user_info_1)
