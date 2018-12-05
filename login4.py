#!/usr/bin/env python3

user_name = ['seven', 'alex']
password = '123123'

for i in range(3):
    user_name_input = input('Input username\n')
    password_input = input('Input password\n')
    if user_name_input in user_name:
        if password_input == password:
            print('login success,login as {}'.format(user_name_input))
            break
        else:
            print('password error')
    else:
        print('username error')
