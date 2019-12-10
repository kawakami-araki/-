# DRF框架权限验证器:

基础验证器

1. drf中集成了关于权限验证的一些基本模块,具体可以分为:

   ​			所有用户均可访问---—---AllowAny

   ​			登录用户可访问–-—---IsAuthenticated

   ​			仅限管理员权限可以访问--------IsAdminUser

2. 关于基本权限验证模块的使用方法

   - 话不多说,上代码

   - ```python
     from rest_framework.permissions import AllowAny
     from rest_framework.views import APIView
     class MyPermissions(APIView):
         
         permission_classes = [AllowAny]
         #当视图函数中设定permission_classes的值为AllowAny时,这个页面允许任何人访问,也就是说,相当于允许游客进行访问
         def get(selfg,request):
             return HttpResponse('权限验证通过,欢迎')
         
         
     
     from rest_framework.permissions import IsAuthenticated,IsAdminUser
     from rest_framework.views import APIView
     class MyPermissions(APIView):
         
         permission_classes = [IsAuthenticated]
         #当视图函数中设定permission_classes的值为IsAuthenticated时,这个页面允许任何用户访问,也就是说,只要你进行登录,就可以进行访问
         def get(selfg,request):
             return HttpResponse('权限验证通过,欢迎')
         
         
     from rest_framework.permissions import IsAdminUser
     from rest_framework.views import APIView
     class MyPermissions(APIView):
         
         permission_classes = [IsAdminUser]
         #当视图函数中设定permission_classes的值为IsAdminUser时,这个页面只允许拥有管理员权限的用户进行访问
         def get(selfg,request):
             return HttpResponse('权限验证通过,欢迎')
     ```

     

# 自定义权限验证器:

1. 在drf中,允许我们自定义一些权限验证器,来实现我们想要的一些功能,比如说.…...留后门、留后门,还有...留后门之类的操作,当然,如果是大公司,同时自己又没有高级权限的话,不建议留后门,毕竟如果留后门被发现了的话不太好,哈哈哈哈

2. 上代码

   - 首先创建一个自定义的权限验证,这个验证就不需要使用自带的模块了,直接自定义

   - ```python
     from rest_framework.permissions import BasePermission
     class My_permissions(BasePermission):
         def has_permission(self,request,view):
             if request.query_paramy.get('user') == 'root':
                 return True
     ```

   - 在调用权限验证的时候选择使用自定义的权限验证器

   - ```python
     class MyPermissions(APIView):
         permission_classes = [My_permissions]
         def get(self,request):
             return HttpResponse('权限验证通过,欢迎')
     ```



------



# 限流

### 全局限流设置:

- 在setting文件中设定限流要求

  - ```python
    
    REST_FRAMEWORK = {
        'DEFAULT_THROTTLE_CLASSES':(
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ),
        'DEFAULT_THROTTLE_RATES':{
            #单位时间内访问次数限制
            #anon匿名用户限流
            'anon':'1/second',
            #user注册用户限流
            'user':'1/second'
        }
    }
    ```

  - 注册限流信息时,所需要使用的rest_framework模块需要现在INSTALLED_APPS中进行配置才能进行使用,同时,这里使用的时候需要与注册的app名相同



### 局部限流设置:

- 无论是局部限流还是全局限流,都需要现在setting文件中进行配置,但是这个配置并不相同

  - ```python
    REST_FRAMEWORK = {
        'DEFAULT_THROTTLE_RATES':{
            'anon':'1/second',
            'user':'1/second'
        }
    }
    ```

  - 在进行局部限流时,不需要导入自带的限流模块

  - ```python
    from rest_framework.views import APIView
    from rest_framework.throttling import UserRateThrottle
    class Mythrottling(APIView):
        throttling_class = [UserRateThrottle]
        def get(self,request):
            return Response('这是投票页面')
    ```

    

