# 		*<u>**flask_session  /cookies*</u>**

## cookie创建:

```python
from flask import Response

res = Response('示例')

res.set_cookie('username','root',
               max_age=60,
               expires=datetime(year,month,day,hour,minute,second),
              domain='.fcg.com')
#创建cookie时需要导入以下几项,
#	1.cookies名字 + cookies值 (必传)
#	2.max_age从当前开始计算的过期时间,单位为秒,不添加的时候默认过期时间为关闭浏览器过期
#	3.expires设定过期时间,以格林尼治标准时间计算,换算到北京时间需要减八,这个参数如果设置的话,需要传入六个参数分别是--(year,month,day,hour,minute,second)
#	4.domain设定cookie作用范围,在主域名前面加上.即为将此cookie应用于所有子域名
#	5.设定作用范围,需要先绑定好主域名和子域名

#cookie删除
res = Response('删除')
res.delete_cookie('username')


```

------

## session创建:

```python
from flask import Flask,session
app = Flask(__name__)


@app.route('/')
def func():
    #创建并设置session.cookie
    session['username'] = '123'
    #设定session过期时间
    session.permanent=True
    return 'hello world'

#session.permanent默认为一个月
#可以通过设定修改,
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(剩余过期的时间)

#session删除
session.pop('username')
#相当于字典删除
session.clear()
#将session中储存的数据全部清空
del session[key]
```

------

## ***<u>请求函数的装饰器使用方法</u>*:**

```python
decorators 
```

- 设置请求函数过滤用装饰器

- ```python
  #从functools 中导入模块wraps
  from functools import wraps
  
  from flask import session,redirect,url_for
  def login_required(func):
      #设定从functools里面导入的装饰器,此装饰器的参数为外部函数传入的值
      @wraps(func)
      #定义内层函数,该内从函数中执行运算与判定
      def wrapper(*args,**kwargs):
          #获取session
          username = session.get('username')
          #判断是否存在session
          if username:
              #存在session时,正常调用外层函数传入的func参数
              return func(*args,**kwargs)
          else:
              #当session中不存在对应的cookie时,重定向当前网址到登陆界面
              return redirect(url_for('login'))
          
      #正常的闭包函数用法,返回内层函数的引用
      return wrapper
  ```

  