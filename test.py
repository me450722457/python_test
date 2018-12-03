#!/usr/bin/env python3
account = 'admin'
password = '123456'

user_account = input(str('Please input your account\n'))
user_password = input(str('Please input your password\n'))

if user_account == account:
    if user_password == password:
        print('success')
    else:
        print('password error')
else:
    print('account error')
