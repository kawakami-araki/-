from lxml import etree
from requests import Session
session = Session()
url = 'https://zhutix.com/tag/win10-zhuti/'
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}
response = session.get(url=url,headers=Headers)
response.encoding = 'utf8'
est = etree.HTML(response.text)

# a_dict = {}
# for i in range(0,len(est.xpath('//div[@class="thumb pos-r"]/a[1]/@href'))):
#     a_dict[est.xpath('//h2[@class="entry-title"]/a[1]/text()')[i]] = est.xpath('//div[@class="thumb pos-r"]/a[1]/@href')[i]
#
# for key,value in a_dict.items():
#     Headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#     }
#     response = session.get(url=value, headers=Headers)
#     response.encoding = 'utf8'
#     est = etree.HTML(response.text)
#     download_url= est.xpath('//p/span[@class="lianai zouyou"]/a[1]/@href')
#     if download_url == []:
#         continue
#     print(download_url)
#     Headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#     }
#     response_1 = session.get(url=download_url[0], headers=Headers)
#     response_1.encoding = 'utf8'
#     down = etree.HTML(response_1.text)
#     dw_url = down.xpath('//div[@id="ready"]/a[1]/@href')
#     if dw_url == []:
#         dw_url = down.xpath('//div[@id="go"]/a[1]/@href')
#     print(dw_url)
#     if dw_url == []:
#         continue
#     print(dw_url)
#     Headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#     }
#     response = session.get(url=dw_url, headers=Headers)
#     response.encoding = 'utf8'
#     with open('./key'+'.rar', 'wb') as f:
#         f.write(response.content)
#     print(value + '文件下载完成!')



word="word"
print("hllo"+word)