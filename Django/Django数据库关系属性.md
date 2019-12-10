# 数据库关系属性

- ## 一对多关系

  - ForeignKey

  - 外键专属,一对多关系设定,通常情况下,这个属性设置在多类属性中,关联一类属性

  - ```python
    news_type = models.ForeignKey('NewsTypeInfo',on_delete=models.CASCADE)
    ```

    

- ## 多对多关系

  - ManyToManyField

  - 多对多关系建立字段,这个字段可以写在任意一个里面,并不影响使用

  - ```python
    news_type = models.ManyToManyField('NewsInfo')
    ```

  

- ## 一对一关系

  - OneToOneField





# 通过模型类实现关联查询语句:

​	

```python
from Two.models import *
b = HeroInfo.objects.filter(hbook__id=1)
#通过一对多关系获取对象的方法
#关系字段加上双下划线加上对应表中的字段即可进行查询,但需要注意
b = HeroInfo.object.get(id=1)
b.hbook
#以上两种方法都能进行查询,但是第一种方法查询出来的结果是一个查询集,第二种拿到的是一个对象
```

在没有关系的情况下查询的话,就不能使用关系属性字段进行查询,这个这时候,就需要用模型类的名字进行查询,用模型类的名字代替关系属性字段的名字





# 自关联属性字段查询:

### 	设定自关联属性字段:

​			

```python
class AreaInfo(models.Model):
	a_title = models.CharField(max_length=20)
    #设置关联属性字段,关联自身,即self
    #这个字段即意味着与自身关联
    a_parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
```

#### 自关联属于特殊的一对多

#### 在查询时遵循一对多的查询方式

由一查多时使用字段名__set.all()进行查询

由多查一时使用字段名查询

