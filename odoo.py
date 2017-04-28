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
text_content = "oe_form_text_content"
button_edit = '.oe_button.oe_form_button_edit'
prichina_otkaza = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[3]/div/div[4]/div/div/table[5]/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/span/select"
button_save = '.oe_button.oe_form_button_save.oe_highlight'
button_musor = "html/body/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div[3]/div/div[4]/div/div/header/ul/li[4]/span[1]"
arrow = 'html/body/div[2]/table/tbody/tr/td[2]/div/div/table/tbody/tr[2]/td[3]/div/div[2]/ul/li[2]/a'

try:	
	send = driver.find_element_by_id(login)
	send.send_keys("admin")
	print(u'Логин                                              ОК')
except:
	print(u'Логин                                              ОШИБКА')
	driver.quit()

try:	
	send = driver.find_element_by_id(password)
	send.send_keys("admin")
	print(u'Пароль                                             ОК')
except:
	print(u'Пароль                                             ОШИБКА')
	driver.quit()

try:
	driver.find_element_by_class_name(enter).click()
	print(u'Вход                                               ОК')
except:
	print(u'Вход                                               ОШИБКА')
	driver.quit()

time.sleep(2)
try:
	driver.find_element_by_xpath(prodaji).click()
	print(u'Продажи                                            ОК')
except:
	print(u'Продажи                                            ОШИБКА')
	driver.quit()
	
time.sleep(3)
try:
	driver.find_element_by_xpath(leads).click()
	print(u'Leads                                              ОК')
except:
	print(u'Leads                                              ОШИБКА')
	driver.quit()

time.sleep(2)
try:
	driver.find_element_by_xpath(novie).click()
	print(u'Новые нажат                                        ОК')
except:
	print(u'Новые не нажат                                     ОШИБКА')
	driver.quit()

time.sleep(2)
list_group = 'oe_list_group_name'
gt = driver.find_elements_by_class_name(list_group)
tranee_el = None
for el in gt:
	el_text = el.text
	result = re.search(u'Стажер', el_text)
	if (result):
		tranee_el = el

if tranee_el:
	tranee_el.click()
	print(u"Произведен вход в: Cтажер                          ОК")
else:
	print(u"Стажер не найден                                   Закрываю браузер!")
	driver.quit()

time.sleep(2)
try:
	driver.find_element_by_xpath(empty_block).click()
	print(u'Пустой блок нажат                                  ОК')
except:
	print(u'Пустой блок не нажат                               ОШИБКА')
	driver.quit()
time.sleep(10)

numb = '.oe_form_pager_state'
num_b = driver.find_element_by_css_selector(numb)
amount = num_b.text
amount_first = re.search(r'^\d+', amount)
begin = int(amount_first.group(0))
# print(begin)
amount_last = re.search(r'[\d]+$', amount)
end = int(amount_last.group(0))
# print(end)

while begin < end:
	if begin != 1:
		time.sleep(12)

	num_b = driver.find_element_by_css_selector(numb)
	amount = num_b.text
	amount_first = re.search(r'^\d+', amount)
	begin = int(amount_first.group(0))
	print(u"Программа на странице №: {} из {} страниц".format(begin, end))

	element = driver.find_element_by_class_name(char_content)
	html = element.get_attribute("outerHTML")
	soup = BeautifulSoup(html, "html.parser")
	desired_text1 = soup.find("span", class_= char_content).next
	# print(desired_text1)
	if (desired_text1 == u'test' or desired_text1 == u'Test' or desired_text1 == u'Тест' or desired_text1 == u'тест'):
		print u"Тема работы: " + desired_text1 + u"                                  ОК"
	else:
		print u"Тема работы не соответсвует                        Пропускаем!"
		if begin == end:
			print u"Очистка закончена успешно!"
			break
		if begin < end:
			driver.find_element_by_xpath(arrow).click()
			print(u'Стрелка нажата                                     ОК')
			time.sleep(10)
		continue

	time.sleep(10)
	element1 = driver.find_element_by_class_name(text_content)
	html = element1.get_attribute("outerHTML")
	soup = BeautifulSoup(html, "html.parser")
	desired_text = soup.find("span", class_= text_content).next
	# print(desired_text)
	result1 = re.search(r'7{11}', desired_text)
	if result1:
		print(u"Номер телефона: " + result1.group(0))

	result2 = re.search(r'test\@test\.ru', desired_text)
	if result2:
		print(u"Почтовый ящик: " + result2.group(0))
	# Если result2 true, то только тогда принт. Если не поставить это условие, то когда result2 равен none возникает ошибка NoneType object has no attribute group

	result3 = re.search(r'test\@diplomtime\.ru', desired_text)
	if result3:
		print(u"Почтовый ящик: " + result3.group(0))

	time.sleep(2)	
	if (desired_text1 == u'test' or desired_text1 == u'Test' or desired_text1 == u'Тест' or desired_text1 == u'тест') and result1 and (result2 or result3):
		print u'Параметры соответствуют для удаления               ОК'
		driver.find_element_by_css_selector(button_edit).click()
	else:
		print u'Параметры не соответствуют для удаления            Пропускаем!'
		if begin == end:
			print u"Очистка закончена успешно!"
			break
		if begin < end:
			driver.find_element_by_xpath(arrow).click()
			print(u'Стрелка нажата                                     ОК')
		continue 


	time.sleep(2)	
	try:
		select = Select(driver.find_element_by_xpath(prichina_otkaza))
		select.select_by_visible_text('Тестовые заявки')
		print u'Выбран тип: Тестовые заявки                        ОК'
	except:
		print u'Выбран тип: Тестовые заявки                        ОШИБКА'
		driver.quit()

	time.sleep(2)	
	try:
		driver.find_element_by_css_selector(button_save).click()
		print u'Кнопка сохранить                                   ОК'
	except:
		print u'Кнопка сохранить                                   ОШИБКА'
		driver.quit()

	time.sleep(2)	
	try:
		driver.find_element_by_xpath(button_musor).click()							
		print u'Перемещено в мусор                                 ОК'
	except:
		print u'Перемещено в мусор                                 ОШИБКА'
		driver.quit()

	time.sleep(15)
	if begin == end:
		print u"Очистка закончена успешно!"
		break

	if begin < end:
		driver.find_element_by_xpath(arrow).click()
		print(u'Стрелка нажата                                     ОК')

	time.sleep(10)
