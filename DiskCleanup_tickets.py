from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import timeit
import termcolor
from termcolor import colored, cprint
from time import sleep
import time
import pickle
# USE ONLY FOR DISK CLEANUP TICKETS!!!
#
#
#  --------------ConnectWise Automator, By Nelson Orellana -----------------
#
# Introducing a selenium + python script that logs into my ConnectWise, varies what it(where it is the ticket type) looks for depending on user input.
#
# ---------------Built 2021.01.27 ------------------------------------------
print_blue = lambda x: cprint(x, 'cyan')
print_yellow = lambda x: cprint(x, 'yellow')
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
def startTym():
    start = timeit.timeit()
    print_yellow(start)
    pickle.dump( start, open( "startTime.p", "wb"))
def Server_Connect():
    try:
        print_yellow("#### -- Establishing External Connection to Server .. -- ####")
        the_url = "https://bruhboxchat.nels277.repl.co/BrinxBot"
        options = webdriver.FirefoxOptions()
        options.headless = True
        driverTwo = webdriver.Firefox(options=options)
        driverTwo.get(the_url)
        time.sleep(1)
        Connection = driverTwo.find_element_by_css_selector("#message")
        Connection.send_keys("/name BrinxBot" + Keys.RETURN)
        Connection.send_keys("Connection has been established..." + Keys.RETURN)
        print_green("#### -- SUCCESS -- #####")
    except WebDriverException:
        print_red("#### -- FAIL -- ####")
        print_red("Server Connection Failed. No login was made to the Server. Continuing...")
    driverTwo.quit()
Server_Connect()

url = "https://cw2.dcstopeka.com/v4_6_release/connectwise.aspx?fullscreen=false&locale=en_US#XQAACADDAwAAAAAAAAA9iIoG07$U9W$OXqU2f868IPYhCwZbCCkqIYRFHeyR$YSSk0sjl7aoF9AsnZZhVeOB946uvkjbEleT3$QSnKOPbfpwf5Rpm4pnPk1eG4JyNyw4s7vLKmXij22FiyTB2oZqWkMCXeweztjksT8JcyXpS28QKVqeMlfeQIvA6iv_pI0FYhAHuS0e3Vbt$Zuae_TWOIh8pyoekVhIeLWFUx_iHiIqFKZ0IFkX0MfeFPUaeW$zvKgRLesGKter7cZIwQmc4Y8195JVWByziRMs2$xmbn18d0ZwG_Ib9tkU6VB9_Ub4niPdSZ$nHIDC$UVoVEOC1Fb8ofrtjiSViR9pq753hcTAPM$PSGDKQQ4djIuGXbE1ZZ0YRUI$qlQONhHfCLrqlUVDP$dCYMDBOkko2Spdq3Z2q$tdG7BACM$b$uAF0IEoXGYAAqoKelgCSjAJ$$Bz93AIVMAy8miuOgfwl$8KxX3SNWL_84lOAA==??ServiceBoard"
driver = webdriver.Firefox()
driver.get(url)

# change the below fields to match your login info for YOUR connectwise site as well as the URL above it is specific to my login page.
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
# so page can load then clicks on summary description and looks for the specifced ticket.    
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
search = driver.find_element_by_xpath("//input[@id='Summary-input']")
ticket_type = 'OP3'
ticket_type = '*Disk Cleanup*' # service tickets where a disk clean up is needed
pickle.dump( ticket_type, open( "ticket_info.p", "wb"))
ticket_type = pickle.load( open( "ticket_info.p", "rb"))
time.sleep(0.5)
search.send_keys(ticket_type)
search.send_keys(Keys.RETURN)
# let the field populate... then searches for tickets that start with "UPDATES" then clicks on the first one
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
try:
    time.sleep(3)
    ticket = driver.find_element_by_css_selector("tr.GE0S-T1CGWF:nth-child(1) > td:nth-child(6) > div:nth-child(1) > a:nth-child(1)").click()
    action = ActionChains(driver)
    action.double_click(ticket)
