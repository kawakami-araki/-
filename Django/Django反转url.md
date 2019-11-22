# Django反转url

1. ## 反转url:

   1. 使用模板语言url

      - {% url ‘index’ %}
      - {% url ‘url路由函数名’ %}

   2. 在url定义中设定路由函数名

      - path(‘index’,views.index,name=‘index’)

   3. 关于应用注册的路由的反转使用

      1. 注册应用路由时添加namespace
         - path(‘’,include('besate',namespace=‘basete’))
      2. 在应用的urls文件中添加
         - app_name = ‘besate’
      3. 使用反转
         - {% url ‘besate:index’ %}

   4. 关于带参数的路由的反转编译

      1. ```
         {% url ‘index’ 参数数值 %}
         ```

         位置参数

      2. 

      ```
      {% url ‘index’ 参数名=参数数值 %}
      ```

      命名参数

2. 在视图中进行反转url操作

   1. 导入模块

      - 原始的方法是从另一个模块中导入,但是3.0中包含了这个模块

      - 所以这个模块现在集成到了django.shortcuts中,只需要再导入render的时候顺便就可以一并导入进去了

      - ```python
        from django.shortcuts import render,reverse,redirect
        ```

   2. 传入参数

      - 传入位置参数时
        - reverse(‘three:index’,args=(1,2,3))
      - 传入命名参数时
        - reverse(‘three:index’,kwargs={‘a’:1,‘b’:2})