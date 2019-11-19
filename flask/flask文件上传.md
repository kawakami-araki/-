# <u>***flask--05***</u>

## 文件上传:

- ```python
  #导入必须的模块包
  from wtform import Form,StringField,PasswordField,SubmitField,BooleanField,FileField,SelectField
  #导入验证器包
  from wtform.validators import EqualTo,Length,UUID,URL,ValidatorsError,InputRequired,Email
  #从flask_wtf中导入file.FileRequired(是否为空验证)和file.FileAllowed(验证是否符合要求的格式,格式要求的范围作为参数进行传递,切记传入的参数必须为一个列表)
  from flask import Flask,request,render_template,send_from_directory
  from werkzeug.datastructures import CombinedMultiDict
  
  from flask_wtf.file import FileRequired,FileAllowed
  #导入文件名过滤包
  from werkzeug.utils import secure_filename
  import os
  
  
  app = Flask(__name__)
  
  upload_url = os.path.join(os.path.dirname(__file__),'image')
  
  
  class userForm(Form):
      #创建文件上传约束
      avater = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
      
  @app.route('/',methods=['GET','POST'])
  dedf func():
      if request.method == 'GET':
          return render_template('add.html')
      else:
          #使用ConbinedMultiDict模块对传输的两个不同的值进行合并,一起传入wtf文件传输判定中进行验证
          userform = userForm(CombinedMultiDict([request.form,request.files]))
          if userform.validate():
              avater = userform.avater.data
              filename = secure_filename(avater.filename)
              avater.save(os.path.join(upload_url,filename))
              return '上传成功'
      
  ```

  