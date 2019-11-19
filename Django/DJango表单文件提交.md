# Django表单提交

- Django表单数据提交涉及到视图函数中的request参数
  - 在django中, request对象封装了表单提交的数据
  - **<u>*request.GET</u>***中存储的是get方法提交的数据
  - **<u>*request.POST</u>***中存储的是post方法提交的数据
- 这些方法使用get方法可以获取到对应的值,获取的名称为表单中提交的数据的名字
- 这些数据将会在提交之后自动储存到request中去



## request其他方法:

- get()

  - 获取request对象中储存的数据

- path

  - 获取当前访问的url地址

- method

  - 获取当前的访问方法

- POST

  - 存储所有使用post方法提交过来的数据

- GET

  - 存储所有使用get方法提交过来的数据

- FILES

  - 存储提交过来的文件对象

- COOKIES

  - 存储cookie信息

- session

  - 存储session信息

  - session使用方法

    1. 直接使用字典的键值对获取方法

       ```python
       request.session['cookie名']
       ```

    2. 使用get方法获取,可以设置默认值

       ```python
       request.session.get('cookie名,default="默认值")
       ```

    3. clear,删除session中保存的数据,但是删除掉的只是值

       ```python
       request.session.clear()
       ```

    4. flash,删除整条数据,完全删除所有数据,数据表完全清除

       ```python
       request.session.flash()
       ```

    5. del    删除目标数据的所有内容

       ```python
       del request.session['cookie']
       ```

    6. 设置session过期时间

       ```python
       request.session.set_expiry(value)
       ```

       - 当没有设置过期时间的时候,默认将会在两周之后过期
       - 当value值为0的时候,将会在关闭浏览器的时候过期
       - 当value大于0的时候,将会在value秒之后过期

    7. has_key   判断session中有没有对应的cookie

       ```python
       request.session.has_key('username')
       ```

       





# ajax方法提交数据

### ajax请求为异步请求

async : true  

该选项默认为true,即异步请求

​	异步请求时优先执行其他的javascript代码,然后才会执行ajax请求的代码

设定为false即为同步请求

------

使用ajax可以实现局部刷新

------



1. 使用ajax方法提交数据

   - ```javascript
     $.ajax({
         'url':'/ajax_handle',
         'dataType':'json',
     }).success(function(data){
         alert(data.res)
     })
     ```

   - 上述为ajax在页面中的代码部分

   - ```python
     from django.http import JsonResponse
     #处理ajax请求的是视图函数
     def ajax_handle(request):
         return JsonResponse({'res':1})
     
     ```

   - 上述为ajax信息处理函数

   - ```python
     urlpatterns = [
         #构建用于处理请求的网页url
         path('ajax_handle/',views.ajax_handle),
     ]
     ```

   - 以上就是基础的ajax请求构建

   - ajax请求禁止返回一个页面,返回的页面将会无法正常显示

------



1. # 踩坑详情

   - ```
     APPEND_SLASH=False
     ```

     - 踩坑第一条
       - 使用ajax进行请求时无法绕过的一个坎,必须在settings配置文件之中配置这条数据才能继续进行下去,让人惊讶的是,教学视频之中居然没有提到这个问题,暂定为django版本过高导致的配置文件差异,从而出现的问题

   - ```
     $.ajax({
         'url':'/ajax_handle/',
         'type':'POST',
         'dataType':'json',
         'data':{
             username:username,
             password:password
         }
     }).success(function (data) {
         if (data.res == 1){
             location.href = '/admin/'
         }else{
             $("#err").show().html('账号名或密码错误')
         }
     })
     ```

     - 踩坑第二条

       - 在路由函数方面,django的路由设定比起flask更加严谨
         - 书写路由重定向时,如果你写的路由为"admin/"这样的格式
           - ​			那么最终请求的网址实际上为;
           - ​			当前网页网址的路由后面加上你要跳转的路由
             - ​		 即:	127.0.0.1:8000/login/admin
           - 在不添加前置/的情况下,默认为在当前网址的基础上再次进行路由访问
         - 无论是ajax里面的url请求地址,还是JavaScript基础上进行的重定向,都需要注意这一点
         - 反之,如果在路由前面加上/,访问的界面实际上就是在最基础的127.0.0.1:8000/的基础上进行的路由访问

     - ## 这些坑需要谨记

