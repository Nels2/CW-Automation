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
from cw_howto import cwLogind, serverConnect, startTym, companyCheck, itGlueLogind, driver, pickle, os, pathlib, datetime, colored, cprint, EC, By, S_er, E_er, WDE_er, print_blue, timer, print_alt_yellow, print_green, print_red, print_yellow, print_alt_green
# USE ONLY FOR oncore TICKETS!!!
#
#
#  --------------ConnectWise AutoBot, By Nels2----------------------------
# 
#
# ---------------Built 2022.05.12 ------------------------------------------
# --------------------------------------------------------------------------
webdriver = driver
startTym()
serverConnect()
cwLogind()
# so page can load then clicks on summary description and looks for the specifced ticket.    
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
search = driver.find_element(by=By.XPATH, value="//input[@id='Summary-input']")
ticket_type = '*On-Core*'  # service tickets where a backup is missed
pickle.dump( ticket_type, open( "ticket_info.p", "wb"))
ticket_type = pickle.load( open( "ticket_info.p", "rb"))
time.sleep(0.5)
status_of_tickets = driver.find_element(by=By.XPATH, value="//*[@id='Description-input']")
status_of_tickets.send_keys("New")
time.sleep(1)
search.send_keys(ticket_type)
ticket_type = '*BM*'
search.send_keys(Keys.RETURN)
# let the field populate... then searches for tickets that start with "On-Core" then clicks on the first one
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
try:
    driver.implicitly_wait(4.25)
    ticket = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[7]/div/a").click()
    action = ActionChains(driver)
    action.double_click(ticket)
    pass
except E_er:
    print_yellow("#### -- Appears to be last ticket of this type("+ticket_type+"). -- ####")
    pass
except NoSuchElementException:
    print_yellow('#### -- Trying again...  -- ####')
    driver.implicitly_wait(1)
    try:
        ticket = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[7]/div/a").click()
        action = ActionChains(driver)
        action.double_click(ticket)
    except NoSuchElementException:
        print_red('#### -- There were no ticket founds for ticket type: ' + ticket_type + ' -- #####')
        print_yellow('#### -- !! Exiting.. !! -- ####')
        sys.exit()
        pass
    except E_er:
        print_yellow('#### -- Ticket Function 2 Was Not Used!(NO TICKET FOUND) -- ####')
        pass
        #Next is viewing what the ticket is about to make sure it is correct before continuing...
#-Now to click on new note and begin the process of TRUE automation without CW's semi useless scripting...
time.sleep(0.2)
#identify pop up
popUp = driver.find_elements(by=By.CSS_SELECTOR, value='#x-auto-282')
#get list size
size = len(popUp)
#check condition
if(size>0):
    print_blue("There is a pop up.. closing...")
    closePopUp = driver.find_element(by=By.XPATH, value ="/html/body/div[6]/div[2]/div[1]/div/div/div[2]/div/div/div").click()
else:
    print_blue("no pop this time")
#identify if ticket is VIP or not.
#vipCheck = driver.find_elements(by=By.CSS_SELECTOR, value='#x-auto-3')
#get list size again
#sized = len(vipCheck)
#check condition
#if(sized>0):
#    print_yellow("#### -- Client is VIP! -- ####")
#    clientVIPStatus = True
#else:
#    print_blue("#### -- Client is not VIP. -- ####")
#    clientVIPStatus = False
# --grabbing client information-- 
print("#### -- Downloading Client Information ... -- ####")
print_alt_yellow("#### -- Client Information: -- ####")
companyN = driver.find_element(by=By.ID, value='x-auto-183-input')
print_blue("Company: "+companyN.get_attribute('value'))
contactN = driver.find_element(by=By.ID, value='gwt-uid-156')
print_blue("Contact: "+contactN.get_attribute('value'))
emailN = driver.find_element(by=By.ID, value='gwt-uid-157')
print_blue("Email: "+emailN.get_attribute('value'))
addressOne= driver.find_element(by=By.ID, value='gwt-uid-160')
cityLo = driver.find_element(by=By.ID, value='gwt-uid-162')
stateLo = driver.find_element(by=By.ID, value='x-auto-184-input')
zipLo =  driver.find_element(by=By.ID, value='gwt-uid-163')
print_blue("Address: "+addressOne.get_attribute('value') + '   '+ (cityLo.get_attribute('value')+', ' +stateLo.get_attribute('value') +'   '+ (zipLo.get_attribute('value'))))
print_alt_yellow("#### --*-*-*-*-*-*-*-*-*-*--- ####")
# -- grabbing ticket information --
print("#### -- Downloading Ticket Information ... -- ####")
print_alt_yellow("#### -- Ticket Information: -- ####")
ticketNum = driver.find_element(by=By.CSS_SELECTOR, value='#x-auto-186-label').text
ageOfTicket = driver.find_element(by=By.CSS_SELECTOR, value='.GE0S-T1CK0M > b:nth-child(1)').text
print_blue("Number[#] & Age: "+ ticketNum + " | " + ageOfTicket)
boardT = driver.find_element(by=By.ID, value='x-auto-187-input')
print_blue("Ticket Board: "+boardT.get_attribute('value'))
statusT = driver.find_element(by=By.ID, value='x-auto-189-input')
print_blue("Ticket Status: "+statusT.get_attribute('value'))
typeofT = driver.find_element(by=By.ID, value='x-auto-190-input')
print_blue("Ticket Type: "+typeofT.get_attribute('value'))
ticketDescriptionA = driver.find_element(by=By.CSS_SELECTOR, value='.TicketNote-initialNote > div:nth-child(6) > div:nth-child(1) > label:nth-child(1) > p:nth-child(1)').text
print_blue("Ticket Full Description: "+ticketDescriptionA)
try:
    ticketDescriptionB = driver.find_element(by=By.CSS_SELECTOR, value='.TicketNote-initialNote > div:nth-child(6) > div:nth-child(1) > label:nth-child(1) > p:nth-child(2)').text
    print_blue(ticketDescriptionB)
except NoSuchElementException:
    pass
print_alt_yellow("#### --*-*-*-*-*-*-*-*-*-*--- ####")
# now to scroll the view down.. hopefully!
try:
    grab = driver.find_element_by_name('html')
    grab.send_keys(Keys.PAGE_DOWN)
except NoSuchElementException:
    grab = driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# also need to save what ticket is about so BrinxBot isn't lost..