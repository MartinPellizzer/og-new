from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

import re
import os
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas

import sys
import csv

driver = None

sep = '\\'


######################################################################################
# CSV
######################################################################################
def get_old_businesses(output_file):
	global sep
	if not os.path.isfile(output_file): 
		with open(output_file, 'w', encoding="utf-8") as f:
			return []
	else:
		with open(output_file, 'r', encoding="utf-8") as f:
			return [line.split(sep)[0] for line in f.readlines()]


######################################################################################
# STRINGS
######################################################################################
def sanitize(text):
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.-()\'&@ '
	encoded_string = text.encode('ascii', 'ignore')
	decoded_string = encoded_string.decode()
	text = ''
	for c in decoded_string:
		if c in chars:
			text += c
	return text


######################################################################################
# EMAILS
######################################################################################
def find_contact_url(url):
	contact_page = ''

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')

	for link in soup.find_all('a'):
		if 'contatti' in str(link).lower():
			link = link.get('href')
			contact_page = link
	
	return contact_page


def scrape_emails(url):
	emails = set()

	regex_string = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

	# homepage
	try: 
		# print('finding contact url...')
		response = requests.get(url)
		# print(response)
		matches = re.finditer(regex_string, response.text)
		for match in matches: emails.add(match.group())
	except: return emails

	# contact page 1
	try:
		# print('finding contact url...')
		contact_page = find_contact_url(url)
		response = requests.get(contact_page)
		# print(response)
		matches = re.finditer(regex_string, response.text)
		for match in matches: emails.add(match.group())
	except: return emails
	
	# print('done scraping website')
	return emails
	
######################################################################################
# BROWSER
######################################################################################
# def open_browser():
# 	global driver
# 	options = Options()
# 	# options.add_argument('--headless')
# 	options.add_argument('--disable-gpu')
# 	driver = webdriver.Chrome(r'C:\drivers\chromedriver', options=options)
# 	driver.maximize_window()
# 	driver.get('https://www.google.com')
# 	sleep(2)
# 	driver.find_element(By.XPATH, '//div[text()="Rifiuta tutto"]').click()
# 	sleep(2)


def open_browser():
	global driver
	driver = webdriver.Firefox()
	driver.maximize_window()
	driver.get('https://www.google.com')
	sleep(2)
	driver.find_element(By.XPATH, '//div[text()="Rifiuta tutto"]').click()
	sleep(2)


def scroll_down_up_down():
	global driver
	try: feed = driver.find_element(By.XPATH, '//div[@role="feed"]')
	except: return
	feed.send_keys(Keys.PAGE_DOWN)
	sleep(2)
	feed.send_keys(Keys.PAGE_UP)
	sleep(2)
	feed.send_keys(Keys.PAGE_DOWN)
	sleep(2)


def search(search_text):
	driver.get(f'https://www.google.com/maps/search/{search_text}')


def click_on_listing(business):
	for _ in range(3):
		try: 
			business.click()
			return True
		except: 
			print('error click')
			continue
	return False


######################################################################################
# SCRAPE
######################################################################################
def get_card_element(e):
	try: return e.find_elements(By.XPATH, '//div[@role="main"]')[1]
	except: return None


def scrape_name(e):
	try: return e.find_element(By.XPATH, './/h1').text
	except: return ''
	

def scrape_address(e):
	try: return e.find_element(By.XPATH, './/button[@data-item-id="address"]').text
	except: return ''


def scrape_district(e):
	try: return e.find_element(By.XPATH, './/button[@data-item-id="address"]').text.split(' ')[-1]
	except: return ''


def scrape_website(e):
	try: return e.find_element(By.XPATH, './/a[@data-item-id="authority"]').get_attribute("href")
	except: return ''


def scrape_phone(e):
	try: return e.find_element(By.XPATH, './/button[contains(@data-item-id, "phone")]').text
	except: return ''




def find_new_business(old_businesses):
	global driver
	try: feed = driver.find_element(By.XPATH, '//div[@role="feed"]')
	except: return None, None
	items = feed.find_elements(By.XPATH, './/a/..')
	for item in items:
		a = item.find_element(By.XPATH, './/a')
		a_href = a.get_attribute('href')
		if 'support.' in a_href: continue
		if 'google.' not in a_href: continue
		if '/maps/' not in a_href: continue
		label = a.get_attribute('aria-label')
		label = sanitize(label)
		label = label.replace('Link visitato', '')
		if label not in old_businesses:
			return item, label
	return None, None



def debug_info(name, address, district, website, phone, emails):
	print(f'{"Name:":<8} {name}')
	print(f'{"Address:":<8} {address}')
	print(f'{"District:":<8} {district}')
	print(f'{"Website:":<8} {website}')
	print(f'{"Phone:":<8} {phone}')
	print(f'{"Emails:":<8} {emails}')
	print(f'{"":->64}')
	print()


def add_business_to_csv(output_file, label, address, website, phone, s_emails, district, name):
	string_to_write = ''
	string_to_write += f'{label}{sep}'
	string_to_write += f'{address}{sep}'
	string_to_write += f'{website}{sep}'
	string_to_write += f'{phone}{sep}'
	string_to_write += f'{s_emails}{sep}'
	string_to_write += f'{district}{sep}'
	string_to_write += f'{name}\n'

	with open(output_file, 'a', encoding="utf-8") as f:
		f.write(string_to_write)
		

