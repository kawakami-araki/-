# Django数据库操作

## #Django中不需要定义id字段

### 数据库创建--基础字段:

- CharField(定义一个字符串类型的字段)

  - max_length=xx,  定义字符串最大长度

- DateField(定义一个时间类型的字段)

  - 时间类型字段一共有三个,TimeField

- BooleanField

- FileField

  - 文件字段

- TextField

  - 大文本字段,超过4000字符的文本使用这个字段

- ImageField

  - 上传图片

- ForeignKey  外键

  - 第一个参数为要关联的模型类

  - ### 第二个参数必须加上下面这个参数,才能保证正确

    ```
    on_delete=models.CASCADE
    ```

  - 在django2.0之后的版本中不在有默认的on_delete,所以这里需要手动传入这个参数

    - ```
      on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
      	on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
      	on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
      	on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
      	# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
      	on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
      	# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
      	on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
      	on_delete=models.SET,         # 删除关联数据,
      	 a. 与之关联的值设置为指定值,设置：models.SET(值)
      	 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
      ```


## 字段属性

- default
- null
  - 判断字段能不能为空
  - 默认为false
- primary_key
  - 主键约束
- Foregin_key
  - 外键约束\
- autoincerment
  - 自增长
- blank
  - 后台出入数据时是否允许为空
- verbose_name
  - 设定字段在管理页面显示的名称

## 插入、更新和删除

#### 插入、更新

​	save()

#### 删除

​	delete



------

## 生成迁移文件

- ```python
  python manage.py makemigrations
  #生成迁移脚本
  ```

- ```python
  python manage.py migrate
  #将迁移脚本映射到数据库之中
  ```



------

## 修改Django数据库默认配置:

```python
#修改setting文件中的database中的参数
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'django_demo',#数据库名称,需要手动创建好数据库
        'USER': "root",	#用户名,默认为root
        'PASSWORD': '000000',#mysql密码
        'HOST': 'localhost',#数据库地址,一般为本机127.0.0.1,通localhost
        'PORT': '3306'#MySQL数据库端口号.默认3306
    }
}

```

------

## 运行整个项目:

```python
python manage.py runserver
```

------

## 通过models文件在数据库中添加数据

```python
python manage.py shell
#进入交互模式

from 模块名.models import 模型类名
from first.models import BookInfo
b = BookInfo()
b.btitle = '天龙八部'
from datetime import date
b.bpub_data = date(1998,3,22)
b.save()
```

## 通过模型类从数据库中获取对应的数据

```python
b1 = BookInfo.objects.get(id=1)
```

#通过模型对象BookInfo的objects方法的get方法获取满足对应条件的字段 

type(b1)

#返回对象是First.models.BookInfo

### 修改表中数据:

```
b1.btitle = '新的数据'
b1.save()
```

从根本上来说,修改数据仅仅只是拿到数据之后重新赋值,然后进行提交而已

```
b1.delete()
```

从数据库中删除这条数据

------

## 外键查询:

- ForeignKey设置外键

- 

  ```python
  from django.db import models
  
  # Create your models here.
  class BookInfo(models.Model):
      #书名
      btitle = models.CharField(max_length=10)
      #上架时间
      bpub_data = models.DateField()
  
  
  class HeroInfo(models.Model):
      #人物名
      hname = models.CharField(max_length=10)
      #人物性别,true为男,false为女
      hgender = models.BooleanField(default=False)
      #简介
      hcomment = models.CharField(max_length=300)
      #人物所属书籍,一对多关系
      #设置外键
      hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
  ```

  - 外键创建好之后的字段名为设定好的models模型里面的外键字段加上_id,这个id和另一个表的id对照

  - ```python
    b = BookInfo()
    b.btitle = '天龙八部'
    from datetime import date
    b.bpub_data = date(1998,2,33)
    b.save()
    #之后添加HeroInfo表的数据
    h = HeroInfo()
    h.hname = '段誉'
    h.hgender = True
    #外键字段赋值为已经创建好的与这条数据关联的bookinfo表对象
    #通过这个字段可以查询到对应表的信息
    h.hbook = b
    
    ###################################################################
    #一对多的情况下查询一的信息
    >>>h.hbook.btitle
    >>>'天龙八部'
    >>>h.hbook.bpub_data
    >>>datetime.date(1998,2,33)
    #一对多查询所属信息
    >>>b.heroinfo_set.all()
    #返回的结果是一个集合,里面以列表形式放置了所有对应的数据
    >>> <QuerySet [<HeroInfo: HeroInfo object (1)>]>
    >>>b.heroinfo_set.first()
    #返回的结果是对应数据的第一条
    >>> <HeroInfo: HeroInfo object (1)>
    #通过将这一条数据赋值之后可以继续进行一些查询
    >>>b1 = b.heroinfo_set.first()
    >>>b1.hname
    >>>"段誉"
    ######################################################
    #查询全部数据
    >>> BookInfo.objects.all()
    >>> HeroInfo.objects.all()
    #模型类名.objects.all()
    ```




