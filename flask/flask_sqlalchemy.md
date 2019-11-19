# flask_sqlalchemy



## 创建flask数据库链接

------

```python
from flask import Flask
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.comfig['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:port/database'
db = SQLALchemy(app)
class person(db.Model):
    __tablename__ = 'person'
    id = db.COlumn(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
db.drop_all()
db.create_all()

@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ = '__main__':
    app.run()
```



------

## 关于导包:

- flask_sqlalchemy中把sqlalchemy的所有模块整合到了一起,所以不需要像原生sqlalchemy一样导入一大堆模块,在这一方面做的比原生SQL alchemy好得多

  

------

## 关于分页查询:

# <u>paginate</u>

per_page:设定每页展示的数据

page:当前的页数

has_prve:判断是否具有上一页

has_next:判断是否具有下一页

prve_num:上一页的页码

next_num:下一页的页码

iter_pages: 所有页码,可遍历