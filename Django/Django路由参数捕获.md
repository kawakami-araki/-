# URL参数捕获

1. 参数捕获的方法有两种

   - 位置参数传参

     - 使用一个正则表达式获取参数并传入视图函数中

     - ```python
       from django.urls import re_path,path
       
       urlpatterns = [
       	re_path(r’index/(\d+)‘,veiws.index),
       ]
       ```

       

   - 关键字参数传参

     - 使用关键字参数传参和位置参数是一样的,区别就是再正则表达式中给这个字段起一个别名

     - ```python
       from django.urls import re_path,path
       
       urlpatterns = [
       	re_path(r’index/(?P<num>\d+)‘,veiws.index),
       ]
       ```

       

