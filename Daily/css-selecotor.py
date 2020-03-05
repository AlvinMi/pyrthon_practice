from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://mall4j-admin.gz-yami.com');

driver.implicitly_wait(30)

username = driver.find_element_by_css_selector('form > div:nth-child(1) > div.el-form-item__content> div.info > input.el-input__inner')
username.send_keys('admin')

password = driver.find_element_by_css_selector('form > div:nth-child(2) > div.el-form-item__content> div.info > input.el-input__inner')
password.send_keys('123456')

#  等待10秒，手动输入验证码 并手动点击登陆
time.sleep(10)

# 登陆成功后点击 产品管理--产品管理
chanpinguanli = driver.find_element_by_css_selector('ul.site-sidebar__menu.el-menu>li:nth-child(3)')
chanpinguanli.click()

chanpinguanli_child = chanpinguanli.find_element_by_css_selector('ul.el-menu.el-menu--inline > li:nth-child(1)')
chanpinguanli_child.click();


#  找到第一个订单编号，并打印出来值
order = driver.find_element_by_css_selector('div.content > div.prod:nth-child(2) > div.prod-tit>span:nth-child(1)');
order_text = order.text;
print('订单编号:',order_text)