except ElementNotInteractableException:
    pass
    print_yellow('#### -- Ticket Function Was Not Used! -- ####')
#Next is viewing what the ticket is about to make sure it is correct before continuing...
#-Now to click on new note and begin the process of TRUE automation without CW's semi useless scripting...
time.sleep(0.2)
# now to scroll the view down.. hopefully!
try:
    grab = driver.find_element_by_name('html')
    grab.send_keys(Keys.PAGE_DOWN)
except NoSuchElementException:
    grab = driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# also need to save what ticket is about so BrinxBot isn't lost..
time.sleep(2)
# break text up so I only have computer name so brinxbot can look it up.
try:
    Mark_Resolved = driver.find_element_by_name('GE0S-T1COTH GE0S-T1CJUH cw_status')
    pass
except NoSuchElementException:
        Mark_Resolved = driver.find_element_by_css_selector('#x-auto-200-input') # sometimes the input changes, dont know why.(Referring to Line 141.)
        pass
Mark_Resolved.click()
Mark_Resolved.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
Mark_Resolved.send_keys('Resolved' + Keys.RETURN)
print_green("[BrinxBot]: Marked as Resolved.")
def company():
    if 'Fanestil Meats' in ci_complete:
            print_yellow("#### -- renaming " + ci_complete + " to just 'Fanestil' as 'Fanestil Meats' does not exist in Automate")
            replaced = ci_complete.replace(' Meats', " ")
            ci_complete = replaced
            pass
    elif 'SR Coffman Construction' in ci_complete:
        print_yellow("#### -- renaming " + ci_complete + " to just 'Coffman Construction' as 'SR Coffman Construction' does not exist in Automate")
        replaced = ci_complete.replace('SR Coffman Construction Inc.', "Coffman Construction")
        ci_complete = replaced
        pass
    elif 'Bluestem Insurance Group' in ci_complete:
        print_yellow("#### -- renaming " + ci_complete + " to just 'Bluestem Insurance' as 'Bluestem Insurance Group' does not exist in Automate")
        replaced = ci_complete.replace('Bluestem Insurance Group', "Bluestem Insurance")
        ci_complete = replaced
        pass
    elif 'Dr. Marlin Flanagin, DDS' in ci_complete:
        print_yellow("#### -- renaming " + ci_complete + " to just 'Dr. Marlin Flanagin' as 'Dr. Marlin Flanagin, DDS' does not exist in Automate")
        replaced = ci_complete.replace('Dr. Marlin Flanagin, DDS', "Dr. Marlin Flanagin")
        ci_complete = replaced
        pass
    elif 'Lyon County Title LLC' in ci_complete:
        print_yellow("#### -- renaming " + ci_complete + " to just 'Lyon Co Title' as 'Lyon County Title LLC' does not exist in Automate")
        replaced = ci_complete.replace('Lyon County Title LLC', "Lyon Co Title")
        ci_complete = replaced
        pass
    elif 'Diamond Everley Roofing' in ci_complete:
        print_yellow("#### -- renaming " + ci_complete + " to just 'Diamond Everley' as 'Diamond Everley Roofing' does not exist in Automate")
        replaced = ci_complete.replace('Diamond Everley Roofing', "Diamond Everley")
        ci_complete = replaced
        pass
    elif 'Lore & Hagemann, Inc' in ci_complete:
        print_yellow("#### -- renaming " + ci_complete + " to just 'Lore & Hagemann' as 'Lore & Hagemann, Inc' does not exist in Automate")
        replaced = ci_complete.replace('Lore & Hagemann, Inc', "Lore & Hagemann")
        ci_complete = replaced
        pass
    else:
        pass
