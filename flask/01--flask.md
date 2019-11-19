# -----------------------------flask开端--------------------------------



------

## flask安装:

- ​	pip install flask     在命令提示符中输入pip指令进行安装
- ​        使用pycharm安装flask
  - ![](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572838838246.png)
  - 在file选项中找到settings
  - ![](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572838962436.png)
  - 找到project选项,点击进入porject下的project interpreter选项中
  - ![](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572839047759.png)
  - 点击此处+号,进入搜索
  - ![1572839092726](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572839092726.png)
  - 搜索到之后打勾,点击install package ,开始下载



------

## flask使用:

- ​	初次创建flask工程

  - ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    
    @app.route('/')
    def hello_world():
        return 'hello world!'
    
    if __name__ = '__main__':
        app.run(debug=True)
    ```

    

- 注意,在2018之后版本的pycharm中,设定debug=true并不能开启debug模式,想要开启debug模式需要在pycharm中进行设定

  - ![1572839403379](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572839403379.png)
  - 点击运行按钮左边的选项,在台出的页面中选择edit configurations
  - 进入后勾选FLASK_DEBUG

  