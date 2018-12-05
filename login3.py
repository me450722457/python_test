#!/usr/bin/env python3

user_name_1 = 'seven'
user_name_2 = 'alex'
password = '123123'

for i in range(3):
    user_name = input('Input your username\n')
    user_passwd = input('Input your password\n')
    if user_name == user_name_1:
        if user_passwd == password:
            print('login success,login as {}'.format(user_name_1))
            break
        else:
            print('password error')
    elif user_name == user_name_2:
        if user_passwd == password:
            print('login success,login as {}'.format(user_name_2))
            break
        else:
            print('password error')
    else:
        print('username error')
