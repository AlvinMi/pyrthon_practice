from selenium  import webdriver
# 打开浏览器
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

baidu_input = driver.find_element_by_id('kw')
baidu_input.clear()
baidu_input.send_keys('hello world')

baidu_button = driver.find_element_by_id('su')
baidu_button.click()
