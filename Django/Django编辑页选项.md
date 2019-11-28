# Django编辑页选项

1. ## 设定编辑页数据显示

   - 设定显示顺序     fields

     - 这个属性的值是一个字典,字典中将编辑页面的字段按照想要的顺序排列好

     - ```python
       fields = ['username','password']
       ```

   - 设定显示顺序,这个设定是分块设定,即将编辑页分为几个块       fieldsets

     - 这个属性的值是一个元组,元组中包含着元组,并按照里面的元组分成块

     - ```python
       fieldsets = (
       	('名字',{'fields':['username']}),
           #设定块时,元组的第一个值是这个块的名称,第二个值是一个字典,键为   fields  ,值为一个列表,其中保存的是要展示在这个块中的字段
           ('密码',{'fields':['password']})
           #无论如何设定,遵循基本的规则,字典的键都是fields,值都是一个列表
       )
       ```

   - 设定一类模型编辑时显示字类模型数据

     - 第一种:

       - ```python
         class Power_list_StackedInline(admin.StackedInline):
         	model = Basic_information_of_characters
             #model属性的值为这个表对应的多类表的对象
             extra = 3
             #在显示子类的时候留三个空白的字类方便添加和编辑
             
         #将这个类在模型类约束中引入
         Inlines = [Power_list_StackedInline]
         #inlines属性的值是一个列表
         ```

       - 这个类设定的是显示结果是将对应的子类数据划分为一个个的块

     - 第二种

       - ```python
         class Power_list_TabularInline(admin.TabularInline):
         	model = Basic_information_of_characters
         	extra = 3
         ```

       - 从设定方法和使用方法来说,和第一种方法没什么两样,唯一的区别就是继承的对象不一样

       - 这个方法展示出来的子类是以表格形式展示出来的