# xpath模块使用:

1. ## 安装模块:

   1. ```
      pip install xpath
      pip install lxml
      ```

2. 开始使用

   1. ```python
      from lxml import etree
      # 从lxml导入etree包
      res = etree.parse('./baidu.html',parser=etree.HTMLParser(encoding="utf-8"))
      # 创建新的etree实例
      # 第一个参数为要匹配的文件
      # 第二个参数为要使用的编码方式
      # etree.HTMLParser(encoding='utf-8)
      
      # xpath表达式的使用方式
      # 1-标签匹配
      result_1 = res.xpath('//body/div')[0]
      # 2-索引匹配
      # 索引定位时的索引并不是从0开始,而是从1开始的
      result_2 = res.xpath('//body/div[1]')
      # 3-属性匹配
      result_2 = res.xpath('//body/div[@class="song"]')
      result_2 = res.xpath('//body/div[@id="song"]')
      
      print(result_1)
      print(result_2)
      ```

   2. 要注意的是,xpath使用时需要传入要使用的编码方式,详情请看上方的代码块

   3. ```python
      result_2 = res.xpath('/html/body/div')
      # 层层定位的标签属性,并不局限于三层
      # 用这种方法进行定位传回的数据将会精确到单个目标,
      
      result_2 = res.xpath('//body/div')
      # 使用两个//将会进行全局匹配,并不在局限于精确的目标,也就是说的,结果返回的数据不一定是head标签中的数据,也不一定是是body中的数据,这样匹配的将会是全局的数据
      
      result_2 = res.xpath('/html/body/div[1]')
      # 使用索引后返回的,将会是对应索引位置的数据
      
      result_2 = res.xpath('//div[1]')
      # 使用//与索引返回的,是全局中每一个大标签中所有符合条件的数据之中的第一个
      
      # 和正常python中的索引概念不同的是,这里索引并不是从0开始进行计算的 ,而是从开始计算的
      # 也就是说,res.xpath('//div[1]')等同于res.xpath('/html/body/div')[0]
      
      result_2 = res.xpath('//div[1]/text()')
      # 获取数据中的直系文本信息
      # 这里的text不同于在python中,需要加上()
      
      result_3 = res.xpath('//div[1]//text()')
      # //获取的是全部的文本内容
      
      result_2 = res.xpath('//a[1]/@href')
      # @+属性名,获取对应属性的值
      
      
      ```

   4. 使用xpath直接从获取到的网页中提取数据

   5. ```python
      from lxml import etree
      #
      # res = etree.parse('./baidu.html',parser=etree.HTMLParser(encoding="utf-8"))
      # result_2 = res.xpath('//a/text()')
      # result_2 = res.xpath('//a[1]/@href')
      #
      # print(result_2)
      
      
      from requests import Session
      session = Session()
      url = 'https://www.baidu.com/s'
      Headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
      }
      params = {
          "wd" : '666'
      }
      
      response = session.get(url=url,params=params,headers=Headers)
      response.encoding = 'utf8'
      # 上述为正常的获取页面过程
      
      est = etree.HTML(response.text)
      # 创建etree对象
      # 这里使用的解析方式不再是parse,而是使用HTML
      # parse的使用场景为,对文件类型的数据进行解析
      a_list = est.xpath('//a//text()')
      print(a_list)
      ```

   6. 当使用xpath匹配到的对象的时候,同样可以使用xpath方法

   7. ```python
      # 当使用匹配到的对象的时候
      
      
      li_list = est.xpath('//div//li)')
      a_list = []
      for li in li_list:
          a_list += li.xpath('./div/a')
      for a in a_list:
          href = a.xpath('./@href')
          print(href)
      
      # 当进行第二次xpath时,匹配的公式为'./tagName'
      # ./意味着从当前的对象的下面开始匹配,将这个对象作为根节点,而不是html
      # 如果在这里使用//tagName,则意味着还是从html标签开始进行匹配
      
      ```

   8. last()函数

   9. ```python
      li_list = est.xpath('//div//li[last()])')
      # last()在xpath中的意思是最后一个,当然,
      
      li_list = est.xpath('//div//li[last()-1])')
      # last()-1就是倒数第二个
      
      ```

   10. contains()

   11. ```python
       # contains()函数,匹配属性值中包含某个值的对象
       ```

   12. postion()

   13. ```python
       li_list = est.xpath('//div//li[postion()>5])')
       # postion()函数,按照范围进行取值
       ```




# 懒加载:

在页面中,设定好的属性中,要求只有当对应的属性被观测到的时候才会变成正常的属性,也就是说,当没有被观测到的时候,都将会是另外一个

在被观测到之前,该属性的存在毫无意义,但当他在页面上的可视化区域出现的时候,将会被激活,并变更为另一种可以使用的形态

我愿称之为量子态

在被可视化页面观测到之前,该属性即存在但又不存在,只有当进入可视化页面的时候,才会发生属性变化,成为存在的数据

而但我们使用requests模块进行球球的时候,对于页面的代码而言,他们仍然处于没有观测的状态,所以,当你想要匹配这种代码的时候,就不能使用正常的做法进行匹配,

而是需要找到在为观测状态下的目标代码,根据其特征进行匹配

俗称---高维干涉

(ˉ▽￣～) 

