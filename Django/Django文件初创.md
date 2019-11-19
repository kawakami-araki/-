

# Django首次使用

创建django项目:

#### django-admin startproect 项目名

创建一个完整的django项目

## 创建完整的django文件之后会生成一整套的文件,里面包含了django的各种配置:

1. '__init__.py'		声明这是一个python文件
2. settings.py           整个项目的配置文件
3. urls.py                  url路由的配置
4. wsgi.py                web服务器与django交互入口
5. manage.py          项目管理文件

------

## 此处错误问题:

```python
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```



- #### 提示版本错误,这一点需要将base.py文件中的报错代码注释掉,使其不会因为自身的mysqlclient版本过高导致报错

- 第二处错误为MySQLdb不存在

  - 解决办法

    ```python
    import pymysql
    pymysql.install_as_MySQLdb()
    ```

  - 打开项目中的init配置文件,在其中导入以上代码



------



## django开发时每个模块都需要创建一个应用来实现:

1. 创建应用的方法:

   1. 实例图片

      1. ![1573529761495](C:\Users\lenovo\Desktop\Django\assets\1573529761495.png)
      2. ![1573529772029](C:\Users\lenovo\Desktop\Django\assets\1573529772029.png)

   2. ```python
      #进入项目文件
      #打开cmd命令窗口
      #输入指令
      python manage.py startapp 要创建的应用名称
      #创建完成之后,将会自动生成一个应用文件夹,文件夹名字为创建时输入的名字,文件夹中包含各种初始化的配置文件
      ```

   

2. 配置文件详解:

   1. '__init__.py'		声明这是一个python文件
   2. models.py           与数据库相关的内容
   3. views                   接受请求,进行处理,与models/template进行交互,返回应答
      1. 定义处理函数
      2. 每一个请求都对应着一个处理函数
   4. tests.py                写测试代码的文件
   5. admin.py             网站后台管理相关文件

3. 启动django服务器服务

   1. 在setting.py文件中注册模块信息

   2. ```python
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'First',
      ]
      ```

      

   3. ```
      python manage.py runserver
      ```

      



