# selenium详解：

web自动化测试用的框架，通多代码实现对浏览器的控制，如： 打开网页，点击网页中的元素，实现鼠标滚动等操作



------

- 概念：selenium是一个基于浏览器自动化的一个模块

- 环境安装： 下载selenium模块

- selenium和爬虫之间的关联是什么？

  - 便捷的获取页面中动态加载的数据
  - 实现模拟登录

- 基本操作：

  谷歌浏览器驱动程序下载地址：http://chromedriver.storeage.googleapis.con/index.html

  将下载好的驱动程序放入谷歌浏览器文件包以及python。scripts中

  在系统环境中添加谷歌浏览器

  实例化某一款浏览器对象

  - ```python
    from selenium import webdriver
    # 进行了环境配置之后，可以不写要使用的驱动程序，它会自动调用对应的浏览器驱动程序
    bro = webdriver.Chrome()
    # 指定一个url
    url = 'https://www.baidu.com'
    bro.get(url)
    # 找到要传入的目标的标签
    ```

  - 关于对象捕获

    - ```python
      # xpath方法捕获详情
      from selenium import webdriver
      import time
      es = webdriver.Chrome()
      es.get('https://www.baidu.com/')
      search_input = es.find_element_by_xpath('//input[@id="kw"]')
      
      btn = es.find_element_by_xpath('//input[@id="su"]')
      
      btn.click()
      
      time.sleep(3)
      shouye = es.find_elements_by_partial_link_text('首页')[0]
      shouye.click()
      ```

    - ```python
      # id捕获方法详情
      from selenium import webdriver
      import time
      es = webdriver.Chrome()
      es.get('https://www.baidu.com/')
      # search_input = es.find_element_by_id('kw')
      search_input.send_keys('俺也一样')
      
      # btn = es.find_elements_by_id('su')[0]
      btn.click()
      
      time.sleep(3)
      shouye = es.find_elements_by_partial_link_text('首页')[0]
      shouye.click()
      ```

    - 这两种方法都是精确定位，在没有id的情况下，就可以适当的选择xpath进行捕获

  - selenium执行js语句

    - ```python
      es.execute_script('window.scrollTo(0,document.body.clientHeight)')
      ```

  - 关闭浏览器

    - ```python
      es.quit()
      ```

  ## selenium的爬虫应用，对页面源码进行抽取：

  1. 使用requests时，我们需要考虑浏览器页面的动态加载所带来的差异，这些动态加载的数据在正常情况下无法用requests进行直接获取
  2. 在使用sesnium时，我们所能获得的页面数据实际上就是所有的数据，动态加载得到数据同样会存在于其中，也就是说，selenium对于网页源码的获取更加全面与简便

  

  

  ```python
  from selenium import webdriver
  from lxml import etree
  import time
  import json
  es = webdriver.Chrome()
  es.get(url='https://xueqiu.com/')
  time.sleep(3)
  res_text = es.page_source
  tree = etree.HTML(res_text)
  div_list = tree.xpath('//*[@id="app"]/div[3]/div[1]/div[2]/div[2]/div[1]/div[@class="AnonymousHome_home__timeline__item_3vU"]')
  json_dict = []
  for i in div_list:
      a_dict = {}
      a_dict['title'] = i.xpath('./h3/a/text()')
      a_dict['content'] = i.xpath('./p/text()')[0]
      a_dict['username'] = i.xpath('./div/div/a[@class="AnonymousHome_user-name_3wN"]/text()')[0]
      a_dict['company'] = i.xpath('./div/div/span[1]/text()')[0]
      a_dict['creat_time'] = i.xpath('./div/div/span[2]/text()')[0]
      a_dict['count'] = i.xpath('./div/div[2]/text()')[0]
      json_dict.append(a_dict)
  with open('./xueqiu.json', 'w', encoding='utf-8') as f:
      f.write(json.dumps(json_dict,ensure_ascii=False,indent=4))
  time.sleep(5)
  es.quit()
  ```

- 在使用selenium时，有时候会遇到子页面的情况，通常，这种页面基于iframe存在，遇到这种情况时，我们需要对获取到的主页面源码进行处理，让他能够直接匹配子页面

- ```python
  # swithc_to     将目标iframe注册到页面
  es.switch_to.frame('iframeResult')
  ```

  ##  selenium动作链：

- 创建动作链

  - 在我们需要对页面进行一连串的动作的时候，如： 拖动页面上的块，拖拽图片，挪动方块等，就需要使用到动作链

  - ```python
    from selenium import webdriver
    from lxml import etree
    import time
    import json
    from selenium.webdriver import ActionChains
    es = webdriver.Chrome()
    es.get(url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    # 从网页中找到对应的iframe的id
    time.sleep(3)
    es.switch_to.frame('iframeResult')
    p = es.find_element_by_id('draggable')
    action = ActionChains(es)
    action.click_and_hold(p)
    for i in range(5):
        # move_by_offset()方法，第一个参数为水平移动的距离，第二个参数为垂直移动的距离
        # perform作用是立即执行动作，也就是说，创建好就会进行执行
        action.move_by_offset(10,3).perform()
    action.release()
    ```

  - 上述为示范性代码

- 获取图片





## 无头浏览器：

1. ​	phantomJS是一款无可视化界面的浏览器

2. ```python
   from selenium import webdriver
   # 导入chrome的options中的Options对象
   from selenium.webdriver.chrome.options import Options
   import time
   # 创建一个实例化的Options对象
   chrome_options = Options()
   # 为这个对象设置全性的状态
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--disable-gpu')
   
   # 在绑定浏览器的时候对chrome_options进行重新的赋值
   es = webdriver.Chrome(chrome_options=chrome_options)
   es.get('https://www.baidu.com/')
   print(es.page_source)
   ```

3. 无可视化界面的作用是取消每次运行时打开的网页，但是依然保留浏览器访问的效果，也就是说，不需要每次都打开一个浏览器界面

4. 这样的话，省去了很多不必要的资源占用

5. ```
   # save_screenshot 对页面进行截图并保存起来
   es.save_screenshot('./2.png')
   ```





## 关于截屏与图片点击:

```python
from time import sleep
from lxml import etree
from pil import Image
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])


chrome_option = Options()
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--dosable-gpu')


es = Chrome(options=option,chrome_options=chrome_option)

es.get('https://www.baidu.com/')
sleep(5)

es.save_screenshot('./day05/1.png')

img = es.find_element_by_xpath('//div[@id="lg"]/img')
sleep(3)

location = img.location
size = img.size
rangle = (int(location['x']),int(location['y']),int(location['x'] + size['width']),int(location['y'] + size['height']))
print(rangle)


i = Image.open('./day05/1.png')

frame = i.crop(rangle)

frame.save('./day05/frame.png')
# 构建数据流对图片进行点击操作
action = ActionChains(es)
# move_to_element_with_offset()  第一个参数是作为目标的图片,第二个参数和第三个参数分别为横向便宜和纵向偏移
# click() 方法,进行点击
# perform()  将设定好的数据流立即执行
action.move_to_element_with_offset(img,5,5).click().perform()
sleep(3)
es.quit()
```

