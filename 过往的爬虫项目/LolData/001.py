from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '18141048'
API_KEY = 'CPKSpk7Up1aATfxAaP9xln1O'
SECRET_KEY = 'miR2GGKYfx214xEGUO0i83cgFmD3T1Z3'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "百度是一家高科技公司"

""" 调用词法分析 """
data = client.lexer(text)
print(data)