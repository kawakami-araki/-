#               ***<u>flask_route*</u>**

- 创建app主体

  - ```python
    from flask import Flask
    app = Flask(__name__)
    ```

- 绑定路由

  - ```python
    @app.route('/')
    ```

  - ```python
    @app.route('/',methods=['GET','PORT'])
    ```

  - 绑定路由时,如果不设定methods方法,将会默认为get方法,这种情况下,其他方法无法访问

- 设定路由的执行函数

  - ```python
    def hello_world():
        return 'hello world!'
    ```

  - 路由的执行函数通过return来实现,在不返回HTML页面的情况下,可以将要返回的数值直接返回,但是只能返回字符串类型

- 在设定玩路由之后,只需要开辟一个程序入口进行运行,就构成了一个完整的flask

  - ```python
    if __name__ = '__main':
        app.run(debug=True)
    ```

    