from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from timeit import default_timer as timer
from time import sleep
import termcolor
from termcolor import colored, cprint
import time
from time import sleep
import re
import sys
import os
import datetime
import pickle

# Created by Nelson Orellana (Nels2 @ GitHub), 2021.26.02
# This script is intened to grab todays(date ran) serviceboard to get an overview of tickets without having to login.
#
#
print_blue = lambda x: cprint(x, 'cyan')
print_yellow = lambda x: cprint(x, 'yellow')
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
url = "https://cw2.dcstopeka.com/v4_6_release/connectwise.aspx?fullscreen=false&locale=en_US#XQAACADDAwAAAAAAAAA9iIoG07$U9W$OXqU2f868IPYhCwZbCCkqIYRFHeyR$YSSk0sjl7aoF9AsnZZhVeOB946uvkjbEleT3$QSnKOPbfpwf5Rpm4pnPk1eG4JyNyw4s7vLKmXij22FiyTB2oZqWkMCXeweztjksT8JcyXpS28QKVqeMlfeQIvA6iv_pI0FYhAHuS0e3Vbt$Zuae_TWOIh8pyoekVhIeLWFUx_iHiIqFKZ0IFkX0MfeFPUaeW$zvKgRLesGKter7cZIwQmc4Y8195JVWByziRMs2$xmbn18d0ZwG_Ib9tkU6VB9_Ub4niPdSZ$nHIDC$UVoVEOC1Fb8ofrtjiSViR9pq753hcTAPM$PSGDKQQ4djIuGXbE1ZZ0YRUI$qlQONhHfCLrqlUVDP$dCYMDBOkko2Spdq3Z2q$tdG7BACM$b$uAF0IEoXGYAAqoKelgCSjAJ$$Bz93AIVMAy8miuOgfwl$8KxX3SNWL_84lOAA==??ServiceBoard"
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(url)

def CWlogind():
    comp = ''
    userd = ''
    pasd = ''

    u = driver.find_element_by_name('CompanyName')
    u.send_keys(comp)
    s = driver.find_element_by_name('UserName')
    s.send_keys(userd)
    p = driver.find_element_by_name('Password')
    p.send_keys(pasd)
    p.send_keys(Keys.RETURN)
    # clicking proceed so i can continue
    try:
        time.sleep(3)
        pro_clk = driver.find_element_by_xpath("//input[@value='Proceed']")
        pro_clk.click()
        print_yellow("#### -- Proceed was clicked -- ####")
    except NoSuchElementException: 
        pass
    print_green("#### -- Logged in! -- ####")
CWlogind()
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
status_of_tickets = driver.find_element_by_xpath('//*[@id="Description-input"]')
status_of_tickets.send_keys("New (Automate)")
status_of_tickets.send_keys(Keys.RETURN)
time.sleep(1)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
TotalAMTT = driver.find_element_by_css_selector(".GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
stri = TotalAMTT
Amt = stri.split("- ",1)[1]
stri = Amt
PGAmt = stri.split(" of",1)[0]
stri = TotalAMTT
Amts = stri.split("of ",1)[1]
print_yellow("#### -- Total Amount of Tickets Today Under the Alerts Board:      " + Amts + " -- ####")
print_yellow("#### -- Total Amount of Tickets Today Under the Alerts Board Page: " + PGAmt + " -- ####")
driver.implicitly_wait(2)

x = int(PGAmt) 
i = int(1)
while i < x:
    path2 = "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[2]" 
    if "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[2]" in path2:
        sreplacement = "/tr[" + str(i) + "]/td[2]"
        suni = path2.replace('/tr[1]/td[2]', sreplacement)
        path2 = suni
        pass
    path1 = "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[6]"
    if "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[6]" in path1:
        replacement = "/tr[" + str(i) + "]/td[6]"
        uni = path1.replace('/tr[1]/td[6]', replacement)
        path = uni
        pass
    TicketNumber = driver.find_element_by_xpath(path2).text
    Ticketlist = driver.find_element_by_xpath(path).text
    if 'Reboot' in Ticketlist:
        ticketT = 'Reboot Type'
        pass
    elif 'edgeupdate' in Ticketlist:
        ticketT = 'edgeupdate Type'
        pass
    elif 'Disk Cleanup' in Ticketlist:
        ticketT = 'Disk Cleanup Type'
        pass
    elif 'NIC' in Ticketlist:
        ticketT = 'NIC Type'
        pass
    print_yellow('Ticket Number# & Type: ' + TicketNumber + ' & ' + ticketT)
    print_blue('Ticket Information: ' + Ticketlist)
    i += 1
    pass
print('#### -- End of Ticket List for this Page'+ '(' + PGAmt + ' of '+ Amts + ') -- ####')