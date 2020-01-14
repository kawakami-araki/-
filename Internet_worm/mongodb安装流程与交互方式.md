[TOC]



# mongodb;

1. 第一步,安装

   1. [官方网站网址](<https://www.mongodb.com/download-center?jmp=nav#community>)

2. 第二步,环境配置

3. 第三步

   1. 构建mango.config文件

      - 文件内部填充

      - ```
        port = 27017
        dbpath= D:\MongoDB\data\db
        logpath= D:\MongoDB\data\log\mongo.log 
        directoryperdb = true
        fork = true
        logappend=true
        journal=true
        quiet=true
        ```

4. 启动mongo服务

   1. ```
      mongod --dbpath D:\MangoDB\data
      ```

5. 启动另一个窗口

   1. 输入mongo
   2. 如果进入了服务的话,说明启动成功了



## python与mongodb交互:

```python
from pymongo import  MongoClient
client = MongoClient('localhost',27017)

db = client.local

collection = db.spider

# collection.insert({'name':'Tom','age':25,'addr':'Cleveland'})


for item in collection.find({'name':'Tom'}):
    print(item)
```

### 将字符串数据转换成时间字段:

```python
from dateutil import parser
dateStr = "2019-12-19"
myDatetime = parser.parse(dateStr)
print(myDatetime)
```



# mongoDB操作指令:

1. show dbs
   1. show databases
   2. 基本上和mysql一样
2. use dbname
   1. 进入数据库,
3. show tables
   1. 展示所有的表
4. mongodb不需要进行创建表或者是创建库,在需要使用的时候只需要直接使用就行,内部程序将会自动创建对应的数据库与数据表
5. 在第一次向一个集合插入数据的时候,就会自动创建目标集合
6. mongodb自动生成_id属性作为数据得到唯一性识别码
7. db.tableName.finc()
   1. 查看表中的全部数据
8. db.tableName.insert({})
   1. 在表中插入数据

