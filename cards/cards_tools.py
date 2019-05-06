from functools import wraps
import db


def show_menu():
    print('*' * 50)
    print('欢迎使用【名片管理系统】v1.0')
    print('1. 新增名片')
    print('2. 修改名片')
    print('3. 显示详情')
    print('4. 显示所有\n')
    print('0. 退出')
    print('*' * 50)


def format_line(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('\n' * 10)
        print('-' * 50)
        return func(*args, **kwargs)

    return wrapper


@format_line
def add_cards():
    '''
    1.添加名片信息
    2.调用插入数据库方法
    3.提示用户完成添加或者失败
    '''
    name = str(input('请输入名称： '))
    phone = int(input('请输入电话： '))
    qq = int(input('请输入QQ号： '))
    email = str(input('请输入E-mail： '))
    connect = db.CardsAdd()
    connect.insert(name, phone, qq, email)


@format_line
def modify_cards():
    pass


@format_line
def show_details():
    pass


@format_line
def show_all():
    show_all_db = db.CardsAdd()
    print(show_all_db.select_all())

    # print(results)