def computerz():
    if ticket_type == '*Disk Cleanup*':
        time.sleep(0.5)
        ticket_info = driver.find_element_by_css_selector(".GE0S-T1CHBL").text
        print_yellow("#### -- " + ticket_info + " -- ####")
        pickle.dump( ticket_info, open( "ticket.p", "wb"))
        try:
            str = ticket_info
            z = str.split("for ",2)[1]
            str = z
            computer = str.split(" at ",1)[0]
        except IndexError:
            str = ticket_info
            z = str.split("detected ",2)[1]
            str = z
            computer = str.split(" has",1)[0]
        if '_' in computer:
            print_yellow('#### -- ' + computer + ' contains an "_"! Removing the "_" & replacing with a space... -- #####')
            unique = computer.replace('_', ' ')
            uniqued = unique.split(" ",1)[0]
            computer = uniqued
            pass
        else:
            pass
        pickle.dump( computer, open( "save.p", "wb"))
        company_info = driver.find_element_by_css_selector(".GE0S-T1CHBL").text
        str = company_info
        ci = str.split("at ",1)[1]
        str = ci
        ci_complete = str.split("\\",1)[0]
        company()
        pickle.dump( ci_complete, open( "company_info.p", "wb"))
        print_blue("[CW-Main][BrinxBot]: Looking for: " + computer + " from " + ci_complete + "....")
        pass  
computerz()
# ---- The above saves to a variable called 'computer' for use in AutomateConnection.py when this file(CW) is imported in.
# make sure internal note section is selected.
time.sleep(2.7)
click_internal = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(2) > div > table > tbody > tr > td:nth-child(2)").click()
#next up is clicking 'New Note'...
new_note = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(1) > div > div > div > div > div > div.CwButton-wrap.TicketNote-newNoteButton > div > div > div > svg").click()
#wait until the interal dialog box loads in...
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'TicketNote-row')))
time.sleep(2)
#now check discussion. after discussion is checked we begin entering our notes.
check_disucssion = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(1) > div:nth-child(1) > div > div > div").click()
enter_notes = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(2) > div > div.ManageNoteRichTextEditor-richEditor > div > div.DraftEditor-editorContainer > div")
if ticket_type == '*Disk Cleanup*':
    enter_notes.send_keys('[BrinxBot]: Python was used to complete this ticket!')
    enter_notes.send_keys(Keys.SHIFT + Keys.RETURN)
    enter_notes.send_keys('[BrinxBot]: Issuing Disk Cleanup script to machine to run tonight at 12:00:00 AM....done!')
    enter_notes.send_keys(Keys.SHIFT + Keys.RETURN)
    enter_notes.send_keys('[BrinxBot]: No further action is needed, the Disk Clean up will run, if another error occurs during the script, a ticket will be created.')
    pass
else:
    print_red("Unknown Ticket type. BrinxBot does not know what to do here.")
#will now check the resolution box 
mark_as_done = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(1) > div:nth-child(3) > div > div > div").click()
#and finally.. hit SAVE!
done = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-buttons > div.CwButton-wrap.TicketNote-newNoteDialogSaveButton").click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#x-auto-312')))
click_yes = driver.find_element_by_css_selector(".GE0S-T1CANG > div:nth-child(1)").click()
time.sleep(2)
#driver.quit() uncomment when running in production (using to complete tickets or you will have to force close this window. )
def Server_ReConnect():# reconnects to the server instead of keeping the first initial connection alive to save some CPU usage.
    try:
        the_url = "https://bruhboxchat.nels277.repl.co/BrinxBot"
        options = webdriver.FirefoxOptions()
        options.headless = True
        driverTwo = webdriver.Firefox(options=options)
        driverTwo.get(the_url)
        time.sleep(1)
        Connection = driverTwo.find_element_by_css_selector("#message")
        Connection.send_keys("/name (CW)BrinxBot" + Keys.RETURN)
        Connection.send_keys("Ticket has been noted and marked as resolved in CW" + Keys.RETURN)
    except NoSuchElementException:
        print_red("Server Connection Failed. Continuing...")
    driverTwo.quit()
Server_ReConnect()
#------------------------------------ENTER AUTOMATE-------------------------#