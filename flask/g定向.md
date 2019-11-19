# g定向

- g定向使用

  - ```python
    from flask import Flask,g
    
    
    app = Flask(__name__)
    
    @app.route('/')
    def func():
        g.username = 'root'
        return 'hello world'
    ```

  - g的声明方法和local相同

  - 使用g定向声明过的变量在整个flask文件中通用,及如果你在app中调用了另一个外部文件的函数,在这个函数中你是可以直接传入g来使用你在app中声明的变量的

  - 这样可以不传入参数