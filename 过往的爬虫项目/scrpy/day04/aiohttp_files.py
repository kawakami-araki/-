import aiohttp
import asyncio
import time
from lxml import etree
import json
import random
start = time.time()
async def func(url):
    async with aiohttp.ClientSession() as a:
        async with await a.get(url=url,headers=Headers) as response:
            result = await response.text()
            return result

def func1(task):
    tree = etree.HTML(task.result())
    ip_list = tree.xpath('//table[@id="ip_list"]//tr[@class="odd"]/td[2]/text()')
    port_list = tree.xpath('//table[@id="ip_list"]//tr[@class="odd"]/td[3]/text()')
    http_type_list = tree.xpath('//table[@id="ip_list"]//tr[@class="odd"]/td[6]/text()')
    global num
    for i in range(len(ip_list)):
        if http_type_list[i] == 'HTTPS':
            json_data_https.append({'ip': ip_list[i],'port': port_list[i],'http_type':http_type_list[i]})
            global https_num
            https_num += 1
        else:
            json_data_http.append({'ip': ip_list[i],'port': port_list[i],'http_type':http_type_list[i]})
            global http_num
            http_num += 1
    print('第%d頁爬取完成'% num)
    print(json_data_http)
    num += 1


if __name__ == '__main__':
    urls = []
    num = 1
    json_data_http = []
    json_data_https = []
    http_num = 0
    https_num = 0
    for i in range(1,100):
        urls.append('https://www.xicidaili.com/nn/%d'% i)
    tasks = []
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
        'Cookie': "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTY4MDY3MTJiYzc5ZDJhN2ViMDZiNGQyZDE2ZTQ5MGQxBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMU1xTTFUbnhpOHlac3pJWXBSUzMwSGZTVk5oM2wzSTNQQWNIZ0JOMTM5SzA9BjsARg%3D%3D--b6b7096e52c83ea05ccf81e6886bf299746e9863; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1576808673,1576821840,1577428632; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1577428744"
    }
    for url in urls:
        f = func(url)
        task = asyncio.ensure_future(f)
        tasks.append(task)
        task.add_done_callback(func1)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    with open('./day04/pricx/http.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_data_http,ensure_ascii=False,indent=4))
    with open('./day04/pricx/https.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_data_https,ensure_ascii=False,indent=4))
    print(time.time()-start)
    print(http_num)
    print(https_num)