## 数据库查询语句

### 条件查询

- all

  - all返回的是一个数据集合
  - 此返回数据可以进行遍历

- filter

  - 返回的结果也是一个集合,可以遍历
  - 属性名__exact = 1
    - 判断是否相等
    - 此项属性等同于id = 1
  - 属性名__contains
    - 查询包含某个字符的数据
  - 属性名__endswith
    - 查询以某字符结尾的数据
    - 以某字符串结尾
  - 属性名__startswith
    - 以某字符串开头
  - 属性名__isnull
    - 查询某字段为空或者不为空的数据
    - 属性名_isnull=false    不为空
    - 属性名__isnull=true   为空
  - 属性名__in = [1,2,3]
    - 查询目标字段再此列表元素的范围内的数据
  - 属性名__gt = 3(gt为大于)
    - 等同于                属性名 > 3
  - 属性名__lt = 3(lt为小于)
    - 等同于                属性名 < 3
  - 属性名__gte = 3(gte为大于等于)
    - 等同于                属性名 >= 3
  - 属性名__lte = 3(lte为小于等于)
    - 等同于                属性名 <= 3
  - 属性名__year
    - bpub_date__year = 1980
    - 查询1980年之后的数据
    - 查询时间信息还可以使用上面的大于等于的方法
      - bpub_date_gt = date(1998,1,1)
      - 查询在1998年1月1日之后的数据

- exclude

  - 返回的结果也是一个集合,可以遍历

  - 查询不满足某个条件的数据

- order_by排序

  - 返回的结果也是一个集合,可以遍历

  - 排序字段一般是放在条件查询之后进行的
  - BackInfo.objects.all().order_by(‘id’)
    - 默认排序方式为升序排列
  - BackInfo.objects.all().order_by(‘-id’)
    - 在前面加个-将会进行降序排列

### 多条件查询

- 两个条件并存
- 与&
  - filter(id_gt=1,age_gt=10)
    - id大于1并且age大于10
- 或  |
  - 这个条件查询需要导入一个新的模块
  - from django.db.models import Q
  - filter(Q(id=1) | Q(age=15))
  - 创建新的Q对象,作为或条件的单位,
- 查询条件为一个字段的数值大于另一个字段的数据
  - 如,查询一本书的阅读量大于评论量的的数据
  - 这个时候需要导入一个新的模块F
    - from django.db.models import F
    - 使用f模块构造对应字段的对象,并将这个对象作为条件进行查询
    - BookInfo.objects.filter(bread_gt=F(bcomment))

### 聚合函数.

##### —-—-聚合操作的关键字:

​	**aggregate**

​	查询时所使用的模块都在django.db.models这个包里面

#### 聚合函数总览

- count该字段的总个数
- max最大数值
- min最小数值
- sum该字段数值的和
- avg平均数值

#### 聚合函数使用时需要导入模块

1. ​	<u>f**rom django.db.models import Count,Max,Min,Avg,Sum**</u>
2. ​	<u>**这五个聚合函数需要从django.db.models里面引入进来**</u>
3. ​	<u>**BookInfo.objects.aggregate(Sum(‘bread’))**</u>
4. ​	<u>**模型类名.bojects.aggregate(聚合函数(字段名))**</u>
5. ​	<u>**当不加查询条件时默认为all,也就是说,all时可以省略的</u>**

##### 当进行聚合之后,返回的值是一个字典,书写形式为,key = 聚合的属性名__聚合方式      ,value = 聚合的结果

#### 聚合函数另一种用法:

在已经进行过条件查询的情况下,直接使用小写的.count()得到的结果时一个数值,这个数值是已经查询到的数据的总数

但是因为条件查询完毕之后获取的是数据集合,所以这个数据集合是没有其他的属性的,他唯一适用的聚合函数只有一个,那就是计算总数的**<u>`count`</u>**

注意,在所有返回的为数据集合的查询语句后面,以上的所有函数都是可以用的,你可以继续在后面使用分类,

所有结果为查询集的结果都是可以进行切片的,[:]

注意,这个切片使用的下标是不允许使用负数的

切片之后的结果依然是一个查询集,可以使用get()方法进行查询

exists()   判断这个查询集中是否有数据,有返回True,没有返回False

existe     相当于查看这个判断并展示这个查询及的全部数据

