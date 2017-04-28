# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as beatsop
import re

driver = webdriver.Chrome("chromedriver")
driver.set_page_load_timeout(30)
driver.get("http://192.168.0.45:8069/web/login?redirect=http%3A%2F%2F192.168.0.45%3A8069%2Fweb%3F")
driver.implicitly_wait(10)
driver.maximize_window()

try:	
	send = driver.find_element_by_id('login')
	send.send_keys("admin")
	print(u'Логин -    ОК')
except:
	print(u'Логин -    ОШИБКА')
	driver.quit()

try:	
	send = driver.find_element_by_id('password')
	send.send_keys("admin")
	print(u'Пароль -    ОК')
except:
	print(u'Пароль -    ОШИБКА')
	driver.quit()

try:
	driver.find_element_by_class_name('btn-primary').click()
	print(u'Вход    ОК')
except:
	print(u'Вход    ОШИБКА')
	driver.quit()

try:
	driver.find_element_by_xpath(".//*[@id='oe_main_menu_placeholder']/ul[1]/li[3]/a/span").click()
	print(u'Продажи    ОК')
except:
	print(u'Продажи    ОШИБКА')
	driver.quit()
	

try:
	driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[1]/div/div[1]/div/div/div[3]/ul[1]/li[2]/a/span").click()
	print(u'Leads    ОК')
except:
	print(u'Leads    ОШИБКА')
	driver.quit()

try:
	driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/th").click()
	print(u'Leads    ОК')
except:
	print(u'Leads    ОШИБКА')
	driver.quit()

try:
	driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/table/tbody[2]/tr[3]/th").click()
	print(u'Leads    ОК')
except:
	print(u'Leads    ОШИБКА')
	driver.quit()



try:
	driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/table/tbody[3]/tr[1]/td[1]").click()
	print(u'Leads    ОК')
except:
	print(u'Leads    ОШИБКА')
	driver.quit()
time.sleep(10)

# promo = driver.find_element_by_css_selector('.oe_form_char_content')
# promo_value = promo.get_attribute('value')
# print(promo_value)


element = driver.find_element_by_class_name('oe_form_char_content')
html = element.get_attribute("outerHTML")
soup = BeautifulSoup(html, "html.parser")
desired_text1 = soup.find("span", class_= 'oe_form_char_content').next
print(desired_text1)
# if desired_text == u'test':
	# driver.find_element_by_css_selector('.oe_button.oe_form_button_edit').click()
	


element1 = driver.find_element_by_class_name('oe_form_text_content')
html = element1.get_attribute("outerHTML")
soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= 'oe_form_text_content').next
print(desired_text)
result1 = re.search(r'\d{11}', desired_text)
print(result1.group(0))
result2 = re.search(r'\w{4}\@\w{4}.\w{2}', desired_text)
print(result2.group(0))
if desired_text1 == u'test' and result1.group(0) == '77777777777' and result2.group(0) == 'test@test.ru':
	print 'ok'
	if driver.find_element_by_css_selector('.oe_button.oe_form_button_edit').click():
		print 'ok'
		if select = Select(driver.find_element_by_id("#oe-field-input-96")):
			print 'ok'
	   		if select.select_by_visible_text('Тестовые заявки'):
	   			print 'ok'
				if driver.find_element_by_css_selector('.oe_button.oe_form_button_save.oe_highlight').click():
					print 'ok'
					if driver.find_element_by_xpath("html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[3]/div/div[4]/div/div/header/ul/li[4]/span[1]").click():
						print 'ok'
					else:
						print 'no'
						driver.quit()	
				else:
					print 'no'
					driver.quit()		
			else:
				print 'no'
				driver.quit()			
		else:
	   		print 'no'
			driver.quit()				
	else:
		print 'no'
		driver.quit()					
else:
	print 'no'
	driver.quit() 