def scrape_new_business(search_text, search_industry, search_district, i):
	global sep

	output_file = f'./exports/{search_industry}-{search_district}.csv'.replace(' ', '_')

	old_businesses = get_old_businesses(output_file)
	business, label = find_new_business(old_businesses)
	print(f'{i}: {label}')

	if not business:
		scroll_down_up_down()
		return 'no_new_business_found'

	# google maps is bugged: scroll a bit the screen and try clicking again if needed
	if not click_on_listing(business):
		scroll_down_up_down()
		return 'failed_to_click_listing'

	# TODO: if time is not enough to open new card, manage it
	# otherwise it will take business info from previous card, which is wrong!!!
	sleep(5)
	
	card_element = get_card_element(business)

	name = scrape_name(card_element)
	address = scrape_address(card_element)
	district = scrape_district(card_element)
	website = scrape_website(card_element)
	phone = scrape_phone(card_element)
	emails = scrape_emails(website)
	s_emails = ' '.join(emails)

	# if search_district.lower().strip() != district.lower().strip():
	# 	return 'NO MATCH: District'

	name = sanitize(name)
	address = sanitize(address)
	district = sanitize(district)
	phone = sanitize(phone)

	if name != label:
		add_business_to_csv(output_file, label, address, website, phone, s_emails, district, name)
		return 'name_not_equal_label'

	add_business_to_csv(output_file, label, address, website, phone, s_emails, district, '')

	debug_info(name, address, district, website, phone, s_emails)

	return 'success'
	




# # open_browser()

# provincia = 'TV'
# industry = 'salumifici'

# # GET COMUNI FROM PROVINCIA
# with open('comuni.csv', 'r', encoding="utf-8") as f: comuni = [line.split(sep) for line in f.readlines()]
# comuni_filtered = [line for line in comuni if line[2].strip().lower() == provincia.strip().lower()]

# for i, comune in enumerate(comuni_filtered):
# 	print(comune)
# 	comune_nome = comune[1]
# 	search_text = f'{industry} {comune_nome.lower()}'
# 	search(search_text)
# 	sleep(10)
# 	if i >= 3: break




# search(search_text)

# for i in range(30):
# 	err = scrape_new_business(search_text, i)
# 	print(err, '\n')
# 	if err == 'name_not_equal_label': break

# quit()












######################################################################################
# MAIN
######################################################################################
def main():
	search_industry = input('Inserisci il settore (es. salumifici): ')
	search_district = input('Inserisci la provincia (es. TV): ')
	scrapes_num = int(input('Inserisci il numero di azioni (es. 30): '))

	# search_industry = 'caseifici'
	# search_district = 'BO'
	# scrapes_num = 20

	# GET COMUNI FROM PROVINCIA
	with open('comuni.csv', 'r', encoding="utf-8") as f: comuni = [line.split(sep) for line in f.readlines()]
	comuni_filtered = [line for line in comuni if line[2].strip().lower() == search_district.strip().lower()]

	open_browser()
	# search(search_text)
	
	for i, comune in enumerate(comuni_filtered):
		print('*********************************')
		print(comune)
		print(f'{i}/{len(comuni_filtered)}')
		print('*********************************')

		comune_nome = comune[1]
		search_text = f'{search_industry} {comune_nome.lower()}'
		search(search_text)
		sleep(10)
		# if i >= 3: break

		for k in range(scrapes_num):
			err = scrape_new_business(search_text, search_industry, search_district, k)
			print(err, '\n')
			# if err == 'name_not_equal_label': break

	driver.quit()

main()


# search_text = 'salumifici parma'

# open_browser()
# search(search_text)

# for i in range(30):
# 	err = scrape_new_business(search_text, i)
# 	print(err, '\n')
# 	if err == 'name_not_equal_label': break



# output_file = f'./exports/{search_text}.csv'.replace(' ', '_')

# old_businesses = get_old_businesses(output_file)
# business, label = find_new_business(old_businesses)

# card_element = get_card_element(business)
# e.find_element(By.XPATH, './/h1').text
















# search_industry = 'caseifici'
# search_district = 'MO'
# scrapes_num = 10

# # GET COMUNI FROM PROVINCIA
# with open('comuni.csv', 'r', encoding="utf-8") as f: comuni = [line.split(sep) for line in f.readlines()]
# comuni_filtered = [line for line in comuni if line[2].strip().lower() == search_district.strip().lower()]

# for i, comune in enumerate(comuni_filtered):
# 	print('*********************************')
# 	print(comune)
# 	print(f'{i}/{len(comuni_filtered)}')
# 	print('*********************************')

# 	comune_nome = comune[1]
# 	search_text = f'{search_industry} {comune_nome.lower()}'
# 	search(search_text)
# 	sleep(10)
# 	# if i >= 3: break

# 	for k in range(scrapes_num):
# 		err = scrape_new_business(search_text, search_industry, search_district, k)
# 		print(err, '\n')
# 		# if err == 'name_not_equal_label': break

# 	break

# search_industry = 'caseifici'
# search_district = 'MO'
# scrapes_num = 6


# for k in range(scrapes_num):
# 	output_file = f'./exports/{search_industry}-{search_district}.csv'.replace(' ', '_')

# 	old_businesses = get_old_businesses(output_file)
# 	business, label = find_new_business(old_businesses)
# 	print(f'{k}: {label}')
# 	print(f'{business}')