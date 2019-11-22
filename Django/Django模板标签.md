# Django模板使用

1. ```
   {% for foo in msg %}
       {{ forloop.counter }}
   {% endfor %}
   ```

   - for循环中可以使用forloop.counter获取当前循环的次数

2. ```
   {% if books %}
   
   {% else %}
       
   {% endif %}
   ```

   1. if循环,包括elseif与else

## 模板注释

单行注释:

```
{#  注释的内容  #}
```

多行注释:

```
{% comment %}
注释的内容
{% endcomment %}
```



## 过滤器:

1. default

   - 

2. length

   -  

3. date

   - 默认时间显示格式为美式

   - ```
     dete:'Y年-m月-d日'
     ```

   - 通过过滤器可以将时间格式转化为想要的状态

   - safe,关闭自动转义

   - autoescape标签关闭转义

     - ```
       {% autoescape %}
       模板内容
       {% endautoescape %}
       ```

   - 模板硬编码不会进行转义

### 自定义过滤器:

1. ​	在应用下新建templatetags文件夹,此文件夹名为固定名称,不可自定义

2. ​        在文件夹中创建一个py文件用来存放自定义过滤器

   - ```python
     from django.tempalte import Library
     #创建一个实例化Library对象
     register = Library()
     
     #创建一个过滤器函数
     @register.filter
     def mod(num):
         return num %2 == 0
     ```

3. 在模板中导入这个过滤器文件

   - ```
     {% load filters %}
     #在这里进行的模块导入只需要将过滤器文件的名字导入进去就可以直接进行使用了
     ```

### 一个坑:

​	自定义过滤器时,创建出来的library对象的名字必须是register

​	目前还不明白原因,但是使用了library之后会出现无法查询到filters模板的问题,

#### 	自定义过滤器时最少需要有一个参数传入,最多两个