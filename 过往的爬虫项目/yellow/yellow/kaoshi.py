# from selenium.webdriver import Chrome,ChromeOptions
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# pro = Chrome(options=option)
# pro.get('https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=')
# print(pro.page_source)



import requests
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Cookie': 'sid=sem; toUrl=/; JSESSIONID=""; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1577690695; lastCity=101010100; __c=1577690698; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3DNew-%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-05%26unit%3D%25E5%2593%2581%25E7%2589%258C%252B%25E8%2581%258C%25E4%25BD%258D-%25E4%25BF%25A1%25E6%2581%25AF%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25A5%25BD%25E7%2594%25A8%25E5%2590%2597%26bd_vid%3D17399182057516737945&l=%2Fwww.zhipin.com%2F%3Fka%3Dheader-home&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3DNew-%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-05%26unit%3D%25E5%2593%2581%25E7%2589%258C%252B%25E8%2581%258C%25E4%25BD%258D-%25E4%25BF%25A1%25E6%2581%25AF%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25A5%25BD%25E7%2594%25A8%25E5%2590%2597%26bd_vid%3D17399182057516737945&friend_source=0&friend_source=0; __zp_stoken__=f330QN%2BzFJiDmndOYgQOOeMBdx60U4fAUNeaK9ABORAdPOJAx2vfTSGK5yD1LZFttb0TbeZlXSSzi9UoxaZBWT5QVleIsOAjzy2cc0VNiNq%2FKatSgsKOttJ%2FDHNslasJUtv4; __a=29527690.1577690715.1577690715.1577690698.4.2.3.4; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1577690704'
}
response = requests.get('https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=',headers=headers).text
print(response)