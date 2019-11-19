# Django视图管理

## #视图函数在views.py文件中进行定义

## 1).定义视图函数

​	

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return HttpResponse('视图函数成功')
```

------

## 2).配置路由

- 导入路由模块

  - ```python
    from django.urls import path
    from django.conf.urls import include
    urlatterns = [
        path('',include('路径'))
    ]
    ```

  - 设定好总的路由之后开始设定从属的路由

  - ```python
    from django.urls import re_path
    
    from First import views
    #导入views视图函数文件
    urlpatterns = [
        #给视图函数绑定url,
        re_path(r'index/',views.index)
        ###################################
        #两种方法都可以使用
        path('index/',views.index)
    ]
    ```

  - path配置方法不需要考虑路由名字匹配的问题

------

## 3).构建模板文件

------

- 构造模板

  - 在django2.2.7中,创建新的项目时会自动配置好tempalte文件,只需要在里面创建应用文件的模板文件夹即可,

  - 旧版本中并不主动生成template文件夹,所以需要自己创建并进行配置

  - ```
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ```

- 模板构造与导入

  - 加载模板文件

    - 从模板文件目录获取html文件的内容,得到一个模板对象
  - 定义模板上下文

    - 向模板文件传递数据
  - 模板渲染

    - 得到一个标准的html页面

      - ```python
        re_path(r'lists/(\d+)',views.lists)
        ```

      - 重定向,路由传参方法,使用正则匹配路由

      - ```python
        def lists(request,bid):
            books = BookInfo.objects.get(id=bid)
            heros = books.heroinfo_set.all()
            return render(request,'FirstTemplates/lists.html',{
                'books' : books,
                'heros' : heros
            })
        ```