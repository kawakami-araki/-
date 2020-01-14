from selenium import webdriver
from lxml import etree
import time
import json
from selenium.webdriver import ActionChains
es = webdriver.Chrome()
es.get(url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 从网页中找到对应的iframe的id
time.sleep(3)
es.switch_to.frame('iframeResult')
p = es.find_element_by_id('draggable')
action = ActionChains(es)
action.click_and_hold(p)
for i in range(5):
    action.move_by_offset(10,3).perform()

