# 模型管理器详解

1. ## objects模型管理器

   1. 本质上来说,objects其实是django为我们封装的一个特殊的模型管理器类,它本质上其实是models.Manager对象

   2. 也就是说,我们可以通过重写models.Manager的方法来实现给这个管理器进行重命名

   3. 如:

      1. ```python
         #在模型类属性之中直接重写models.manger方法
         book = models.manger()
         #自定义一个管理器对象,这之后我们就可以不适用objects来进行查询
         #而是使用book来进行查询
         BookInfo.book.all()
         #在进行定义之后,将无法使用原本的objects
         ```

2. ## 常用的重写模型管理器方法

   1. 创建一个模型类来进行重写

      1. ```python
         class BookInfoManger(models.Manager):
             pass
         ```

      2. 这是最简单得到重写Manager的方法

      3. 通过这个类可以创建全新的Manager对象来进行查询

      4. 注意,一旦进行重写之后,django自带的objects将会无法使用,只能使用自己创建的对象进行查询

   2. 在模型类之中进行其他的编写

      1. 重写all方法(改变结果集)

         - ```python
           def all(self):
               #通过super方法调用父类的all方法对模型类对象进行查询
           	books = super().all()
               #对处理过的结果进行处理
               books = books.filter(id__gt=1)
               #将结果返回
               return books
           ```

         - 这样处理过的all方法在调用时将不会返回全部的数据,而是会根据这个重新定义的all方法对数据进行处理之后才会返回,

         - 最终返回结果为

           ```python
           >>> BookInfo.a.all()
           >>> <QuerySet [<BookInfo: 神墓>, <BookInfo: 龙蛇演义>, <BookInfo: 那年那兔那些事儿>, <BookInfo: 亮剑>, <BookInfo: 秒速五厘米>, <BookInfo: 你的名字>]>
           
           ```

           返回结果为一个返回集

      2. 自定义类方法(定义额外的方法)

         - 在这里我们可以自定义一些方法,比如自定义一些添加用的方法,也即是说,把原本复杂的添加方法封装成为类方法进行使用,这样的话,可以减少代码的数量

         - 重写字段添加

           - ```python
             @classmethod
             def create_book(cls,btitle,bpub_date,cate_id):
                 obj = BookInfo()
                 obj.btitle = btitle
                 obj.bpub_date = bpub_date
                 obj.cate_id = cate_id
                 obj.save()
                 return obj
             ```

           - 重写添加信息方法

           - 在模型类中的写法,此方法不适合写在模型类中,因为过多的类方法会使模型类变得臃肿,不方便使用,所以我们一般将这些方法定义在我们重写的manager模型管理器中

           - ```python
             def create_book(self,btitle,bpub_date,cate_id):
                 obj = BookInfo()
                 obj.btitle = btitle
                 obj.bpub_date = bpub_date
                 obj.cate_id = cate_id
                 obj.save()
                 return objpython
             ```

           - 这两种方法都可以使用,

           - 重写封装的方法适用于增删改查的所有方法

           - 在manager函数中,封装好了一个model方法,这个方法返回的是调用这个方法的模型类

             ```
             self.model()
             ```

             使用这个方法之后,就不会出现换一个模型类就无法调用的情况了