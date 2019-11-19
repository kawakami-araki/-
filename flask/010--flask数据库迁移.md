# `flask`数据库迁移

------

```python
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm.orm import *
from sqlalchemy.dialects.mysql import LONGTEXT,DECIMAL,DATETIME

Host = '127.0.0.1'
Port = '3306'
User = 'root'
Password = '000000'
Database = 要使用的数据库名称
DB_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'.format(user=User,password=Password,host=Host,port=Port,database=Database)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()
class person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
Base.metadata.drop_all()
Base.metadata.create_all()

```

创建一个模型

------

```
alembic init alembic
```

创建新的alembic文件(此操作在命令提示符中完成)

------

修改alembic文件内容

- 打开alembic.ini文件
  - 修改***<u>sqlalchemy.url**</u>*为:

​		

```
			sqlalchemy.url = 'mysql+mysqlconnector://root:password@localhost:port/database'
```

- 打开alembic文件夹

  - ![](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572832080587.png)

  - 打开env.py文件

    - 在其中添加以下代码

    - ```python
      import sys,os
      import app
      sys.path.append(os.path.dirname(os.path.dirname(__file__)))
      ```

  

  - 修改文件代码

    - ```python
      #修改前
      target_metadata = None
      #修改后
      target_metadata = app.Base.metadata
      ```

      ------

------



```


*alembic revision --autogenerate -m 'first commit'
创建新的迁移脚本(此操作在命令提示符中完成)
alembic revision --autogenerate -m 'add age column'
更新迁移脚本(此操作在命令提示符中完成)

```

------



#### <u>***alembic upgrade head***</u>

数据库迁移开启(此操作在命令提示符中完成)

------

### **<u>alembic常用字段</u>**

- ​	init
  - 新建一个仓库
- revision
  - 创建一个新的版本文件
- --autogenerate
  - 自动将当前模型的修改,生成迁移文件
- --m
  - 本次迁移做了哪些修改,可以通过指定这个参数,进行回顾
- upgeade
  - 将置定版本的迁移文件映射到数据库之中,如果有多个迁移文件没有映射,那么会执行多个迁移脚本
- [head]
  - 代表最新的迁移脚本的版本号
  - 一般指向最新版
- 'first commit' 
  - 生成第一个迁移脚本时的映射参数
- add age column
  - 修改数据库时使用的映射参数
- history
  - 列出所有的迁移版本及其信息
  - alembic history  (展示所有的版本更新的版本号)
- heads
  - 展示head指向的脚本文件的版本号
  - 这个版本号通常为正在使用的版本号
- downgrade
  - 执行指定版本迁移文件中的downgrade函数
  - 与upgrade对应,使用方法为
    - alembic downgrade 版本号
    - 版本号可以在文件中查看,即为对应迁移文件中的revision的值
- current
  - 展示当前数据库中的版本号
  - 使用方法
    - 在数据库中会生成一个额外的表,alem_version ,这个表中存储着当前的版本号
    - 在命令提示符中输入
      - alembic current 会得到当前正在使用的版本号

------

## ***<u>alembic在flask中的使用*</u>**

- 前期操作方法相同

- 在创建好仓库时,按照以下步骤设定

  - 找到alembic.ini文件

  - ![1572849457816](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572849457816.png)

  - 修改其中的sqlalchemy_uri的值为要使用的数据库链接

  - 找到alembic文件夹下的env.py

  - 在其中进行如下操作

  - ```python
    import sys,os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import app
    *
    target_metadata = app.db.Model.metadata
    ```

- 之后的操作和之前并无差别