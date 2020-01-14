from multiprocessing.dummy import Pool
from requests import Session
from lxml import etree

session = Session()

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

resp = session.get(url='https://www.baidu.com',headers=Headers)

url = 'https://www.baidu.com/s'

params = {
    "wd" : '16'
}
content_baidu = session.get(url=url,headers=Headers,params=params)
content_baidu.encoding = 'utf-8'
res = etree.HTML(content_baidu.text)
url_list = res.xpath('//h3[@class="t"]/a/@href')
print(len(url_list))
pool = Pool(10)

def get_request(url):
    print('发送一次请求')
    return session.get(url=url,headers=Headers).text
if __name__ == '__main__':
    try:
        response_text_list = pool.map(get_request,url_list)
    except ConnectionError:
        print('失败一次')
    finally:
        print(len(response_text_list))
        for i in response_text_list:
            res = etree.HTML(i)
            html_text = res.xpath('//body')
            print(html_text)