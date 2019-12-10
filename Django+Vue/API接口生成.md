# 自动创建api接口的文档

## 	配置:

#### 				setting文件配置:

1. 下载模块

   ```python
   pip install corsapi
   ```

2. 配置SCHEMA_CLASS

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema'
   }
   ```

3. 在主路由中注册使用

   ```python
   from rest_framework.decumentation import include_docs_urls
   from django.url import path,include
   urlpatterns = [
       path('docs/',include_docs_urls(title='API管理页面')),
   ]
   ```

创建成功之后的画面如下图:![1575621839123](C:\Users\lenovo\Desktop\Django+Vue\assets\1575621839123.png)



在这里面,还有一些别的设置,如,在模型类中设置字段的提示属性 :

- help_text = ‘ ’

  