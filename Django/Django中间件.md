# django中间件

中间件需要使用request参数的META属性

- 获取用户ip地址

  - ​		如下所示
  - 

  ```
  request.META['REMOTE_ADDR']
  ```



## 自定义中间件类对访问的ip进行限制,从而对特定ip进行封号处理

1. 创建一个全新的中间件文件

   1. 创建一个新的中间件问价

      - middleware.py

      - ```python
        from django.http import HttpResponse
        
        class BlockedIPSMiddleware(object):
            EXCLUDE = ['192.168.1.238','127.0.0.1']
            def process_view(self,request,view_func,*view_args,**view_keargs):
                user_ip = request.META['REMOTE_ADDR']
                if user_ip in BlockedIPSMiddleware.EXCLUDE:
                    return HttpResponse("拒绝访问")
        ```

      - 注意,2.0以后无法使用以上的方法进行中间价创建

      - ```python
        from django.http import HttpResponse
        
        from django.utils.deprecation import MiddlewareMixin
        
        class BlockedIPSMiddleware(MiddlewareMixin):
            EXCLUDE = ['192.168.1.238','127.0.0.1']
            def process_view(self,request,view_func,*view_args,**view_keargs):
                user_ip = request.META['REMOTE_ADDR']
                if user_ip in BlockedIPSMiddleware.EXCLUDE:
                    return HttpResponse("拒绝访问")
        ```

   2. 创建好之后,再setting文件中进行中间件注册

      - setting.py文件中
      - MIDDLEWARE = [要注册的中间件函数路径]
      - 该路径需要精确到中间件函数类

   3. 运行django项目,可以看到,被记录的函数已经无法正常访问这个项目了

   4. 中间件覆盖了项目所属所有的页面

2. process_exception

   1. 这个中间件函数将会在视图函数出错的时候进行调用

   2. ##### 注意,这个函数在进行调用的时候,如果多个中间件类都定义了这个函数并且都进行了注册,将会以从下往上的顺序进行调用