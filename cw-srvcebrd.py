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
print_blue = lambda x: cprint(x, 'white', attrs=['bold'])
print_yellow = lambda x: cprint(x, 'yellow')
print_alt_yellow = lambda x: cprint(x, 'yellow', attrs=['underline'])
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
    except ElementNotInteractableException:
        pass
    except NoSuchElementException: 
        pass
    print_green("#### -- Logged in! -- ####")
CWlogind()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
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
os.remove("ticket_types.txt")
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
    if 'Reboot' in Ticketlist or 'UPDATES - Reboot Pending' in Ticketlist:
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
    elif 'UPDATES -  Out of date' in Ticketlist or 'UPDATES - Out of date' in Ticketlist:
        ticketT = 'Out of Date PC'
        pass
    elif 'No Checkin' in Ticketlist:
        ticketT = 'Out of Date PC'
        pass
    elif 'Webroot Process Not Running' in Ticketlist:
        ticketT = 'WebRoot Error'
        pass
    elif 'Unclassified Apps' in Ticketlist:
        ticketT = 'Unclassified App Warning'
        pass
    elif 'Perf - Processor Queue Length' in Ticketlist:
        ticketT = 'Perf Type Ticket'
        pass
    elif 'Software Uninstalled' in Ticketlist or 'Get Product Keys Script Failed' in Ticketlist :
        ticketT = 'No Time Entry Needed'
        pass
    else:
        ticketT = 'Unknown'
        pass
    with open('ticket_types.txt', 'a') as f:
        print("Ticket Type: ", ticketT, file=f)
    print_alt_yellow('Ticket Number[#] & Type: ' + TicketNumber + ' & ' + ticketT + ": ") 
    print_blue('>> Ticket Information: ' + Ticketlist)
    i += 1
    pass
driver.quit()
total_egu = 0
total_dc = 0
total_reb = 0
total_nic = 0
total_OD = 0
total_PT = 0
total_UA = 0
total_NTEN = 0
total_WE = 0
total_UT = 0
with open('ticket_types.txt') as f:
    for line in f:
        found_egu = line.find('edgeupdate Type')
        if found_egu != -1 and found_egu != 0:
            total_egu += 1
        found_dc = line.find('Disk Cleanup Type')
        if found_dc != -1 and found_dc != 0:
            total_dc += 1
        found_nic = line.find('NIC Type')
        if found_nic != -1 and found_nic != 0:
            total_nic += 1
        found_reb = line.find('Reboot Type')
        if found_reb != -1 and found_reb != 0:
            total_reb += 1
        found_OD = line.find('Out of Date PC')
        if found_OD != -1 and found_OD != 0:
            total_OD += 1
        found_PT = line.find('Perf Type Ticket')
        if found_PT != -1 and found_PT != 0:
            total_PT += 1
        found_UA = line.find('Unclassified App Warning')
        if found_UA != -1 and found_UA != 0:
            total_UA += 1
        found_NTEN = line.find('No Time Entry Needed')
        if found_NTEN != -1 and found_NTEN != 0:
            total_NTEN += 1
        found_WE = line.find('WebRoot Error')
        if found_WE != -1 and found_WE != 0:
            total_WE += 1
        found_UT = line.find('Unknown')
        if found_UT != -1 and found_UT != 0:
            total_UT += 1
print('#### -- End of Ticket List for this Page'+ '(' + PGAmt + ' of '+ Amts + ') -- ####')
print_yellow('#### -- Total Amount of Each Ticket Type Today: -- ####')
print_blue("|    Out of Date PC:                             "+str(total_OD)+"    | ")
print_blue("|    Unknown:                                    "+str(total_UT)+"    | ")
print_blue("|    WebRoot Error Type:                         "+str(total_WE)+"    | ")
print_blue("|    Perf Warning Type:                          "+str(total_PT)+"    |")
print_blue("|    Unclassified App Warning:                   "+str(total_UA)+"    |")
print_blue("|    No Time Entry Needed:                       "+str(total_NTEN)+"    |")
print_yellow('#### --   Ticket Types That BrinxBot Can Work:  -- ####')
print_blue("|    Reboot Type:                                "+str(total_reb)+"    | ")
print_blue("|    EdgeUpdate Type:                            "+str(total_egu)+"    | ")
print_blue("|    Disk Cleanup Type:                          "+str(total_dc)+"    | ")
print_blue("|    NIC Type:                                   "+str(total_nic)+"    |")
print_yellow('#### --------------------------------------------- ####')