
# import requests
# import csv
# import pandas as pd
# from bs4 import BeautifulSoup
# from requests.exceptions import RequestException
# def get_one_page(url):
# 	try:
# 		headers = {
# 			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) ' + 
# 			'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
# 		}
# 		html = requests.get(url, headers=headers)
# 		if html.status_code == 200:
# 			return html.text
# 		return None
# 	except RequestException:
# 		return None


# print(get_one_page('https://www.zhipin.com/c101010100/?query=python&page=2&ka=page-2'))


# import os
# file_path = __file__.split('/')[:-1]
# file_path_2 = '/'.join(file_path)
# print(file_path_2)

# import os

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# IMAGES_STORE = 'C:/Users/lenovo/Desktop/two_spiders/two_spiders/imgsLib'
IMAGES_STORE = os.path.join(BASE_DIR,'imgsLib')
print(IMAGES_STORE)