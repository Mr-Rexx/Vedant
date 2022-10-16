# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:01:02 2022

@author: Vedan
"""
import requests
from bs4 import BeautifulSoup 

URL = "https://www.demoblaze.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

from selenium import webdriver
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
source =driver.get('https://analyticsindiamag.com/')
source_code=driver.page_source

soup = BeautifulSoup(source_code,'lxml')
article_block =soup.find_all('div',class_='post-title')

for titles in article_block:
	title =titles.find('span').get_text()
	print(title)
    
    