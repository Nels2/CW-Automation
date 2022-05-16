from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from cw_howto import cwLogind, cwTicketTypeSearch, serverConnect, startTym, clickOnTicket, grabClientInfo, grabTicketInfo, saveCurrentWebLink, identify_POP, identify_VIP, lookForNewTixOnly, itGlueLogind, itGlueSearch, driver, pickle, os, pathlib, datetime, colored, cprint, EC, AC, By, S_er, E_er, WDE_er, print_blue, timer, sys, print_alt_yellow, print_green, print_red, print_yellow, print_alt_green
import time
from time import sleep
import re
# USE ONLY FOR oncore TICKETS!!!
#  --------------ConnectWise AutoBot, By Nels2----------------------------
# 
# ---------------Built 2022.05.12 ------------------------------------------
# --------------------------------------------------------------------------
webdriver = driver
startTym()# Start timer to keep track of how long script takes to run.
serverConnect()#connect to my chat site to keep records of the work BrinxBot does.
cwLogind()# logs into ConnectWise.
lookForNewTixOnly()
clientVIPStatus = False # this will show to be relevant later...
ticket_type = '*On-Core*'  # service tickets where a backup is missed
pickle.dump( ticket_type, open( "ticket_info.p", "wb"))
cwTicketTypeSearch()# let the field populate... then searches for tickets that start with "On-Core" then clicks on the first one
clickOnTicket()#Next is viewing what the ticket is about to make sure it is correct before continuing...
identify_POP()# identify if there is a pop up on the screen, if so to close it.
print("#### -- Downloading Ticket & Client Information ... -- ####")
identify_VIP()#identify if client is VIP or not.
grabClientInfo()# --grabbing client information-- 
grabTicketInfo()# -- grabbing ticket information --
saveCurrentWebLink() # saves current ticket page's link for future use.
itGlueLogind()# logs into IT Glue
itGlueSearch()# Searches in IT Glue for the company that was in the ticket.