from selenium import webdriver
import time
es = webdriver.Chrome()
es.get('https://www.baidu.com/')
search_input = es.find_element_by_id('kw')
# search_input = es.find_element_by_xpath('//input[@id="kw"]')
search_input.send_keys('俺也一样')
btn = es.find_elements_by_id('su')[0]
# btn = es.find_element_by_xpath('//input[@id="su"]')
btn.click()
time.sleep(3)
# shouye = es.find_elements_by_partial_link_text('首页')[0]
# shouye.click()

es.execute_script('window.scrollTo(0,document.body.clientHeight)')
time.sleep(3)
es.quit()