# 元类

### 	通过在模型类中定义元类来对创建好的数据库表进行约束,以确保生成的数据表不依赖于应用文件的名字





```python
from django.db import models
class BookInfo(models.Manager):
    btitle = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'bookinfo'
```

#### 定义元类Meta,设定好创建的数据库的名字之后,执行数据库迁移

#### 产生的数据库名字将不会安装应用名_模型类名的规则进行创建





# 模板错误试图:

### 调试模式:

- ​	在网站上线时,应关闭DE_BUG模式,该选项在setting文件中进行配置,默认为true

  ​		默认选项

  ```python
  DEBUG = True
  
  ALLOWED_HOSTS = []
  
  ```

  ​		修改选项

  ```python
  DEBUG = False
  
  ALLOWED_HOSTS = ['*']
  ```

​	ALLOWED_HOSTS选项设定的是允许访问的IP地址,一般默认设置为*,即允许所有

- ​	错误访问视图
  - 当出现错误请求或者服务器异常时,我们可以对从异常操作的响应进行,如自定义错误页面
  - 常见的错误有404(页面不存在)、500(服务器错误)
  - 自定义错误访问视图需要在templates模板文件夹下创建错误访问模板,文件名为对应的http状态码,
  - 如: 404.html
  - 错误试图的定义需要关闭debug模式

