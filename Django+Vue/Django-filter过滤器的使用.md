# DJango-filter模块使用:

## 目前,过滤器django_filter只能在ListAPIView的子类中使用

1. ### 过滤

   - ```python
     from rest_framework.generics import ListAPIView
     from django_filters.rest_framework import DjangoFilterBackend
     class MYfilter(ListAPIView):
         queryset = Students.objects.all()
         serializer_class = StudentsSerializer
         filter_backends = [DjangoFilterBackend]
         filter_fields = ("id",)
         #注意,filter_fields的值必须是一个元组!!!!
     ```

   - 使用方法

     ```
     在网址url之后追加-------/?id=1
     ```

     

2. ### 排序

   - ```python
     from rest_framework.filters import OrderingFilter
     from rest_framework.generics import ListAPIView
     class MYfilter(ListAPIView):
         queryset = Students.objects.all()
         serializer_class = StudentsSerializer
         filter_backends = [OrderingFilter]
         ordering_fields = ['id']
     ```

   - 使用方法

     ```
     在网址url之后追加------/?ordering=xx
     xx为ordering_fields中准备的用来作为排序基准的字段
     倒序为在xx前加上-号
     ```

     