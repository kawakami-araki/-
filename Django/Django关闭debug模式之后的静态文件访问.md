1. ```
   STATIC_URL = '/static/'
   #配置默认的static静态文件夹位置
   STATIC_ROOT = 'static'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR,'/static/')
   ]
   ```

   - ### 设置setting

2. 设置url

   1. ```.
      from django.views import static ##新增
      from django.conf import settings ##新增
      from django.conf.urls import url ##新增
      
      
      ............
          url(r'^static/(?P<path>.*)$', static.serve,
            {'document_root': settings.STATIC_ROOT}, name='static'),
      ```

   2. 固定公式可以直接使用

3. 模板中渲染

   1. ```
      <div id="box1"><img src="{% url 'static' path='logo/logo0.png' %}" alt=""></div>
      ```

   2. 使用url反转路由

   

   

   