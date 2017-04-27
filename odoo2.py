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

login = 'login'
password = 'password'
enter = 'btn-primary'
prodaji = ".//*[@id='oe_main_menu_placeholder']/ul[1]/li[3]/a/span"
leads = "html/body/div[2]/table/tbody/tr/td[1]/div/div[1]/div/div/div[3]/ul[1]/li[2]/a/span"
novie = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/th"
stajer = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/table/tbody[2]/tr[3]/th"
empty_block = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[2]/div/table/tbody[3]/tr[1]/td[1]"
char_content = 'oe_form_char_content'
# То есть содержание заголовка где указана тема
text_content = "oe_form_text_content"
# То есть где указано: телефон, почта, тема итд
button_edit = '.oe_button.oe_form_button_edit'
prichina_otkaza = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[3]/div/div[4]/div/div/table[5]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/span/select"
button_save = '.oe_button.oe_form_button_save.oe_highlight'
button_musor = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[3]/div/div[4]/div/div/header/ul/li[4]/span[1]"
try:	
	send = driver.find_element_by_id(login)
	send.send_keys("admin")
	print(u'Логин -   ОК')
except:
	print(u'Логин -   ОШИБКА')
	driver.quit()

try:	
	send = driver.find_element_by_id(password)
	send.send_keys("admin")
	print(u'Пароль -  ОК')
except:
	print(u'Пароль -  ОШИБКА')
	driver.quit()

try:
	driver.find_element_by_class_name(enter).click()
	print(u'Вход      ОК')
except:
	print(u'Вход      ОШИБКА')
	driver.quit()

time.sleep(1)
try:
	driver.find_element_by_xpath(prodaji).click()
	print(u'Продажи   ОК')
except:
	print(u'Продажи   ОШИБКА')
	driver.quit()
	
time.sleep(1)
try:
	driver.find_element_by_xpath(leads).click()
	print(u'Leads     ОК')
except:
	print(u'Leads     ОШИБКА')
	driver.quit()

time.sleep(1)
try:
	driver.find_element_by_xpath(novie).click()
	print(u'Leads     ОК')
except:
	print(u'Leads     ОШИБКА')
	driver.quit()

time.sleep(1)

list_group = 'oe_list_group_name'
gt = driver.find_elements_by_class_name(list_group)
for el in gt:
	print(el).text
	el_text = el.text
	result = re.search(u'Стажер', el_text)
	if result:
		aster = result.group(0)
		print(aster)
		el.click()
	

# try:
# 	driver.find_element_by_xpath(stajer).click()
# 	print(u'Leads     ОК')
# except:
# 	print(u'Leads     ОШИБКА')
# 	driver.quit()


time.sleep(1)
try:
	driver.find_element_by_xpath(empty_block).click()
	print(u'Leads     ОК')
except:
	print(u'Leads     ОШИБКА')
	driver.quit()
time.sleep(10)


element = driver.find_element_by_class_name(char_content)
html = element.get_attribute("outerHTML")
soup = BeautifulSoup(html, "html.parser")
desired_text1 = soup.find("span", class_= char_content).next
print(desired_text1)
if desired_text1 == u'test':
	print "ok"
else:
	print "no"
	driver.quit()
	


element1 = driver.find_element_by_class_name(text_content)
html = element1.get_attribute("outerHTML")
soup = BeautifulSoup(html, "html.parser")
desired_text = soup.find("span", class_= text_content).next
print(desired_text)
result1 = re.search(r'7{11}', desired_text)
if result1:
	print(result1.group(0))

result2 = re.search(r'test\@test\.ru', desired_text)
if result2:
	print(result2.group(0))
# Если result2 true, то только тогда принт. Если не поставить это условие, то когда result2 равен none возникает ошибка NoneType object has no attribute group

result3 = re.search(r'test\@diplomtime\.ru', desired_text)
if result3:
	print(result3.group(0))


if desired_text1 == u'test' and result1 and (result2 or result3):
	print 'ok'
	driver.find_element_by_css_selector(button_edit).click()
else:
	print 'no'
	driver.quit() 

try:
	select = Select(driver.find_element_by_xpath(prichina_otkaza))
	select.select_by_visible_text('Тестовые заявки')
	print 'Выбран тип: Тестовые заявки - ok'
except:
	print 'Выбран тип: Тестовые заявки - no'
	driver.quit()

try:
	driver.find_element_by_css_selector(button_save).click()
	print 'ok'
except:
	print 'no'
	driver.quit()

try:
	driver.find_element_by_xpath(button_musor).click()							
	print 'ok'
except:
	print 'no'
	driver.quit()


# if desired_text1 == u'test' and result1.group(0) == '77777777777' and (result2.group(0) == 'test@test.ru' or result3.group(0) == 'test@diplomtime.ru'):