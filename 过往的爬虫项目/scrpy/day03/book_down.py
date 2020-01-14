from multiprocessing.dummy import Pool
from requests import Session
from lxml import etree
def request_one(url):
    res = session.get(url=url,headers=Headers).text
    res.encode('utf-8')
    tree = etree.HTML(res)
    url_list = tree.xpath('//div[@class="book-item"]/h3/a/@href')
    title_list = tree.xpath('//div[@class="book-item"]/h3/a/text()')
    request_title(url_list,title_list)

def request_title(url_list,title_list):
    for i in range(len(url_list)):
        book_text = session.get(url='http://www.shicimingju.com' + url_list[i],headers=Headers).text
        book_text.encode('utf-8')
        tree = etree.HTML(book_text)
        book_url_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a/@href')
        book_mulu_list  = tree.xpath('//div[@class="book-mulu"]/ul/li/a/text()')
        book(book_url_list,book_mulu_list,title_list[i])

def book(url_list,mulu_list,title):
    with open('./'+title+'.txt','w',encoding='utf-8') as f:
        for i in range(len(url_list)):
            url = url_list[i]
            mulu = mulu_list[i]
            book_text = session.get(url='http://www.shicimingju.com'+url,headers=Headers).text
            book_text.encode('utf-8')
            tree = etree.HTML(book_text)
            book_neirong = ''.join(tree.xpath('//div[@class="chapter_content"]/p/text()'))
            f.write(mulu+'\n')
            f.write(book_neirong)
        print(title,'下载完成')

if __name__ == '__main__':
    session = Session()
    url = 'http://www.shicimingju.com/bookmark/sidamingzhu.html'
    Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

    request_one(url)