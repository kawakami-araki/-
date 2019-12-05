# DRF验证器机制

1. 创建基于drf框架的验证器

   1. ```python
      from rest_framework import serializer
      class SerializerStudents(serializer.Serializer):
          name = serializer.CharField(max_length=10,min_length=2)
      ```

   2. 在创建好的视图类中使用这个验证器类

      ```python
      class Students(View):
          def post(self,request):
              #获取客户端传输过来的json数据并进行解码操作
              data_string = request.body.decode()
              #导入json模块
              import json
              #使用json模块的方法对获取到的字符串进行转换,变成一个字典
              data_dict = json.loads(data_string)
              #使用创建好的验证器类
              from .serializer import SerializerStudents
              serializer = SerializerStudents(data=data_dict)
              #验证器类的is_valid方法返回的数据为bool数据,当通过验证时,返回结果为true,否则返回false
              print(serializer.is_valid())
              #is_valid方法的属性为raise_excaption
              #这个属性默认时关闭的,当他开启时,意味着当验证出错时,将会直接报错,并直接停止代码的继续运行,
              print(serializer.is_valid(raise_exception=True))
              #返回报错信息,这个并不会阻止程序的继续运行
              print(serializer.erreo_messages)
              #
              
      ```

2. 创建一个验证器方法进行验证

   1. 单字段验证

      - ```python
        def validate_name(self,data):
            #传入的参数可以直接设定为data
            if data == 'root':
                raise serializer.ValidationError(message='用户名不能为root')
                #当满足条件时,返回错误原因和信息
            return data
        	#当通过验证时,返回原数据data
        ```

   2. 全局字段验证

      - ```python
        def validate(self,data_dict):
            #验证方法和单字段验证基本相同,区别是传入的数据类型是字典,进行判断是只需要从字典中取出对应的值即可进行判断,要注意的是,最终依然要将这个数据返回回去
            name = data_dict.get('name')
            password = data_dict.get('password')
            
            return data_dict
        ```

3. 创建一个验证器类外部的方法进行使用

   1. 在验证器类外部进行函数定义

      - ```python
        def check_validate(data):
            if data=='user':
                raise serializer.ValidationError(message='不能使用user作为用户名')
            return data
        ```

   2. 在验证器类中定义字段属性时使用

      - ```python
        name = serializer.CharFIeld(max_length=20,min_length=2,validates=[check_validate])
        ```

4. 在验证器类中重写create(添加一条数据)方法和update(修改一条数据)方法

   1. 重写create方法

      - ```python
        def create(self,validate_data):
            name = validate_data.get('name')
            instance = Students.objects.create(
            	name=name
            )
            return instance
        ```

   2. 重写update方法

      - ```python
        def update(self,instance,validate_data):
            name = validate_date,get('name')
            instance.name = name
            instance.save()
            return instance
        ```

   3. 使用这两种方法

      1. 通用的激活方法

         - ```python
           serializer.save()
           ```

         - 通过验证之后的数据,可以使用方法save()

      2. create可以直接使用,当验证时传入的参数仅有一个data时,将会调用create方法,而不会激活update方法

      3. 使用update方法

         1. ```python
                def update(self, instance, validated_data):
                    name = validated_data.get('name')
                    curess = 1
                    instance.name = name
                    instance.curess_id = curess
                    instance.save()
                    return instance
            ```

         2. ```python
            class stdSl(View):
                def put(self,request,id):
                    instance = Students.objects.get(id=id)
                    import json
                    data_dict = json.loads(request.body.decode())
                    serializer = Students_Serializer(instance=instance,data=data_dict)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return HttpResponse('ok')
            ```

            

## 以上内容为serializer.Serializer组件的使用,相比较起来,drf框架中其实已经封装好了专用的模型类序列化器

------

### serializer.ModelSerializer:

- 







------

## 验证器使用时的属性和字段:

- 
- 

