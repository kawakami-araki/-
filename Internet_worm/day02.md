---
requests模块初试
---

# requests模块

## 概念

​		一个机遇网络请求的模块,作用就是用来模拟浏览器发起请求

​	[asdsa]()

## 编码流程

​		-- 指定url

​		-- 进行请求的发送

​		-- 获取相应数据(即,爬取到的数据)

​		-- 持久化存储

​			** 环境的安装

​			** pip install requests

## 代码示例

```python
#导入request模块
import requests
# 准备初始url
url = 'https://www.baidu.com/s'
# 准备伪装用的请求头
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Cookie': "BAIDUID=97DA851F88C92BE45D7963ADA75C3434:FG=1; BIDUPSID=97DA851F88C92BE45D7963ADA75C3434; PSTM=1567649375; BD_UPN=12314753; BDUSS=3ZzTkJOTHRNVkpqVGR4cE9BaWlOVlJUcX5JbHVXMWEwWVQ3V1pmbUJEbVQxQmRlRUFBQUFBJCQAAAAAAAAAAAEAAABbuGacAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJNH8F2TR~Bdb; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=cvFOJeC62CrXf4cwU0e2tW9rYM4hm03TH6aIl2P5JFJeo_dcX41gEG0PDf8g0KubMVkPogKKBeOTHg_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JRA8oKPhtCvhDRTvhCcjh-FSMgTBKI62aKDs2ROYBhcqEIL4W6-aKPIp5nO8W4KL-6nH2IOK5DoEHxbSj4QzQU0zDPvl0RQuWI3bhqvztp5nhMJFXj7JDMP0qJ7j2RQy523ion6vQpn-KqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0j63-DaAJt6njJTRe0Rj-KbP_hDL9eKTjhPrMjHrJWMT-0bFH_JR2QJP5fUbJQpPVKJ3-MMc9BMvuJan7_JjYbRDVMfQhWhJChtLeyU6r3fQxtNRB-CnjtpvhKJjjWtcobUPUDMc9LUvqHmcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD05MDIwjTt3-4LtMxrXKK6QKCjj3toObnnqq6rkbJ83yhFzXP6-35KHf6rMKR_bbhrBj5CzKJOb5MrXeJb-5h37JD6yb-n5Lb8KDRPGehrAMJFYQ4oxJpO7BRbMopvaKquVoJQvbURvD-ug3-7qex5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoD-2tKD5MIDr5nJbq4I85M5H54cX--o2WbCQaM7O8pcNLTDKLnLNjb72-MC8BNrJ-KTua-PMjbCxjqO1j4_PMa8OKhFeLHIebbQJyIb-hl5jDh3Ub6ksD-Rt5frp2aRy0hvc0J5cShnkDMjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDG8JJ5_eJbCsL-35HJcqfbo4-tr_KICShUFs5b5lB2Q-5KL-0-oieCbn5p_2bjD33NrHXxuJ2IDjoMbdJJjzDKoMjf6Py4LeBUO2XT0D52TxoUJg5DnJhhvG-xc4Mp8ebPRi3tQ9QgbMMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjLBDTb33H; H_PS_PSSID=1460_21110_30210_30284_22160; yjs_js_security_passport=3b54287a45b25629d2f7cfdb10008d7e9d67b5bd_1576637318_js; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=2; BD_HOME=1; H_PS_645EC=b428Vxu0iZX7iP6ukpImwh5YVC5tlT7Iwn5ZIzZa5ijoKNVsMoi%2FCv%2FtNME"
}
# 准备请求时的数据
params = {
    "wd" : '666'
}
# 开始进行数据获取
# url 要爬取的网页
# params 要传入的数据
# headers 伪装用的请求头
response = requests.get(url=url,params=params,headers=Headers)
# 对获取到的页面进行转码
response.encoding = 'utf8'
# 将整个页面的数据进行赋值
text = response.text
# 打开一个新的文件,将获取到的数据进行存储
with open('./baidu.html','w',encoding='utf8') as f:
    f.write(text)
# 爬虫工作结束
```

