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

