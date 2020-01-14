from requests import Session
import time
url = 'https://www.zhipin.com/c101010100/'
import random
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
Headers = {
    "User-Agent": random.choice(user_agent_list),
    'Cookie': 'lastCity=101010100; __c=1577408160; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1577408161; __l=l=%2Fwww.zhipin.com%2Fbeijing%2F&r=&friend_source=0&friend_source=0; __a=70815146.1577408160..1577408160.9.1.9.9; __zp_stoken__=7afdSfEVBzlhqH8Ak%2Bl%2B1St98gc0M%2F1zaZLDCc5ntdbsOABzsTE7vquQVFrd6FvG55VjALJJLFiwM6VXR8%2FhRZvbdSv92DHSLth8cpRmzOb1GBbMIDYNDK7qJTzOfZJNR7%2BP; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1577409340'
}
params = {
    "query" : 'python',
    'page':1
}
sessions = Session()
res = sessions.get(url='https://www.zhipin.com/',headers=Headers)
response = sessions.get(url=url,params=params,headers=Headers)
print(response.text)
# start = time.time()
# for i in range(3):
#     response = requests.get(url=url,headers=Headers)
# from lxml import etree
# print(response.text)
# with open('./kaoshi/zhipin.txt', 'w', encoding='utf-8') as f:
#     f.write(response.text)
# with open('./kaoshi/zhipin.txt', 'a') as a:

#     tree = etree.parse(a)
#     li_list =tree.xpath('//div[@id="main"]//div[@class="job-list"]/ul/li')
#     print(li_list)