## 易错点:

1. 请求时,并不一定要传入数据,url是必须的,同时,要根据网站的要求进行对应的转码
2. 当爬虫被反爬时,西药进行ua伪装

## requests使用post请求:

1. 使用post请求时,需要传入的参数基本上没有变化,唯一的区别就是params变成了data
2. 除此以外和get请求基本一致,但是要注意,当使用axios请求时,需要将你要用到的参数放进去,如页码,每页最大数量等
3. 由于axios返回的数据实际上是json格式的字符串,因此,在进行数据解析的时候,不能再使用text
4. 要使用json来进行解析,然后才能进行操作



# request概念



## 请求方法

1. GET  :  请求页面,并返回页面内容   
2. POST  :  用于提交表单数据或上传文件,数据包含在请求体重
3. PUT  :  从客户端想服务器传送的数据取代指定文档中的内容
4. DELETE  :  请求服务器删除指定的页面
5. HEAD  :  类似于GET请求,只不过返回的响应中没有具体的内容,用于获取报头
6. CONNECT  :  把服务器当成跳板,让服务器代替客户端访问其他网页
7. OPTIONS  :  允许客户端查看服务器的性能
8. TRACE  :  会先服务器收到的请求,用于测试或诊断

## GET    POST  区别:

1. GET请求包含在URL里面,明文传输,安全性低
2. POST请求数据封装到了请求体中,安全性较高



## 关于访问请求的方法:

1. text
   1. 查看返回的TEXT/HTML格式代码
2. json
   1. 将获取到的json字符串转化为dict格式
3. content
   1. 将获取到的文件流进行转化存储







# UA伪装:

关于UA伪装:

- ​	模拟headers
  - 用以模拟浏览器对网页url进行访问,以此来避开页面的反爬机制
  - user_agent       存储用户使用的系统版本号与浏览器信息等数据,用来模拟浏览器访问







# request

- get/post
  - url
  - data/params   (对请求参数进行封装)
  - headers       (UA伪装)
- 动态加载
  - ajax
  - js
- 鉴定是否具备动态加载
  - 局部搜索
  - 全局搜索

## re模块匹配:

使用re模块对获取到的页面进行匹配,用到的比较少,但也是个重点

```python
import re
impore requests
res = requests.get('www.baidu.com')
res.encoding = 'utf8'
# ret为 正则匹配公式
# re.S为 单行匹配,通常情况下,在匹配html页面的时候,都需要进行单行匹配
re.findall(ret,res,re.S)

```





# requests高阶应用:

1. 文件上传功能

   - ```python
     import requests
     url = 'http://www.httpbin.org/'
     Headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
     }
     
     f = open('./baidu.html','rb')
     files = {
         'file': f
     }
     response = requests.get(url=url,headers=Headers,files=files)
     if response:
         print('上传成功')
     ```

   - 文件上传功能

2. 模拟cookie

   1. 手动添加cookie

      - 在headers中添加cookie属性

      - ```python
        
        Headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            'Cookie': "BAIDUID=97DA851F88C92BE45D7963ADA75C3434:FG=1; BIDUPSID=97DA851F88C92BE45D7963ADA75C3434; PSTM=1567649375; BD_UPN=12314753; BDUSS=3ZzTkJOTHRNVkpqVGR4cE9BaWlOVlJUcX5JbHVXMWEwWVQ3V1pmbUJEbVQxQmRlRUFBQUFBJCQAAAAAAAAAAAEAAABbuGacAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJNH8F2TR~Bdb; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=cvFOJeC62CrXf4cwU0e2tW9rYM4hm03TH6aIl2P5JFJeo_dcX41gEG0PDf8g0KubMVkPogKKBeOTHg_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JRA8oKPhtCvhDRTvhCcjh-FSMgTBKI62aKDs2ROYBhcqEIL4W6-aKPIp5nO8W4KL-6nH2IOK5DoEHxbSj4QzQU0zDPvl0RQuWI3bhqvztp5nhMJFXj7JDMP0qJ7j2RQy523ion6vQpn-KqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0j63-DaAJt6njJTRe0Rj-KbP_hDL9eKTjhPrMjHrJWMT-0bFH_JR2QJP5fUbJQpPVKJ3-MMc9BMvuJan7_JjYbRDVMfQhWhJChtLeyU6r3fQxtNRB-CnjtpvhKJjjWtcobUPUDMc9LUvqHmcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD05MDIwjTt3-4LtMxrXKK6QKCjj3toObnnqq6rkbJ83yhFzXP6-35KHf6rMKR_bbhrBj5CzKJOb5MrXeJb-5h37JD6yb-n5Lb8KDRPGehrAMJFYQ4oxJpO7BRbMopvaKquVoJQvbURvD-ug3-7qex5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoD-2tKD5MIDr5nJbq4I85M5H54cX--o2WbCQaM7O8pcNLTDKLnLNjb72-MC8BNrJ-KTua-PMjbCxjqO1j4_PMa8OKhFeLHIebbQJyIb-hl5jDh3Ub6ksD-Rt5frp2aRy0hvc0J5cShnkDMjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDG8JJ5_eJbCsL-35HJcqfbo4-tr_KICShUFs5b5lB2Q-5KL-0-oieCbn5p_2bjD33NrHXxuJ2IDjoMbdJJjzDKoMjf6Py4LeBUO2XT0D52TxoUJg5DnJhhvG-xc4Mp8ebPRi3tQ9QgbMMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjLBDTb33H; H_PS_PSSID=1460_21110_30210_30284_22160; yjs_js_security_passport=3b54287a45b25629d2f7cfdb10008d7e9d67b5bd_1576637318_js; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=2; BD_HOME=1; H_PS_645EC=b428Vxu0iZX7iP6ukpImwh5YVC5tlT7Iwn5ZIzZa5ijoKNVsMoi%2FCv%2FtNME"
        }
        ```

      - 如上图所示

      - ```python
        import requests
        
        url = 'https://www.baidu.com/s'
        
        ### 创建requests.cookies.RequestsCookiesJar对象
        jar = requests.cookies.RequestsCookieJar()
        Cookie =  "BAIDUID=97DA851F88C92BE45D7963ADA75C3434:FG=1; " \
                  "BIDUPSID=97DA851F88C92BE45D7963ADA75C3434; " \
                  "PSTM=1567649375; BD_UPN=12314753; " \
                  "BDUSS=3ZzTkJOTHRNVkpqVGR4cE9BaWlOVlJUcX5JbHVXMWEwWVQ3V1pmbUJEbVQxQmRlRUFBQUFBJCQAAAAAAAAAAAEAAABbuGacAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJNH8F2TR~Bdb; " \
                  "BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; " \
                  "BDSFRCVID=cvFOJeC62CrXf4cwU0e2tW9rYM4hm03TH6aIl2P5JFJeo_dcX41gEG0PDf8g0KubMVkPogKKBeOTHg_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; " \
                  "H_BDCLCKID_SF=JRA8oKPhtCvhDRTvhCcjh-FSMgTBKI62aKDs2ROYBhcqEIL4W6-aKPIp5nO8W4KL-6nH2IOK5DoEHxbSj4QzQU0zDPvl0RQuWI3bhqvztp5nhMJFXj7JDMP0qJ7j2RQy523ion6vQpn-KqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0j63-DaAJt6njJTRe0Rj-KbP_hDL9eKTjhPrMjHrJWMT-0bFH_JR2QJP5fUbJQpPVKJ3-MMc9BMvuJan7_JjYbRDVMfQhWhJChtLeyU6r3fQxtNRB-CnjtpvhKJjjWtcobUPUDMc9LUvqHmcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD05MDIwjTt3-4LtMxrXKK6QKCjj3toObnnqq6rkbJ83yhFzXP6-35KHf6rMKR_bbhrBj5CzKJOb5MrXeJb-5h37JD6yb-n5Lb8KDRPGehrAMJFYQ4oxJpO7BRbMopvaKquVoJQvbURvD-ug3-7qex5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoD-2tKD5MIDr5nJbq4I85M5H54cX--o2WbCQaM7O8pcNLTDKLnLNjb72-MC8BNrJ-KTua-PMjbCxjqO1j4_PMa8OKhFeLHIebbQJyIb-hl5jDh3Ub6ksD-Rt5frp2aRy0hvc0J5cShnkDMjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDG8JJ5_eJbCsL-35HJcqfbo4-tr_KICShUFs5b5lB2Q-5KL-0-oieCbn5p_2bjD33NrHXxuJ2IDjoMbdJJjzDKoMjf6Py4LeBUO2XT0D52TxoUJg5DnJhhvG-xc4Mp8ebPRi3tQ9QgbMMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjLBDTb33H; " \
                  "H_PS_PSSID=1460_21110_30210_30284_22160; " \
                  "yjs_js_security_passport=3b54287a45b25629d2f7cfdb10008d7e9d67b5bd_1576637318_js; " \
                  "BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; " \
                  "delPer=0; " \
                  "BD_CK_SAM=1; " \
                  "PSINO=2; " \
                  "BD_HOME=1; " \
                  "H_PS_645EC=b428Vxu0iZX7iP6ukpImwh5YVC5tlT7Iwn5ZIzZa5ijoKNVsMoi%2FCv%2FtNME"
        将准备好的cookie进行处理,并添加到jar对象中去
        for i in Cookie.split(';'):
            key,value = i.split('=',1)
            jar.set(key,value)
        
        
        Headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        
        }
        
        params = {
            "wd" : '666'
        }
        # 发送请求时添加cookies参数
        response = requests.get(url=url,params=params,headers=Headers,cookies=jar)
        response.encoding = 'utf8'
        
        text = response.text
        print(text)
        ```

      - 上述为第二种cookies的使用方法

   2. 全自动添加cookie

      - ```python
        from requests import Session
        
        # 构建全安心的Session实例
        
        session = Session()
        
        url = 'https://www.baidu.com/s'
        
        Headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        
        params = {
            "wd" : '666'
        }
        
        response = session.get(url=url,headers=Headers,params=params)
        
        response.encoding = 'utf8'
        
        text = response.text
        ```

      - 使用session的时候,将会全自动生成cookies

      - 同时,相比较requests访问,session访问将会存储状态,

      - requests访问时无状态访问,session访问将会进行状态保持,维持会话

      - 省略了大量的cookie代码,相比较来说,更加方便

      - ```python
        # requests访问的时候,每次都需要传入cookie
        # 如果需要访问的网站时需要维持登陆状态的话,使用resquests将会很不方便,因为没有状态保持
        # session可以维持用户的登陆状态
        ```



## SSL证书验证:

```python
import requests
import urllib3

url = 'https://www.tutumanhua.com/gaoxiao/'

# 关闭网页证书报错
urllib3.disable_warnings()

res = requests.get(url=url, verify=False)
# verify=False    
# 关闭SSL证书验证
```



# Request,Session:

```python
from requests import Session,Request

url = 'https://www.baidu.com'
session = Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}
res_obj = Request(method='GET',url=url,headers=headers)
# 对准备好的数据进行处理,并添加请求方式
res_obj2 = session.prepare_request(res_obj)
# 使用session.prepare_request对数据进行处理,并打包好
ret = session.send(res_obj2)
# 将打包好的数据发送出去,并接受返回的数据
ret.encoding = 'utf-8'
with open('./baidu.html', 'w', encoding='utf-8') as f:
    # 持久化存储
    f.write(ret.text)
```





# Urllib3:

1. request