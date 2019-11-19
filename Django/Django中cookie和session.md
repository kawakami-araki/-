# COOKIES

1. 设置cookie

   1. 创建一个全新的HttpResponse对象

      ```python
      response = HttpResponse('设置cookie')
      response.set_cookie('num',1,max_age=10*24*3600)
      ```

   2. 获取cookie

      ```python
      num = request.COOKIES['num']
      return HttpResponse(num)
      ```

2. 设置过期时间

   1. max_age,设置单位为秒

      ```python
      response.set_cookie('num',1,max_age=10*24*3600)
      ```

   2. exprice,设置较为复杂,但是适合长期设置

      ```python
      from django.http import JsonResponse,HttpResponse
      from datetime import datetime,timedelta
      response.set_cookie('num',1,expires=datetime.now() + timedelta(days=10))
      ```

      

------

# 相较于cookie,session安全性较高,在保存一些重要数据时,更适合使用session来进行保存,如用户的帐号,密码,私人信息等

# sessions

1. 设置session

   1. ```python
      #设置session
      def set_session(request):
          request.session['username'] = 'root'
          request.session['age'] = '000000'
          return HttpResponse('设置成功')
      ```

2. 获取session

   1. ```python
      #获取session
      def get_session(request):
          username = request.session['username']
          age = request.session['age']
          return HttpResponse(username + ':' + str(age))
      ```

3. session使用方法
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

      

