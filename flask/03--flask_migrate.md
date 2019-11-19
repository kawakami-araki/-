#                                                ***<u>flask_migrate*</u>**

------

## flask_migrate初试:

- 模块导入

  - ```python
    from flask_migrate import  Migrate,MigrateCommand
    ```

  - Migrate用于migrate对象实例化通过app以及db来构筑完整的migrate

  - MigrateCommand是一个对象,其中封存着要使用的command对象(此对象使用方法等同于flask_script的构筑方法)

  - 此处还可以导入flask_script模块

- 具体实现步骤

  - migrate文件内的构造

  - ```python
    #导入flask_script模块
    from flask_script import Manager
    #导入flask_migrate模块
    from flask_migrate import Migrate,MigrateCommand
    #导入app
    from app import app
    #导入数据库链接实例db
    from exts import db
    
    
    #实例化manager对象
    manager = Manager(app)
    #开始创建app与数据库连接
    Migrate(app,db)
    #在创建好的对象中添加script子命令
    manager.add_command('db',MigrateCommand)
    
    ```

  - exts文件中的构造

  - ```python
    from flask_sqlalchemy import SQLALchemy
    
    db.SQLALchemy()
    ```

  - app文件中的构造

  - ```python
    from flask import Flask
    from exts import db
    import config
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    
    
    if __name__ == '__main__':
        app.run()
    
    ```

  - models文件中的构造

  - ```python
    from exts import db
    class person(db.Model):
        __tablename__ = 'person'
        id = db.column(db.Integer,primary_key=True,autoincrement=True)
        name = db.Column(db.String(100))
    ```

------

## flask_migrate在命令行中的使用:

- 进入文件夹,打开命令窗口

- ```python
  python 文件名 db(子命令名称) init
  #创建一个migrations文件夹
  ```

- 创建一个迁移文件

- ```python
  python 文件名 db(子命令名称) migrate
  ########################################
  #注意,这里有一个坑,如果在创建migrate文件的时候,没有传入你的models文件中的表(类)
  #那么将会出现无法找到表的情况
  #具体表现形式为
  """
  INFO  [alembic.runtime.migration] Context impl MySQLImpl.
  INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  INFO  [alembic.env] No changes in schema detected.
  """
  #在这种情况下,需要在migrate中导入表
  form models import Person
  ########################################
  ```

- 将创建好的迁移文件映射到数据库中

- ```python
  python 文件名 db(子命令名) upgrade
  #完成数据库映射
  ```

- python 文件名 db(子命令名) downgrade

- python 文件名 db(子命令名) head

- python 文件名 db(子命令名) history

基本上所有的方法对应着flask_alembic中的方法

可以使用 --help方法查看可以使用的全部方法