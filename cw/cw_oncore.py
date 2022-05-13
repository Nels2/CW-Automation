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
from cw_howto import cwLogind, serverConnect, startTym, grabClientInfo, grabTicketInfo, identify_POP, identify_VIP, lookForNewTixOnly, itGlueLogind, driver, pickle, os, pathlib, datetime, colored, cprint, EC, By, S_er, E_er, WDE_er, print_blue, timer, print_alt_yellow, print_green, print_red, print_yellow, print_alt_green
# USE ONLY FOR oncore TICKETS!!!
#
#
#  --------------ConnectWise AutoBot, By Nels2----------------------------
# 
#
# ---------------Built 2022.05.12 ------------------------------------------
# --------------------------------------------------------------------------
webdriver = driver
startTym()# Start timer to keep track of how long script takes to run.
serverConnect()#connect to my chat site to keep records of the work BrinxBot does.
cwLogind()# logs into ConnectWise.
clientVIPStatus = False # this will show to be relevant later...
# loads page then clicks on summary description input field and looks for the specifced ticket.    
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
search = driver.find_element(by=By.XPATH, value="//input[@id='Summary-input']")
ticket_type = '*On-Core*'  # service tickets where a backup is missed
pickle.dump( ticket_type, open( "ticket_info.p", "wb"))
ticket_type = pickle.load( open( "ticket_info.p", "rb"))
time.sleep(0.5)
lookForNewTixOnly()
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
# identify if there is a pop up on the screen, if so to close it.
identify_POP()
#identify if client is VIP or not.
identify_VIP()
# --grabbing client information-- 
grabClientInfo()
# -- grabbing ticket information --
grabTicketInfo()
url_third = driver.current_url
driver.quit()
# end