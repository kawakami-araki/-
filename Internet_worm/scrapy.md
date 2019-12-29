# scrapy:

- 什么是框架?
  - 继承了各种功能且具有很强通用性(可以被应用在各种不同的需求中)的一个项目模板
  - 我们需要做的就是学习怎么使用这些框架的功能

- scrapy框架集成的功能有哪些?
  - 高性能的数据解析操作
  - 高性能的数据下载操作
  - 持久化数据存储

- scrapy通常只用于get请求,并不适用于post请求的模拟登陆

- scrapy环境安装
  1. pip install wheel
  2. pip install twisted
     - [twisted下载](https://pypi.org/project/Twisted/#files)
  3. pip install pywin32
  4. pip install scrapy

- 开始创建scrapy工程
  - 进入终端输入指令创建新的scrapy工程
  - ‘scrapy startproject projectname’
  - 按照指令创建新的爬虫文件 
  - scrapy genspider spiderName www.xxx.com
  - 启动爬虫程序
    - scrapy爬虫不能直接运行,
    - 在命令窗口中输入指令
    - scrapy crawl spiderName
      - scrapy crawl spiderName --nolog
      - 运行时不输出日志信息
      - 在setting文件中添加配置
      - LOG_LEVEL= ‘ERROR'’
      - 当发生错误时,将错误日志输出,方便调试

- scrapy工程设置--—–-setting

  - User_Agent    这里设置的是爬虫的请求头
  - ROBOTSTXT_OBEY = True   这里设置的是robots协议,当值为True时,爬虫将会在运行时优先查看robots协议,如果协议不允许将不会进行爬取

- scrapy工程使用

  - 构建解析

  - ```python
    # -*- coding: utf-8 -*-
    import scrapy
    class NewSpiderSpider(scrapy.Spider):
        # 爬虫文件的名称,相当于爬虫文件的唯一标识
        name = '💀'
        # 循序的域名, 通常情况下不会使用
        # allowed_domains = ['www.baidu.com']
        # 起始的url列表, scrapy将会对列表中的url自动进行请求发送
        start_urls = ['http://www.budejie.com/']
    
        def parse(self, response):
            # 在scrapy中,数据解析不需要手动导入etree来进行,相对的,这里面集成了etree 的功能,也就是说,我们可以直接使用scrapy的集成来达到我们进行数据解析的目标
            # 这个功能的使用方式如下
            res = response.xpath('//div[@class="j-r-list-c-desc"]/a/text()').extract()
            # extract方法,提取获取到的selected对象中的data数据,当对象为单个对象的时候,获取到的对象就是单个的字符串,
            # 当提取到的selected对象为list对象时,获取到的数据也会自动变成一个列表,并不需要循环遍历selected列表来进行提取
            for i in res:
                print(i)
    ```

- scrapy持久化存储

  - 基于终端窗口的持久化存储

    - 特性:只可以将parse方法的返回值写入到本地的磁盘文件中

    - 指令: scrapy crawl spiderName -o filePath

    - ```python
          def parse(self, response):
              li_list = response.xpath('//div[@class="j-r-list"]/ul/li')
              all_data = []
              for li in li_list:
                  author = li.xpath('./div[1]/div[2]/a/text()').extract()[0]
                  content = li.xpath('./div[2]/div[1]/a/text()').extract()[0]
                  dic = {
                      'Author': author,
                      'Content': content
                  }
                  all_data.append(dic)
              return all_data
      # scrapy 将会对parse的返回值进行处理,并预置了内部的持久化存储模块.这个持久化存储基于命令终端运行,该选项不支持txt文件存储,目前仅支持('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')这七种文件
      ```

    - 

  - 基于管道的持久化存储

    - 管道话存储需要使用scrapy中封存的一些方法,同时需要进行一些处理,这样的存储方式支持txt文档存储

    - 管道文件存储示例:

    - ```python
      class FirstblodPipeline(object):
          fp = None
          # 设定在管道运行开始之前优先运行的代码
          def open_spider(self, spider):
              print('爬虫开始运行~~~~~~~')
              # 通过在管道运行开始之前打开文件的形式来确保这个文件每次只需要打开一次
              self.fp = open('./firstBlod/spiders/all_data.txt', 'w', encoding='utf-8')
      
          # 当数据被提交时执行的代码,在这里进行数据持久化存储
          def process_item(self, item, spider):
              author = item['author']
              content = item['content']
              # 调用已经打开的文件,并在里面进行写入操作
              self.fp.write(author + ':' + content + '\n')
              # 将item转交给下一个管道类
              return item
          # 当管道关闭时执行的代码
          def close_spider(self, spider):
              print('爬虫结束运行~~~~~~~')
              # 在代码整体运行结束的时候,关闭打开的文件
              self.fp.close()
      
      ```

    - item文件对象实例

    - ```python
      class FirstblodItem(scrapy.Item):
          # define the fields for your item here like:
          # name = scrapy.Field()
          # 构建新的item对象中的参数
          # 格式为    name = scrapy.Field()
          # 使用field文件格式的时候,兼容几乎所有的文件类型
          # 包括但不仅限于   列表,元组,字典,字符串,数字,二进制流等各种各样的形式
          author = scrapy.Field()
          content = scrapy.Field()
      ```

    - settings文件实例

    - ```python
      # Configure item pipelines
      # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
      ITEM_PIPELINES = {
         'firstBlod.pipelines.FirstblodPipeline': 300,
          # 管道对象的名字,后面的数值为管道优先值
          # 优先值高的将会优先执行
          # 数值越低优先值越高
      }
      ```

    - 找到管道相关代码进行激活

    - 在爬虫文件中进行使用

    - ```python
      import scrapy
      from firstBlod.items import FirstblodItem
      # 导入item设定类
      class NewSpiderSpider(scrapy.Spider):
          name = '💀'
          start_urls = ['http://www.budejie.com/']
      
          def parse(self, response):
              li_list = response.xpath('//div[@class="j-r-list"]/ul/li')
              # all_data = []
              for li in li_list:
                  author = li.xpath('./div[1]/div[2]/a/text()').extract()[0]
                  content = li.xpath('./div[2]/div[1]/a/text()').extract()[0]
                  item = FirstblodItem()
                  # 实例化item对象
                  item['author'] = author
                  item['content'] = content
                  # item使用方法和字典类似
                  # 使用yield方法返回封装完成的item对象
                  # 当使用yield返回的时候,将会自动将item传输到管道对应的接受类中,进行处理并持久化存储
                  yield item
      ```

    - 将上述条件准备完毕之后,就可以进行数据的持久化存储了

    - 当然,也不一定非要存储到文件中去,毕竟还有一些涉及到数据库的存储,都可以放到这个管道中来进行

    - 也就是,管道文件中的一个管道类负责一种持久化存储的方案

    - item提交的时候将会把item交给优先级最高的管道类

    - 在管道类中,return item的作用是将item转交给下一个管道类

    - 双管道类写法以及Mysql数据库写入

    - ```python
      class MysqlPip(object):
          conn = None
          cursor = None
      
          # 设定在管道运行开始之前优先运行的代码
          def open_spider(self, spider):
              # 通过在管道运行开始之前打开文件的形式来确保这个文件每次只需要打开一次
              print('爬虫2开始运行~~~~~~~')
              # 建立数据库游标
              self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='000000',db='spider',charset='utf8')
              print(self.conn)
          # 当数据被提交时执行的代码,在这里进行数据持久化存储
          def process_item(self, item, spider):
              author = item['author']
              content = item['content']
              sql = 'insert into bs values ("%s","%s")'% (author,content)
              print(sql)
              self.cursor = self.conn.cursor()
              try:
                  self.cursor.execute(sql)
                  self.conn.commit()
              except Exception as e:
                  print(e)
                  self.conn.rollback()
              print('----------------------------------------------------------------------------')
              return item
          def close_spider(self, spider):
              print('爬虫2结束运行~~~~~~~')
              self.cursor.close()
              self.conn.close()
      ```

  - 手动发送请求:

    - 手动发送get请求

      - 应用场景:   请求同一个主页面下的多个页面

      - 代码

        ```python
        # -*- coding: utf-8 -*-
        import scrapy
        from firstBlod.items import FirstblodItem
        
        class NewSpiderSpider(scrapy.Spider):
            # 爬虫文件的名称,相当于爬虫文件的唯一标识
            name = 'new_spider'
            # 循序的域名, 通常情况下不会使用
            # allowed_domains = ['www.baidu.com']
            # 起始的url列表, scrapy将会对列表中的url自动进行请求发送
            start_urls = [
                'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=',
                ]
            # 设置基本的url模板
            url = 'https://www.zhipin.com/c101010100/?query=python&page=%d&ka=page-%d'
            # 记录页数
            page_name = 1
        
            def parse(self, response):
                li_list = response.xpath('//div[@class="job-list"]')
                print(li_list)
                # all_data = []
                for li in li_list:
                    # 职位名称
                    Job_title = li.xpath('./div/div[1]/h3/a/div[1]/text()').extract()[0]
                    # 公司名称
                    Corporate_name = li.xpath('./div/div[1]/a/text()').extract()[0]
                    # 地址
                    all_address = li.xpath('./div/div[1]/p//text()').extract()[0]
                    # 经验 experience
                    # address,experience,Education = all_address.split('|')
                    #学历 Education
                    # dic = {
                    #     'Author': author,
                    #     'Content': content
                    # }
                    # all_data.append(dic)
                    item = FirstblodItem()
                    item['Job_title'] = Job_title
                    item['Corporate_name'] = Corporate_name
                    yield item
                # 确定当前页数,
                if self.page_name <= 5:
                    self.page_name += 1
                    # 拼接新的url
                    new_url = format(self.url%(self.page_name,self.page_name))
                    # 使用yield进行请求,参数callback为处理这些页面信息所用的函数,可自行设定,也可用递归的方式使用当前的函数
                    yield scrapy.Request(new_url,callback=self.parse)
                else:
                    return li_list
        ```

      - 重写父类的自动请求方法

        ```python
        # 重写父类方法意味着我们可以自定义数据清洗函数,而不需要局限于parse
        def start_requests(self):
        	for url in self.start_urls:
        		yield scrapy.Request(url,callback=self.parse)
        ```

      - 要想使scrapy自动发送get请求,需要重写start_requests方法

    

    ## scrapy图片处理:

  1. 在scrapy中,有着专门的模块对图片数据进行请求以及处理,我们只需要将获取到的图片url以item的形式传输到我们的管道之中进行处理即可,item对象的创建于寻常的创建方法没设么区别,scrapy.Fields包容性极强,不需要考虑兼容性问题,

  2. 在提交到管道中去之后,我们可以在管道之中对item中的数据进行处理,

  3. 使用scrapy中封装的图片处理专用类scrapy.pipelines.images import ImagePipeline

  4. 创建一个新的管道类,这个管道类继承自ImagePipline

  5. ```python
     class ImgSpidersPipeline(ImagesPipeline):
     
         # 对一个图片链接进行请求发送
         # item 就是scrapy提交过来的item数据
         def get_media_requests(self, item, info):
             yield scrapy.Request(item['src'])
     
         # 准备文件名
         def file_path(self, request, response=None, info=None):
             file_name = request.url.split('/')[-1]
             print('正在下载',file_name,'............')
             return file_name
         # 将item传递给下一个即将执行的管道类
         def item_completed(self, results, item, info):
             return item
     ```

  6. 完成这些之后,我们还需要对图片的存储路径进行设置,在setting文件中添加新的属性

     - IMAGES_STORE = “imagePath”

     - imagePath自行设置,最好设置为绝对路径,如果使用相对路径的话,最好参考django中的文件路径的写法,先确定工程的路径,然后再在工程路径的基础上设定相对路径

     - django方法设置路径如下:

     - ```python
       import os
       # 获取当前文件夹的主路径
       BASE_DIR = os.path.dirname(os.path.abspath(__file__))
       # 将要添加的图片文件保存路径加入到主路径中去
       IMAGES_STORE = os.path.join(BASE_DIR,'imgsLib')
       ```

     - 这个方法同样设置在settings文件中

  7. 完成这些之后,只需要在settings中将写好的管道类进行注册,即可开始这个管道类

  8. 运行爬虫程序,将会开始全自动下载选中的图片,根据之前学过的方法,即设定网址的基础模板,即可实现图片的批量下载



## 如何提高scrapy爬虫的效率

  1. 增加并发数量
     - CONCURRENT_REQUESTS = 32
     - 默认并发数量为32
     - 可以自行设置
  2. 降低日志等级
     - LOG_LEVEL = "INFO"
     - LOG_LEVEL = "ERROR"
  3. 禁止cookie
     - COOKIES_ENABLED = False
     - 在scrapy中会自动对cookie进行处理,不管这个页面是否需要验证cookie
     - 将cookie处理模块进行关闭,将会提升scrapy的执行效率
  4. 禁止重试
     - scrapy将会自动对失败的请求进行重试,这严重影响到了爬虫的执行效率,可以将重试功能禁掉,从而提升执行效率
     - 在settings文件中书写代码
     - RETRY_ENABLED = False
     - 当请求失败的时候,scrapy将不会去处理请求失败的数据,而是会直接跳过进行下一条
  5. 减少下载超时
     - DOWNLOAD_TIMEOUT = 10
     - 写入这段代码,作用是设定请求超时的时间,也就是说,当你在亲求时间超过了十秒的时候依然没有拿到数据的话,将会结束请求,执行下一项,而不是一直等待下去,这个熟知的单位是秒
## 请求传参:

- 基于请求传参可以实现深度爬取





## 中间件:




