# 百度AI

百度ai是开放性的库,在其中实现了包括文本识别,语言识别,声音识别,指纹识别,虹膜识别等各式各样基于人工智能AI的识别方法:

```python
from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '18141048'
API_KEY = 'CPKSpk7Up1aATfxAaP9xln1O'
SECRET_KEY = 'miR2GGKYfx214xEGUO0i83cgFmD3T1Z3'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
```

它的库是开放的,使用方法同样是开放的,所以我们在进行时使用的时候,可以直接调用对应的aip库中的识别方法,就可以将我们的数据分门别类地识别出来,

-   # 提取关键字分类

-   ```python
    client.topic(title, content);
    # 文章分类,从标题与内容中提取关键字进行分类
    # title,content都是必填项
    ```

-   ### 判断词义相似度

-   ```python
    client.wordSimEmbedding(word1, word2);
    # 判断两个对象的相似度
    # 这个结果判断的其实是两个对象的词义的相似度
    # 返回结果为:
    '''
    {
        "score": 0.456862,
        # score 为该对象的相似度,
        "words": {
          "word_1": "北京",
          "word_2": "上海"
        }
    }'''
    ```

-   ### 判断文本相似度

-   ```python
    text1 = "浙富股份"
    
    text2 = "万事通自考网"
    
    """ 调用短文本相似度 """
    client.simnet(text1, text2);
    
    """ 如果有可选参数 """
    options = {}
    options["model"] = "CNN"
    
    """ 带参数调用短文本相似度 """
    client.simnet(text1, text2, options)
    
    '''
    # 这个结果匹配的是文本的相似度,也就是说,并不在乎其中的意义,比较的是其中的内容
    {
        "log_id": 12345,
        "texts":{
            "text_1":"浙富股份",
            "text_2":"万事通自考网"
        },
        "score":0.3300237655639648 //相似度结果
    },
    '''
    ```

-   ### 抽取关键字

-   ```python
    title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"
    
    content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"
    
    """ 调用文章标签 """
    client.keyword(title, content);
    
    # 提取标题与文章中的关键字信息,也就说文字节点,这一点能够方便我们更快的定位想要的信息,以及进行更加精确的信息分类
    '''
    {
        "log_id": 4457308639853058292,
        "items": [
            {
                "score": 0.997762,
                "tag": "iphone"
            },
            {
                "score": 0.861775,
                "tag": "手机"
            },
            {
                "score": 0.845657,
                "tag": "苹果"
            },
            {
                "score": 0.83649,
                "tag": "苹果公司"
            },
            {
                "score": 0.797243,
                "tag": "数码"
            }
        ]
    }
    
    '''
    ```

-   ### 错别字纠正

-   ```python
    text = "百度是一家人工只能公司"
    
    """ 调用文本纠错 """
    client.ecnet(text);
    # 返回结果将会把错误信息与正确的信息封装到item中,并返回,根据这些信息可以将原来的数据进行修正,减少错别字
    '''
    {
        "log_id": 6770395607901559829,
        "item": {
            "vec_fragment": [
                {
                    "ori_frag": "只能",
                    "begin_pos": 21,
                    "correct_frag": "智能",
                    "end_pos": 27
                }
            ],
            "score": 0.875169,
            "correct_query": "百度是一家人工智能公司"
        },
        "text": "百度是一家人工只能公司"
    }
    '''
    ```

-   ### 文字情绪识别

-   ```python
    text = "本来今天高高兴兴"
    
    """ 调用对话情绪识别接口 """
    client.emotion(text);
    
    """ 如果有可选参数 """
    options = {}
    options["scene"] = "talk"
    
    """ 带参数调用对话情绪识别接口 """
    client.emotion(text, options)
    
    # neutral      非强烈负面情绪
    # pessimistic  强烈负面情绪
    '''
    {
        "log_id": 4258005459150262970,
        "text": "本来今天高高兴兴",
        "items": [
            {
                "prob": 0.998619,
                
                "label": "neutral"
            },
            {
                "prob": 0.00138141,
                "label": "pessimistic"
            },
        ]
    }
    '''
    ```



