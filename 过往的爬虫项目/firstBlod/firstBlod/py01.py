# import pymysql
# conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='000000',db='spider',charset='utf8')
#
# sql = 'insert into bs values ("%s","%s")' % ('aaa', 'aaat')
# cur = conn.cursor()
# cur.execute(sql)
# conn.commit()

from pymongo import  MongoClient
client = MongoClient('localhost',27017)
db = client.local
collection = db.spider
# collection.insert({'name':'Tom','age':25,'addr':'Cleveland'})

for item in collection.find({'name':'Tom'}):
    print(item)


