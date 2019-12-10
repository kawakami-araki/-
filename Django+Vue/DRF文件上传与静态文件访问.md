# DRF文件上传及访问

## 关于DRF文件上传:

​	其实我的掌握并不强,目前也只能完成非前后端分离的状态提交的数据,在前后端分离的状态,我提交的数据不知道为什么始终无法传上来,查验代码之后提示是我的上传数据格式不一致,但是查了好久都没找到具体的解决办法

​	那么,先演示一下使用drf进行的django工程内部的提交:

​		

```python
class imgCal(ModelViewSet):
    queryset = imageInfo.objects.all()
    serializer_class = StudentsSerializer
    #重写get方法,确保在进行get访问时获取进行文件上传的模板
    def get(self,request):
        return render(request,'./imgfrom.html')

	#在这里,我选择了重写ModelViewSet中自带的create方法,并将其更名为post
    #模板自带的create方法所获得的request.data并不是表单直接提交的数据,因为个人原因(其实就是懒)我将request.data方法改掉,改为使用表单的方式获取数据,然后存储到一个字典之中,
    def post(self, request, *args, **kwargs):
        # 创建一个新的字典
        a_dict = {}
        # 获取上传的文件,并存储到创建的字典中去
        a_dict['name'] = request.POST.get('name')
        a_dict['img'] = request.FILES.get('img')
        # 最后得到的,是这样一个集合
        # < QueryDict: {'name': ['小小'], 'img': ['C:\\fakepath\\003.png']} >
        print(request.GET)
        # 创建序列化器对象,将床架你的字典作为data放入序列化器
        serializer = self.get_serializer(data=a_dict)
        print(serializer.is_valid())
        # create方法原生的使用方法,转到下一个类方法中
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 将最终结果返回回去,不需要修改
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # 对序列化器结果进行判断,这里加不加都可以,之所以加上这层判断,只是我在书写过程中,为了确保结构完整,并且能够在每一个位置进行判断,确定bug位置而书写的
        #当序列化通过时,执行save
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # 当序列化未通过时,将会执行以下数据
        else:
            print('数据无效',serializer.data)
            return Response(serializer.data)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
```

以下是序列化器部分:

```python
class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = imageInfo
        fields = '__all__'
```

平平无奇的序列化器,没有添加什么额外的配置要求

值得一提的是,在数据库中我并不是使用的imageFields,而是使用了兼容性感觉更高的filefield

下面是数据库配置:

```python
def upload_to(instance, fielname):
    return '/'.join([settings.MEDIA_ROOT, instance.user_name, fielname])
#以上代码是自己重写的文件下载模块,已弃之不用

class imageInfo(models.Model):
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to='')
    # 必备参数,upload
    # 如果你不需要再设定好的下载路径中再次准备一个文件夹进行文件存储,可以直接为空,即: upload=''
    # 当然,在使用之前,需要准备好MEDIA_URL以及MEDIA_ROOT,如果想要在网页中能直接通过网址进行蹄片查看,需要配置好meida路由

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'imageinfo'
```

以下是路由配置:

```python
re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),


#setting文件配置

MEDIA_URL = 'static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static\media')


```

在完成上述的代码之后,只需要配置好模板文件即可,正常的form表单的提交方法,后台的代码将会自行对获得的数据进行解析存储