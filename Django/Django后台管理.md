# Django后台管理操作

#后台管理系统为admin.py文件



## 1).本地化

- ​	修改语言格式

  - 修改为中文:zh-hans

  - ```python
    LANGUAGE_CODE = 'zh-hans'
    ```

- ​	修改时区

  - 修改为中国时区

  - 没有北京的时间,所以我们选择上海

  - Asia/shanghai

  - ```python
    TIME_ZONE = 'Asia/shanghai'
    ```

## 2).创建管理员

- 创建超级管理员

- ```
  python manage.py createsuperuser
  ```

- 使用管理员帐号可以登入后台管理界面进行操作

## 3).注册设定好的模型类

- 在对应文件的amdin文件中注册模型类

  - ```python
    class HeroInfoAdmin(admin.ModelAdmin):
        list_display = ['hname', 'hcomment', 'hbook_id', 'hbook_id']
    #在这里可以设定展示出来的字段总览
    #使用admin模块中的site.register进行注册
    
    admin.site.register(BookCateInfo,BookCateInfoAdmin)
    ```

- 在后台管理界面中想要将每一项数据库中的数据渲染出来需要在模型类中重写__str__方法

  - ```python
    def __str__(self):
        return self.btitle
    #重写str方法,会使这个表渲染在管理界面时的样式改变
    ```

- 在数据库模型中设定方法

  - ```python
    def user(self):
        return self.username
    user.admin_order_field = 'username'
    #为创建的方法字段添加排序属性
    
    user.short_description = '用户名'
    #为创建的方法附加一个别名用于展示
    ```

  - 这个方法适用于自定义模型类的方法时使用

------

### 在注册模型类时可以添加的属性:

- list_display

  - 设定管理页面中娴熟的模型类字段
  - 这个字段可以可以使用模型类中自定义好的方法

- list_per_page

  - 设定管理页面中每页显示的数据量
  - list_per_page = 10(每页展示十条数据)

- action_on_bottom

  - 设定下方的操作框
  - ![1574901352508](C:\Users\lenovo\Desktop\Django\assets\1574901352508.png)
  - 在action_on_bottom = True时,将会在展示页的下方再次增加一个操作框
  - 底部操作框在不设定的时候默认为False

- action_on_top

  - 设定上方的操作框
  - ![1574901605253](C:\Users\lenovo\Desktop\Django\assets\1574901605253.png)
  - 在action_on_top = False时,将会取消展示页上方的操作框,
  - 顶部操作框默认为True

- list_filter

  - 在页面右侧添加快速过滤选项,该选项遵循注册模型类时的约束进行

  - ```python
    list_filter = ['username']
    #这个属性的参数是一个列表,可以在其中添加要过滤的字段名
    #过滤器将会列出所有的字段名方便选择
    ```

- search_fields

  - 在页面顶部添加搜索框

  - ```python
    search_fields = ['username']
    #这个属性的参数是一个列表,可以在其中添加字段
    #在执行搜索时,将会在指定字段的数据中进行匹配
    ```

  - 