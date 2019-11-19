# 										 app上下文

应用上下文和请求上下文都是存放到一个'LocalStack'的栈中

和应用app相关的操作就必须用到应用上下文,比如通过current_app获取当前这个app

和请求相关的操作就必须用到请求上下文,比如url_for反转视图函数

视图函数中不需要考虑上下文的问题



------



### 应用上下文:

```python
from flask import current_app
#current_app模块的作用是获取当前文件的栈
#使用的方法

current_app.name
#获取当前文件的名字
#此选项需要在路由函数中才能使用
#在路由函数外直接使用将会报错
```

- ##### 手动推入应用上下文:

  - 第一种方法:

    ```python
    #在路由函数外调用current_app模块
    #需要先设定好应用上下文
    app.context = app.app_context()
    app.context.push()
    print(current_app.name)
    
    ```

  - 第二种方法:

    ```python
    with app.app_context():
    	print(corrent_app.name)
    ```

------

### 请求上下文:

```python
#请求上下文最常见的一个是url_for
#在视图函数中
@app.route('/')
def func():
    #查看url_for打印出来的路由地址
    print(url_for('func1'))
    return 'hello world'

@app.route('/test/')
def func1():
    return 'hello user'

print(url_for('func1'))
#在路由函数外直接调用url_for 查看路由地址将会报错,原因是请求上下文问题
#此问题无法使用应用上下文的方法解决
```

- ##### 手动推入请求上下文:

  - ​	

    ```python
    #在路由函数之外调用
    with app.test_requert_context():
        print(url_for('func1'))
    #注意,test_request_context这个函数会在推送请求上下文之前先检查有没有应用上下文,如果没有,将会先推送一个应用上下文过来,在推送一个请求上下文,也就是说,在一定程度上等同于app_context的加强版
    ```

    