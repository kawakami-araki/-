

#                ***<u>flask_script*</u>**

## flask_script安装:

1. ​	安装方法

   1. ```
      pip install flask-script
      ```

------

## flask_script初次使用:

1. ```python
   from flask_script import Manage
   from app import app
   manage = Manage(app)
   @manage.command
   def func():
       print('hello world')
       
       
   #最简单的flask_script创建
   #无参数
   ```

2. ```python
   @manage.option('-u','--username',dest='')
   def func(username):
       print("你输入的账号为%s"%username)
       
   #有参数
   ```

3. 进入命令提示符,进入代码所在的文件夹

   1. ```python
      python (文件名称) func
      
      #无参数
      ```

   2. ```python
      python (文件名称) func -u "root"
      
      #有参数
      ```

------

## flask_script进阶操作:

1. 额外创建一个script文件

2. 在文件中引入要集成的文件

   1. ```python
      from flask_script import Manager
      from app import app,db,Person
      
      db_script = Manager()
      @db_script.command
      def func1():
          print('仓库创建成功')
      
      
      @db_script.command
      def func2():
          print('数据迁移成功')
      
      @db_script.command
      def func3():
          print('数据映射成功')
      ```

3. 在主文件中注册附属的script文件

   1. ```python
      from flask_script import Manager
      from app import app,db,Person
      from db_script import db_script
      manager = Manager(app)
      manager.add_command('db',db_script)
      ```

4. 在命令提示符中使用

   1. ```python
      python 文件名 db func1
      python 文件名 db func2
      python 文件名 db func3
      ```

      

