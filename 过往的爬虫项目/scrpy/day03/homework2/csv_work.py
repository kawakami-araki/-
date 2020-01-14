from lxml import etree
import requests
import csv
def func(url):
    a = 1
    json_list = []
    with open('./data.csv', 'w', encoding='utf-8') as csvf:
        # 构建csv文件基础属性,内容的分隔符
        writer = csv.writer(csvf,delimiter=',')
        # 写入文件,传入的参数是一个列表
        writer.writerow(['user', 'content', 'img_name', 'up','down'])
    with open('./data.csv', 'a', encoding='utf-8') as csvf:
        writer = csv.writer(csvf,delimiter=',')
        while True:
            res = requests.get(url=url,headers=Headers).text
            tree = etree.HTML(res)
            # 用户名
            user_name_list = tree.xpath('//li//div[@class="u-txt"]/a/text()')
            # 内容
            # neirong_list = tree.xpath('//li/div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()')
            neirong_list = tree.xpath('//li/div[@class="j-r-list-c"]')
            # 点赞
            nice_count = tree.xpath(
                '//div[@class="j-r-list-tool"]/div[@class="j-r-list-tool-l "]/ul/li[@class="j-r-list-tool-l-up"]/span/text()')
            # 踩
            not_count = tree.xpath(
                '//div[@class="j-r-list-tool"]/div[@class="j-r-list-tool-l "]/ul/li[@class="j-r-list-tool-l-down "]/span/text()')

            # 下一页的网址
            for i in range(len(user_name_list)):
                a_dict = {
                    "user": user_name_list[i],
                    'up': nice_count[i],
                    'down': not_count[i],
                    'content': neirong_list[i].xpath('./div[@class="j-r-list-c-desc"]/a/text()')[0],
                    'img_name' : ''
                }
                json_list.append(a_dict)
                if neirong_list[i].xpath('./div[@class="j-r-list-c-img"]/a/@href') != []:
                    img_url = neirong_list[i].xpath('./div[@class="j-r-list-c-img"]/a/@href')[0]
                    a_tree = etree.HTML(requests.get('http://www.budejie.com'+img_url,headers=Headers).text)
                    if a_tree:
                        a_img_url = a_tree.xpath('//div[@class="j-r-list-c"]/div[@class="j-r-list-c-img"]/img/@src')
                        if a_img_url != []:
                            img_name = a_tree.xpath('//div[@class="j-r-list-c"]/div[@class="j-r-list-c-img"]/img/@src')[0].split('/')[-1]
                            with open('./'+img_name, 'wb')as m:
                                m.write(requests.get(a_img_url[0],headers=Headers).content)
                            a_dict['img_name'] = img_name

                writer.writerow([a_dict["user"], a_dict['content'], a_dict['img_name'], a_dict['up'], a_dict['down']])
            print('第{a}页完成'.format(a=a))
            a += 1
            url_list = tree.xpath('//div[@class="j-page"]/div/a[@class="pagenxt"]/@href')
            if url_list == []:
                break
            else:
                url = 'http://www.budejie.com/' + url_list[0]
            if a > 5:
                break
if __name__ == '__main__':
    Headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=n0T3lOTFc9zAynEuauNxoQ84QsYHJ-BOc4xVzJGGr16JZ1SjyZEz4t1C3Mu2_knF&wd=&eqid=974edc0f00052fae000000025e0084dd; Hm_lvt_7c9f93d0379a9a7eb9fb60319911385f=1577092322; _ga=GA1.2.1651456976.1577092326; _gid=GA1.2.115374688.1577092326; Hm_lpvt_7c9f93d0379a9a7eb9fb60319911385f=1577098722"
    }
    url = 'http://www.budejie.com/'
    func(url)