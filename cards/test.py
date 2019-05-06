import db

a = db.CardsAdd()

a.insert('gujin_test1', 1860146, 450722457, 'me450722457@vip.qq.com')
print(a.select_all())