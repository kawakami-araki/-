from selenium import webdriver
from selenium.webdriver import ChromeOptions,Chrome
from lxml import etree
import time
import json

option = ChromeOptions()
option.add_experimental_option('excludeSwithes', ['enable-automation'])
es = Chrome(options=option)
url='https://www.zhipin.com'
es.get(url=url)
# search_input = es.find_element_by_id('kw')
search_input = es.find_element_by_xpath('//input[@name="query"]')
search_input.send_keys('python')
btn = es.find_element_by_xpath('//button[@class="btn btn-search"]')
# btn = es.find_element_by_xpath('//input[@id="su"]')
btn.click()
time.sleep(3)
print(es.page_source)
res_text = es.page_source
with open('./kaoshi/%d.txt'% i, 'w', encoding='utf-8') as f:
    f.write('res_text')
# for i in range(1,6):
#     es.get(url=url% i)
#     time.sleep(2)
#     res_text = es.page_source
#     with open('./kaoshi/%d.txt'% i, 'w', encoding='utf-8') as f:
#         f.write('res_text')
    # tree = etree.HTML(res_text)
    # div_list = tree.xpath('//div[@id="main"]//div[@class="job-list"]/ul/li')
    # json_dict = []
    # print(div_list)
    # for i in div_list:
    #     a_dict = {}
    #     a_dict['title'] = i.xpath('./h3/a/text()')
    #     a_dict['content'] = i.xpath('./p/text()')[0]
    #     a_dict['username'] = i.xpath('./div/div/a[@class="AnonymousHome_user-name_3wN"]/text()')[0]
    #     a_dict['company'] = i.xpath('./div/div/span[1]/text()')[0]
    #     a_dict['creat_time'] = i.xpath('./div/div/span[2]/text()')[0]
    #     a_dict['count'] = i.xpath('./div/div[2]/text()')[0]
    #     json_dict.append(a_dict)
    # with open('./xueqiu.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(json_dict,ensure_ascii=False,indent=4))
    # time.sleep(5)
    # es.quit()
    exit()