# 分页器类书写

1. ```python
   # 废话不多说,直接上代码
   from rest_framework import pagination
   
   class PaginationStudents(pagination.PageNumberPagination):
   	page_size = 5    
   	# 在不传入page_size参数时的默认长度
   	page_size_query_param = 'size'
   	# 设定在使用url传递参数时每页展示数量的参数名
   	page_query_param = 'page'
   	# 设定在使用url传递参数时展示的页数的参数名
   	max_page_size = 5
   	# 设定每页的最大展示数量
       
       
   #注意,在使用分页的时候,可以不传入每页展示数量,默认将会使用设定好的page_size
   ```

2. 创建好分页器类之后,进行使用

   ```python
   from rest_framework.views import ModelAPIView
   class MyPaginations(ModelAPIView):
       queryset = Students.objects.all()
   	serializer_class = MySerializers
       pagination_class = PaginationStudents
       
   ```

3. 使用时的传参方式

   - ```
     127.0.0.1/api/students5/?page=1&size=5
     
     page为页码
     size为单页显示的最大数量
     
     ```

     




​	





