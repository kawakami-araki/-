# import requests
# import urllib3
# import bs4
# import os
# url = 'https://www.tutumanhua.com/gaoxiao/'
#
# urllib3.disable_warnings()
#
# res = requests.get(url=url, verify=False)
# res.encoding = 'utf-8'
# soup = bs4.BeautifulSoup(res.text,features='lxml')
# li_list = soup.find('div',class_='cy_list_mh').find_all('li',class_='title')
# url_dict = {}
# for i in li_list:
#     new_url = 'https://www.tutumanhua.com' + i.a['href']
#     title = i.text
#     url_dict[title] = new_url
#
# # print(url_dict)
#
# res_2 = requests.get(url=url_dict['命里有他'], verify=False)
# res_2.encoding = 'utf-8'
# soup = bs4.BeautifulSoup(res_2.text,features='lxml')
# li_list = soup.find('div',class_='cy_plist').find('ul',id='mh-chapter-list-ol-0').find_all('li')
# new_dict_1 = {}
# for item in li_list:
#     new_dict_1[item.text] = 'https://www.tutumanhua.com' + item.a['href']
# print(new_dict_1)
# # {'3  命中注定出现！': '/gaoxiao/mingliyouta/392790.html', '第2话  心动时刻': '/gaoxiao/mingliyouta/392789.html', '2  心动时刻': '/gaoxiao/mingliyouta/391974.html', '第1话 冤家路窄，变身为猫': '/gaoxiao/mingliyouta/390648.html', '序章 ': '/gaoxiao/mingliyouta/388061.html'}
#
# a_list = []
# for p in range(1,1000):
#     res_3 = requests.get(url=(new_dict_1['3  命中注定出现！'] + '?P=%d'% p), verify=False)
#     res_3.encoding = 'utf-8'
#     soup = bs4.BeautifulSoup(res_3.text,features='lxml')
#     # select_list = soup.find('span',class_='k_total')
#     img = soup.find('img',id='qTcms_pic')
#     if img not in a_list:
#         print(p)
#         a_list.append(img)
#         print(img)
#     else:
#         break
    # print(select_list)
    # new_dict_2 = {}
    # for item in li_list:
    #     new_dict_1[item.text] = item.a['href']
    # print(new_dict_1)























































# from requests import Session,Request
#
# url = 'https://www.baidu.com'
# session = Session()
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
# }
# res_obj = Request(method='GET',url=url,headers=headers)
# res_obj2 = session.prepare_request(res_obj)
# ret = session.send(res_obj2)
# ret.encoding = 'utf-8'
# with open('./baidu.html', 'w', encoding='utf-8') as f:
#     f.write(ret.text)


# import requests
# import urllib3
#
# # url = 'https://www.tutumanhua.com/gaoxiao/'
# url = 'http://httpbin.org/get'
#
# urllib3.disable_warnings()
# proxies = {
#     "http": "http://60.167.103.60:9999",
#     "https": "https://183.166.138.137:9999"
# }
# res = requests.get(url=url, verify=False,proxies=proxies)
# print(res.text)

# from requests import Session
# session = Session()
# url = 'https://www.baidu.com/s'
# Headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
# }
#
# proxies = {
#     "http": "http://60.167.103.60:9999",
#     "https": "http://58.87.68.189:1080"
# }
# params = {
#     "wd" : 'ip'
# }
# response = session.get(url=url,params=params,headers=Headers,proxies=proxies)
# response.encoding = 'utf8'
# text = response.text
# print(text)