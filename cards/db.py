import pymysql


class CardsAdd():
    def __init__(self,
                 host='localhost',
                 user='root',
                 password='root',
                 dbname='CARDDB'):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.db = pymysql.connect(self.host, self.user, self.password,
                                  self.dbname)
        self.cursor = self.db.cursor()

    def insert(self, name, phone, qq, email):
        # import pdb;pdb.set_trace()
        self.name = name
        self.phone = phone
        self.qq = qq
        self.email = email
        sql = 'insert into cards(name,phone,qq,email) values("%s",%s,%s,"%s")'
        try:
            self.cursor.executemany(sql,
                                [(self.name, self.phone, self.qq, self.email)])
            self.db.commit()
        except:
            print('Add failed')
            self.db.rollback()

    def delete(self,id):
        self.id = id
        sql = 'delete from cards where id=%s'
        try:
            self.cursor.executemany(sql,[(self.id)])
            self.db.commit()
        except:
            print('Delete Failed')
            self.db.rollback()

    def select_all(self):
        sql = '''
        select * from cards
        '''
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            # for row in results:
            #     id = row[0]
            #     name = row[1]
            #     phone = row[2]
            #     qq = row[3]
            #     email = row[4]
            #     return id, name, phone, qq, email
            return results
        except:
            print('Error: Failed to fetch data from database!')

    def select_card(self,id):
        self.id = id
        sql = 'select * from cards where id=%s'
        try:
            self.cursor.executemany(sql,[(self.id)])
        except:
            print('Select Failed')

    def __del__(self):
        self.db.close()
