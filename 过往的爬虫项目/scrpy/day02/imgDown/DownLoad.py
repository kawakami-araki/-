import os
import requests
from lxml import etree
def url_get(url,headers):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    res = response.text
    url_dict = lxml_xpath(text=res)

    for i,j in url_dict.items():
        folder_path = "./" + i + "/"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        img_in = img_down(j,headers=headers,folder_path=folder_path)
        if img_in:
            print('下载成功,当前文件数量为:=======>>',img_file)
        else:
            os.removedirs(folder_path)
def lxml_xpath(text):
    ret = etree.HTML(text)
    url_dict = {}
    title_list = ret.xpath('//div[@class="box list channel"]/ul/li/a/text()')
    url_list = ret.xpath('//div[@class="box list channel"]/ul/li/a/@href')
    for i in range(len(title_list)):
        url_dict[title_list[i]] = 'https://www.232mk.com' + url_list[i]
    return url_dict
def img_down(url,headers,folder_path):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    res = response.text
    ret = etree.HTML(res)
    # url_dict = {}
    # div class="content"
    url_list = ret.xpath('//div[@class="content"]/p/a/@href')
    if url_list == []:
        print('这里没有,下一位')
        return False
    for img_url in url_list:
        img_name = img_url.split('/')[-1]
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        res = response.content
        with open(folder_path+img_name,'wb') as f:
            f.write(res)
        print('---------获得一张cg')
    global img_file
    img_file += 1
    return img_file
if __name__ == '__main__':
    img_file = 0
    page = 1
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    url_list = ['https://www.232mk.com/pic/1/index_%d.html'% page for page in range(29,36)]
    for url in url_list:
        print('开始运行')
        url_get(url,Headers)
        print('第%d页结束'% page)
        page += 1