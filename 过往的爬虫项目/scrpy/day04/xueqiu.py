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