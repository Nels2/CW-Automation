import cw_oncore
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
from cw_howto import cwLogind, serverConnect, startTym, itGlueLogind, driver, pickle, os, pathlib, datetime, colored, cprint, EC, By, S_er, E_er, WDE_er, print_blue, timer, print_alt_yellow, print_green, print_red, print_yellow, print_alt_green
#
# cw_itgluegrab.py
#  logs into it glue to fetch support documents for whatever ticket BrinxBot is looking at.
#  created: 2022.05.13
#  By: Nels2 
# 
# 

itGlueLogind()
driver.implicitly_wait(5)
searchFor = driver.find_element(by=By.XPATH, value ='/html/body/div[1]/section/div/div/div/div[3]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/span/div/label/div/div/input')
searchFor.send_keys(cw_oncore.companyN)


# select first listed company... 
enterCompanyProfile = driver.find_element(by=By.CSS_SELECTOR, value ='td.column-name').click()
driver.implicitly_wait(5)
print_green("#### -- The page for "+cw_oncore.companyN+" in IT Glue, has loaded successfully! -- ####")
# select document side bar item to load documents for company.
loadDocPage = driver.find_element(by=By.CSS_SELECTOR, value ='li.sidebar-item:nth-child(6)').click()
#end timer that started in cw_oncore.py
end = timer()
print('Script Completion Time:'+ str(end-cw_oncore.start))