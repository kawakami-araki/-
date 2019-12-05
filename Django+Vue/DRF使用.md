# DRF初试

1. 创建一个新的序列化器

   1. Serializer序列化器创建,通常这个序列化器我们使用一个新的文件承载

      - ```python
        from rest_framework import serializer
        from .models import *
        class StudentsSerializer(serializer.ModelSerializer):
        	class Meta:
                model = Students
                fields = '__all__'
        ```

      - 在创建序列化器的时候,需要直接或者间接的继承serializer.Serializer这个类

      - 当序列化器继承自serializer.ModelSerializer的时候,需要在序列化器的模型类中声明要使用的模型类model,以及要使用的字段fields

      - 当fields的值为'__all__'的时候,就相当于对应着这个模型类中的全部字段

      - 字段声明

        - 

   2. 在view中使用这个序列化器

      - ```python
        from rest_framework.viewsets import ModelViewSet
        from .serializer import StudentsSerializer
        from .models import *
        class StudentsAPIViews(ModelViewSet):
            queryset = Students.objects.all()
            serializer = StudentsSerializer
        ```

   3. 在settings文件中注册test_framework应用

      - ```python
        INSTALLED_APPS = [
        	'test_framework'
        ]
        ```

   4. 设置test_framework模块路由

      - ```python
        from test_framework.routers import DefaultRouter
        from .views import StudentsAPIViews
        urlpatterns = []
        router = DefaultRouter()
        router.register('student',StudentsAPIViews,basename='StudentsAPIViews')
        
        
        urlpatterns += router.urls
        
        ```

   5. 在主路由中配置好应用的路由

      - ```python
        from fjango.contrib import admin
        from django.urls import path,include
        urlpatterns = [
            path('admin/',admin.site.urls),
            path('api/',include('drf_app.urls')),
        ]
        ```

        