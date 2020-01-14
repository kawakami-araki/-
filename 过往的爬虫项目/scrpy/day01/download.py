# import requests
# url = 'https://vdept.bdstatic.com/577456776e326454437736425a644b68/6d555536596c766d/80f2cdd6f0ad3bd712ba551c00fa309ba0cda2cba416c8c0b0246ff1cbcea9da8ef125b7fdc64c3a90f3efcb7477529a.mp4?auth_key=1576760861-0-0-0cd53cb4fe9e012205b1cc7ad46245f8'
# Headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
# }
# response = requests.get(url=url,headers=Headers)
# text = response.content
# with open('./001.mp4','wb') as f:
#     f.write(text)

import requests
from lxml import etree

url = 'https://www.lanzous.com/ajaxm.php'
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

data = {
    'action': 'downprocess',
    'sign': 'A2VXaQ4_aAzIFDAM8BTVRbVswAzMAbQcxVmADPV0zBDUDJVFyDW1SNwVmAGFXNQA5VTcFOQdhBjBXYA_c_c'
}
response = requests.post(url=url,headers=Headers,data=data)
print(response.json())
# est = etree.HTML(response.text)
# print(response.text)
# dw_url = est.xpath('//div[@id="ready"]/a[1]/@href')
# if dw_url == []:
#     dw_url = est.xpath('//div[@id="go"]/a[1]/@href')
#
# print(dw_url)