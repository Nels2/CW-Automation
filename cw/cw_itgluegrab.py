import cw_oncore
import cw_howto
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
import time
from time import sleep
import re
import sys
from cw_howto import cwLogind, grabClientInfo, serverConnect, startTym, itGlueLogind, driver, pickle, os, pathlib, datetime, colored, cprint, EC, By, S_er, E_er, WDE_er, print_blue, timer, print_alt_yellow, print_green, print_red, print_yellow, print_alt_green
#
# cw_itgluegrab.py
#  logs into it glue to fetch support documents for whatever ticket BrinxBot is looking at.
#  created: 2022.05.13
#  By: Nels2 
# 

itGlueLogind()
companyNameImport = pickle.load( open( "tickets/ticket_info/companyName.p", "rb"))
driver.implicitly_wait(3)

# select first listed company... 
searchFor = driver.find_element(by=By.CSS_SELECTOR, value ='label.form-label:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
driver.implicitly_wait(2)
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.react-table-body > div:nth-child(1)')))
driver.implicitly_wait(10)
# send again so it is actually pasted into the search field.....
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.react-table-body > div:nth-child(1)')))
#click company 
searchFor.send_keys(companyNameImport)
enterCompanyProfile = driver.find_element(by=By.CSS_SELECTOR, value ='td.column-name').click()
driver.implicitly_wait(3)
print_green("#### -- The page for "+companyNameImport+" in IT Glue, has loaded successfully! -- ####")
# select document side bar item to load documents for company.
loadDocPage = driver.find_element(by=By.CSS_SELECTOR, value ='li.sidebar-item:nth-child(6)').click()
print_green("#### -- Current on "+companyNameImport+"'s Documents page. -- ####")
#end timer that started in cw_oncore.py
end = timer()
startImport = pickle.load( open( "startTime.p", "rb"))
print_red('Script Completion Time:'+ str(end-startImport)+ " seconds.")


