import cards_tools

while True:
    cards_tools.show_menu()
    action_str = input('请选择希望输入的信息：')
    if action_str in ['1', '2', '3', '4']:
        if action_str == '1':
            cards_tools.add_cards()
        elif action_str == '2':
            cards_tools.modify_cards()
        elif action_str == '3':
            cards_tools.show_details()
        else:
            cards_tools.show_all()
    elif action_str == '0':
        break
    else:
        print('您输入不正确')
