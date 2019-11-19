# 				***<u>flask_wtf***</u>

------

## *flask_wtf简介:*

- ​	flask_wtf模块下载安装
  - pip install flask-wtf
  - 使用命令行形式安装flask_wtf模块

------

## flask_wtf实际使用:

- ```python
  from wtforms import Form,StringField,PasswordField,SubmitField
  from wtforms.validators import EqualTo,Length
  #创建一个全新的form表单类,该类继承自Form
  class RegistForm(Form):
      #username属性设定
      username = StringField(validators=[Length(min=3,max=8)])
      #password属性设定
      password= PasswordField(validators=[Length(min=6,max=10)])
      #EqalTo作用,添加EqualTo的字段必须与其参数的值相同,相当于绑定
      password_1 = PasswordField(validators=[Length(min=6,max=10),EqualTo('password')])
      sub = SubmitField()
  
  app = Flask(__name__)
  
  
  @app.route('/')
  def hello_world():
      return 'Hello World!'
  #创建form表单提交页面
  @app.route('/regist',methods=['GET','POST'])
  def regist():
      #判断请求方式并给出相应回复
      if request.method == 'GET':
          return render_template('regist.html')
      else:
          #实例化表单类
          regist_form = RegistForm(request.form)
          #判断类中的validate是否正常,即验证是否通过
          #根据判定结果进行不同的返回情况
          if regist_form.validate():
              return 'True'
          else:
              print(regist_form.errors())
              return "false"
  
  ```

- 在length函数中,可以添加一个新的参数,message,用来设定报错之后的

- ```python
  username = StringField(validators=[Length(min=3,max=8,message='您所输入的账户名称不符合要求.请重新输入')])
  ```

- 这个message所储存的参数将会体现在类的errors方法里面,可以通过直接输出来查看

------

## flask_wtf常用验证器:

验证器导入方法:

```python
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import NumberRange
from wtforms.validators import Email
from wtforms.validators import InputRequired
from wtforms.validators import Regexp
from wtforms.validators import URL
from wtforms.validators import UUID

```



- EqualTo           

  - 绑定另一个字段,使两个字段保持一致

- Length             

  - 限定内容长度,以及自定义报错提醒

- NumberRange   

  - 限定数字的大小所在区间,和length一样有max和min两个值限制,只有在这两个值之剑才满足

- Email               

  - 邮箱验证器,用于验证邮箱,不需要参数,内置了邮箱格式验证

- InputRequired  

  - 对输入的信息进行验证,有值即为True,没有则为false

- Regexp

  - 正则表达式,自动将输入的内容于Regexp的内容匹配对照

- URL

  - 验证输入的是否为正确的url地址

- UUID

  - 验证是否为UUID

  - UUID导入方法

    - ```python
      form uuid import uuid4
      print(uuid4())
      ```

------

## 自定义验证器:

- ```python
  def validate_字段名 (self,filed):
      #通过这个方法定义的验证器,将会自行调用进行判断,
  ```

- 自定义验证器的名字为validate_加上要绑定的字段名

- validate_字段名

- 需要设定一个形参,不限制









------

## flask_wtf常用字段:

- IntegerField

  - 整形字段,该输入框只支持输入数字类型
  - 最终拿到的值也是整形,即int
  - 同一属性的还有FloatField

- StringField

  - 字符串形式,该输入框支持输入字符串类型

- PasswordField

  - 密码字段,如果使用该字段创建表单,其生成的将会是密码输入框

- SubmitField

  - 此字段对应的是submit提交按钮

- BooleanField

  - 单选框模板
  - ![1572953397817](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1572953397817.png)

- FileField

  - 文件框

- SelectField

  - 下拉框

  - ```python
    tags = SelecrField('标签名',choices=[('1','python'),('2','ios')])
    ```

    