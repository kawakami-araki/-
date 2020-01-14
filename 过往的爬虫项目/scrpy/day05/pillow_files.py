from time import sleep
from lxml import etree
from pil import Image
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
chrome_option = Options()
# chrome_option.add_argument('--headless')
# chrome_option.add_argument('--dosable-gpu')
es = Chrome(options=option,chrome_options=chrome_option)
es.get('https://www.baidu.com/')
sleep(5)
es.save_screenshot('./day05/1.png')
img = es.find_element_by_xpath('//div[@id="lg"]/img')
sleep(3)
location = img.location
size = img.size
rangle = (int(location['x']),int(location['y']),int(location['x'] + size['width']),int(location['y'] + size['height']))
print(rangle)
i = Image.open('./day05/1.png')
frame = i.crop(rangle)
frame.save('./day05/frame.png')
# 构建数据流对图片进行点击操作
action = ActionChains(es)
# move_to_element_with_offset()  第一个参数是作为目标的图片,第二个参数和第三个参数分别为横向便宜和纵向偏移
# click() 方法,进行点击
# perform()  将设定好的数据流立即执行
action.move_to_element_with_offset(img,5,5).click().perform()
sleep(3)
es.quit()