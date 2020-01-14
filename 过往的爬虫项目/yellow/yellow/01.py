from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '18141048'
API_KEY = 'CPKSpk7Up1aATfxAaP9xln1O'
SECRET_KEY = 'miR2GGKYfx214xEGUO0i83cgFmD3T1Z3'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "百度是一家高科技公司"
title = '高科技公司'

""" 调用词法分析 """
# data = client.lexer(text)
# for i in data['items']:
#     print(i['basic_words'])

data = client.topic(title,text)
print(data['item']['lv1_tag_list'][0]['score'])
print(data['item']['lv1_tag_list'][0]['tag'])
# for i in data['items']:
#     print(i['basic_words'])