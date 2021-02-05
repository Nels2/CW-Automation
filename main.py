from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time
import pickle
# import AutomateConnection.py -- un'#' once Automate Connection has been finished.


#
#
#  --------------ConnectWise Automator, By Nelson Orellana -----------------
#
# Introducing a selenium + python script that logs into my ConnectWise, looks for tickets starting with 'UPDATE'(the ticket it looks for can be change. I plan to add more complexion to this script as time goes on.)
#
# ---------------Built 2021.01.27 ------------------------------------------
#
#
#
url = "https://na.myconnectwise.net/v2020_3/connectwise.aspx?fullscreen=false&locale=en_US#startscreen=sr200"
driver = webdriver.Firefox()
driver.get(url)

# change the below fields to match your login info.
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

# this is the xpath for the ubtton i need to clik on. /html/body/div[3]/table/tbody/tr[2]/td/input[1]
# this is ccs selector path for button i need. below
##  include the first # -> #session-dialog > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)

# clicking proceed so i can continue
time.sleep(3)
driver.find_element_by_xpath("//input[@value='Proceed']").click()

# so page can load then clicks on summary description and looks for the specifced ticket.
# time.sleep(20)
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
search = driver.find_element_by_xpath("//input[@id='Summary-input']")
search.send_keys('UPDATES')
search.send_keys(Keys.RETURN)

# let the field populate... then searches for tickets that start with "UPDATES" then clicks on the first one
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
#WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#srboard-listview-scroller > div.GE0S-T1CAVF > table > tbody:nth-child(2) > tr.GE0S-T1CGWF.cw-ml-row.GE0S-T1CEWF > td:nth-child(6) > div > a")))
time.sleep(3)
ticket = driver.find_element_by_css_selector("tr.GE0S-T1CGWF:nth-child(1) > td:nth-child(6) > div:nth-child(1) > a:nth-child(1)").click()
action = ActionChains(driver)
action.double_click(ticket)

#Next is viewing what the ticket is about to make sure it is correct before continuing...
# Internal Note tabe should now be selected.. 
#---------------Will add error if ticket note is not found later!!!!!!!!! currently stuck here.!!!!!!!!!!!!!!!!!!!!!!!!!!!
#--------------------------    Now to click on new note and begin the process of TRUE automation without CW's useless scripting...
time.sleep(3)
# now to scroll the view down.. hopefully!
grab = driver.find_element_by_tag_name('html')
grab.send_keys(Keys.PAGE_DOWN * 5)

# also need to save what ticket is about so BrinxBot isn't lost..
time.sleep(3)
#       ticket_info = driver.find_element_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]/table/tbody/tr[3]/td/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[3]/div[4]/div/label/p").text
#       print(ticket_info)
# break text up so I only have computer name so brinxbot can look it up.
def computerz():
    ticket_info = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_initial_desc > div > div:nth-child(1) > div > div > div > div > div:nth-child(2) > div > div > div > div > div.CwPodCol-podCol.CwPodCol-podColWithoutSectionHeader.TicketNote-note.TicketNote-initialNote > div:nth-child(5) > div > label > p").text
    print("#### " + ticket_info + "####")
    computer = ticket_info.split("\\",1)[1]
    pickle.dump( computer, open( "save.p", "wb"))
    print(computer)
    print("[CW-Main][BrinxBot]: Looking for...: " + computer)
computerz()
# ---- The above should be saved to a variable called 'computer' for use in AutomateConnection.py when this file(main[.py]) is imported in.
# make sure internal note section is selected.
click_internal = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(1) > div > div > div > div > div > div:nth-child(2) > div > table > tbody > tr > td:nth-child(2)").click()
#next up is clicking 'New Note'...

new_note = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(1) > div > div > div > div > div > div.CwButton-wrap.TicketNote-newNoteButton > div > div > div > svg").click()
#wait until the interal dialog box loads in...
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'TicketNote-row')))
time.sleep(2)
#now check discussion. after discussion is checked we begin entering our notes.
check_disucssion = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(1) > div:nth-child(1) > div > div > div").click()


## --------------------------------------- not needed unless dong a timed entry. --------------------------------------##
#  new note should now be open. For best results, its best to wait until the whole frame itself is loaded in. We'll be looking for the 'notes' area to load in..
#    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, 'notranslate public-DraftEditor-content')))
#    set_time = driver.find_element_by_css_selector("#x-auto-42 > div.GGMMTRSLWE > div.GGMMTRSKWE > table > tbody > tr > td > div > div > div.GGMMTRSNH.mm_tabBody > div > div:nth-child(1) > div.GGMMTRSDXE.pod_unknown.pod_time_entry_details > div.GGMMTRSLWE > div.GGMMTRSKWE > table > tbody > tr:nth-child(1) > td > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > div").click();

#   now that time has been set, we can begin entering our time entry.

## --------------------------------------------------------------------------------------------------------------------##


enter_notes = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(2) > div > div.ManageNoteRichTextEditor-richEditor > div > div.DraftEditor-editorContainer > div")
enter_notes.send_keys('[BrinxBot]: This ticket is being completed using Python & Selenium!')
enter_notes.send_keys('[BrinxBot]: Issuing Reboot Script and scheduling it for 12:00:00 AM tonight...done!') 
enter_notes.send_keys('[BrinxBot]: The issue appears to be resolved, a reboot will occur tonight.')
#will now check the resolution box -- I will add a method that goes into Automate and sends the reboot script. Still testing..
mark_as_done = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(1) > div:nth-child(3) > div > div > div").click()
#and finally.. hit SAVE!
done = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-buttons > div.CwButton-wrap.TicketNote-newNoteDialogSaveButton").click()

#------------------------------------ENTER AUTOMATE-------------------------

