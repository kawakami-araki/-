

# generics

1. 这模块中封装着GenericsAPIViews类,对APIViews进行了进一步的封装,比起APIViews,它的功能进一步扩展

2. ```
   from rest_framework.generics import GenericsAPIViews
   ```

3. 

```python
from django.http import HttpResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentsSerializer,Students_Serializer
from . models import CuressInfo,Students


class StudentsAPIViews(View):
    # queryset = Students.objects.all()
    # serializer_class = StudentsSerializer
    def get(self,request):
        students = Students.objects.all()
        serializer = StudentsSerializer(instance=students,many=True)
        return HttpResponse(serializer.data)

    def post(self,request):
        import json
        data_string = request.body.decode()
        data_dict = json.loads(data_string)
        serializer = Students_Serializer(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse('ok')


class stdSl(View):
    def get(self,request,id):
        from .serializer import SerializerModel
        serializer = SerializerModel(data=Students.objects.all(),many=True)
        serializer.is_valid()
        print(serializer.data)
        return HttpResponse(serializer.data)
    def post(self,request,id):
        from .serializer import SerializerModel
        import json
        data_string = request.body.decode()
        data_dict = json.loads(data_string)
        serializer = SerializerModel(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(serializer.data)

    def put(self,request,id):
        instance = Students.objects.get(id=id)
        import json
        data_dict = json.loads(request.body.decode())
        serializer = Students_Serializer(instance=instance,data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse('ok')

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ModelSerializerAPIViews
class StudentsModelAPIViews(APIView):
    def get(self,request):
        instance = Students.objects.all()
        serializer = ModelSerializerAPIViews(instance=instance,many=True)
        return Response(serializer.data)

    def post(self,request):
        # instance = Students.objects.get(id=id)
        data_dict = request.data
        serializer = ModelSerializerAPIViews(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.error_messages)
        return Response(serializer.data)


from rest_framework.generics import GenericAPIView
class StudentsGenericAPIViews(GenericAPIView):
    queryset = Students.objects.all()
    def get(self,request):
        all_dict = self.get_queryset()
        serializer = ModelSerializerAPIViews(instance=all_dict,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ModelSerializerAPIViews(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

from rest_framework.generics import GenericAPIView
class StudentsGenericAPIViews(GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = ModelSerializerAPIViews
    def get(self,request):
        all_dict = self.get_queryset()
        serializer = self.get_serializer(instance=all_dict,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    


# ListModelMixin                  展示全部数据,里面封装的是全部数据的获取,方法名为list

# CreateModelMixin	   添加新的数据,这里面封存的方法名为create

# DestroyAPIView	  删除对应的数据,对应的方法为destroy

# UpdateAPIView		修改对应的数据,对应的方法名为update

# RetrieveAPIView	  获取单条数据,需要有对应的pk数值传入,方法名为retrieve


# RetrieveUpdateDestroyAPIView	这个里面封装了多个视图分支类,包括DestroyAPIView-------UpdateAPIView------RetrieveAPIView------GenericsAPIView四个,所以它里面包含了对应的方法
from rest_framework.mixins import ListModelMixin,CreateModelMixin
class StudentsListModelMixin(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Students.objects.all()
    serializer_class = ModelSerializerAPIViews
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

    
# from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# 
# 终极形态
# 
# ModelAPIViewSet里面,相当于继承了以上的多种方法
# 同时,在使用ModelAPIViewSet创建的类视图进行注册时,需要在as_view中传入参数具体操作方法请往下看==============>
from rest_framework.viewsets import ModelViewSet
class Students_ListModelMixin(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = ModelSerializerAPIViews

    
    
from rest_framework.viewsets import ReadOnlyModelViewSet
class Students_ListModelMixin(ReadOnlyModelViewSet):
    # 当使用ReadOnlyModelViewSet时,所获得的方法是只读的,也即是说,里面并没有封装修改数据的方法
    queryset = Students.objects.all()
    serializer_class = ModelSerializerAPIViews

# ==================>
	# 路由属性为显示全部数据时的注册方式
	path('students5/',Students_ListModelMixin.as_view({
        'get':'list',
        'post':'create'
    })),
    #当需要使用路由获取参数时的方式
    re_path(r'students5/(?P<pk>\d+)/',Students_ListModelMixin.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
	# 确切的书,在as_view中,你需要将访问方式同函数绑定起来,确保你在访问时将会执行对应的方法
    # 访问方式与方法的绑定一般整合为一个字典形式传入视图类
    

```



------

### 在视图函数函数类中调用多个序列化器

```python
from rest_framework.viewsets import ModelViewSet
from .serializer import CuressInfo,ModelSerializerAPIViews
class StudentsModelViewSet(APIView):
    queryset = Students.objects.all()
    serializer_class = ModelSerializerAPIViews
    # 重写get_serializer_class方法,在其中添加判断,如果对应的访问方式,就返回需要用到的序列化器
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModelSerializerAPIViews
        else:
            return CuressInfo
    
    def get(self,request):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance=instance,many=True)
        
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_excaption=True)
        return Response(serializer.data)
        
        
        
        
class StudentsModelViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = ModelSerializerAPIViews
    # 重写get_serializer_class方法,在其中添加判断,如果对应的访问方式,就返回需要用到的序列化器
    def get_serializer_class(self):
        #在视图集函数中,使用的并不是self.request.method进行判断,而是self.action
        if self.action == 'list':
            return ModelSerializerAPIViews
        else:
            return CuressInfo
    
    def get(self,request):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance=instance,many=True)
        
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_excaption=True)
        return Response(serializer.data)
```

