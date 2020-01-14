[TOC]



# bs4安装配置:

1. ```python
   pip install bs4
   # 在终端中下载bs4解析库
   pip install lxml
   # 在终端中下载lxml库
   ```

1. 创建解析对象

2. ```python
   from bs4 import BeautifulSoup
   
   f = open('../day01/baidu.html','r',encoding='utf8')
   
   soup = BeautifulSoup(f,features='lxml')
   
   print(soup.div)
   ```

3. 要注意的是,soup.TagName返回的是第一个对应的标签的内容,

4. ```python
   from bs4 import BeautifulSoup
   
   f = open('../day01/baidu.html','r',encoding='utf8')
   
   soup = BeautifulSoup(f,features='lxml')
   
   print(soup.find('div'))
   ```

5. soup.find('TagName')所返回的,同样是第一个元素,其效果和soup.TagName基本相同

6. ```python
   from bs4 import BeautifulSoup
   
   f = open('../day01/baidu.html','r',encoding='utf8')
   
   soup = BeautifulSoup(f,features='lxml')
   
   print(soup.find('div',class_ = 'op-short-video-pc-poster c-span6'))
   ```

7. find方法的属性:class_ 设定的是目标的class名,只有符合条件的TagName才能被查询出来

8. ```python
   from bs4 import BeautifulSoup
   
   f = open('../day01/baidu.html','r',encoding='utf8')
   
   soup = BeautifulSoup(f,features='lxml')
   
   print(soup.find_all('div',class_ = 'op-short-video-pc-poster c-span6'))
   ```

9. find_all的用法和find基本相同,但是返回的数据格式是一个列表,并且返回的是所有符合条件的数据,而不是第一个

10. ```python
    from bs4 import BeautifulSoup
    
    f = open('../day01/baidu.html','r',encoding='utf8')
    
    soup = BeautifulSoup(f,features='lxml')
    
    print(soup.select('.opr-recommends-merge-content'))
    ```

11. select方法的用法,参数为选择器,支持标签选择器,层级选择器,id选择器,类选择器

12. ```python
    from bs4 import BeautifulSoup
    
    f = open('../day01/baidu.html','r',encoding='utf8')
    
    soup = BeautifulSoup(f,features='lxml')
    
    print(soup.select('.opr-recommends-merge-content > div > a'))
    ```

13. 层级选择器写法,使用 > 来指向下一级元素

14. 层级选择器如果需要定位子类的子类的话,可以不写 >

15. ```python
    from bs4 import BeautifulSoup
    
    f = open('../day01/baidu.html','r',encoding='utf8')
    
    soup = BeautifulSoup(f,features='lxml')
    
    print(soup.select('.opr-recommends-merge-content a'))
    ```

16. 以上为不指向性获取包含的内容

17. ```python
    from bs4 import BeautifulSoup
    
    f = open('../day01/baidu.html','r',encoding='utf8')
    
    soup = BeautifulSoup(f,features='lxml')
    
    print(soup.select('.cr-title,.c-clearfix span')[0].span.string)
    
    
    -------------------------------------------------------------
    from bs4 import BeautifulSoup
    
    f = open('../day01/baidu.html','r',encoding='utf8')
    
    soup = BeautifulSoup(f,features='lxml')
    
    print(soup.select('.cr-title,.c-clearfix span')[0].span.text)
    ```

18. text与string均可获取标签中的文字内容

19. text获取的是标签中所有的文本内容,

20. string获取的是标签中的直系文本内容以外的内容无法获取

21. "我的奴隶的奴隶,不是我的奴隶"

22. ```python
    from bs4 import BeautifulSoup
    
    f = open('../day01/baidu.html','r',encoding='utf8')
    
    soup = BeautifulSoup(f,features='lxml')
    
    print(soup.select('.cr-title,.c-clearfix span')[0].a['class'])
    print(soup.find('div',class_ = 'op-short-video-pc-poster c-span6').a['class'])
    print(soup.find_all('div',class_ = 'op-short-video-pc-poster c-span6')[0].a['class'])
    ```

23. 通过定位获取属性值

