from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
import time

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# es = webdriver.Chrome(chrome_options=chrome_options)
es = webdriver.Chrome(options=option)
es.get('https://www.taobao.com/')
# print(es.page_source)
# es.save_screenshot('./2.png')

img = es.find_element_by_id('id')
img.screenshot_as_png()