#!/usr/bin/env python3

user_name = 'sam'
user_password = '123123'

for i in range(3):
    input_user_name = str(input('Please input your name\n'))
    input_user_password = str(input('Please input your password\n'))
    if user_name == input_user_name:
        if user_password == input_user_password:
            print('Login success')
            break
        else:
            print('Password Error')
    else:
        print('Username Error')
