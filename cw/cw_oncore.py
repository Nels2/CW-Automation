from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
import time
from time import sleep
import re
from cw_howto import cwLogind, serverConnect, startTym, clickOnTicket, grabClientInfo, grabTicketInfo, identify_POP, identify_VIP, lookForNewTixOnly, itGlueLogind, itGlueSearch, driver, pickle, os, pathlib, datetime, colored, cprint, EC, AC, By, S_er, E_er, WDE_er, print_blue, timer, sys, print_alt_yellow, print_green, print_red, print_yellow, print_alt_green
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
clickOnTicket()
#Next is viewing what the ticket is about to make sure it is correct before continuing...
# identify if there is a pop up on the screen, if so to close it.
identify_POP()
print("#### -- Downloading Ticket & Client Information ... -- ####")
#identify if client is VIP or not.
identify_VIP()
# --grabbing client information-- 
grabClientInfo()
# -- grabbing ticket information --
grabTicketInfo()
url_third = driver.current_url
# this was inside cw_itgluegrab.py moved it here as it really can just be a function instead of whole other file.
itGlueLogind()# logs into IT Glue
itGlueSearch()# Searches in IT Glue for the company that was in the ticket.