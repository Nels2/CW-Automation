from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from time import sleep
import re
import pickle
import datetime
import sys
import os
import pyfiglet
from pyfiglet import Figlet
import termcolor
from termcolor import colored, cprint
import CW
from CW import computerz, Ticket_info_method
# -- -- -- -- -- -- -- -- -- #
#    Created by Nelson O.    #
#        2021.01.29          #
#    AutomateConnection      #
# -- -- -- -- -- -- -- -- -- #
# --
# This script is intended to login into Automate and grab the verification code from an email to login.
# Should ALWAYS be used before 'CW.py'
# So far this script can complete script types 'updates', 'Disk Cleanup'  and 'service edgeupdate has stopped'
# --
print_blue = lambda x: cprint(x, 'cyan')
print_yellow = lambda x: cprint(x, 'yellow')
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
ticket_type = pickle.load( open( "ticket_info.p", "rb"))
ticket_info = pickle.load( open( "ticket.p", "rb"))
now = datetime.datetime.now()

url = "https://seamlessdata.hostedrmm.com/automate/login" # make sure this is for YOUR automate, where-ever it is hosted..
driver = webdriver.Firefox()
driver.get(url)
pre = "[" + now.strftime('%Y-%m-%d %I:%M:%S %P') + "]: "
# time to make this easy to use for anyone althought this time is only for when the script was origanlly ran at.. so not the most accurate.. will change when I learn a new way to print the time as a function is ran instead of when the script is first ran...
print("------------------------------------------------------------------")
# change the below fields to match your login info for automate login.
usrname = ''
passwd = ''

print_yellow("#### --------- Begin Automate Connection --------- ####")
try:
    custom_fig = Figlet(font='hollywood')
    print_red(custom_fig.renderText('Brinx'))
except NotImplementedError: 
    pass
alt_logo = colored('#### -- BrinxBot, an ICX Creation | Version 1.2.0 -- ####', 'red', attrs=['reverse', 'blink'])
print(alt_logo)
print_blue(pre + "[BrinxBot]: starting out.. login in to Automate is first task... commencing...")
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
time.sleep(3)
enter_user = driver.find_element_by_id('loginUsername')
time.sleep(0.5)
enter_user.send_keys(usrname) # for some reason usrname + Keys.RETURN does not owkr on this script but works fine with CW.py... will just click 'Next' instead of sending return,
time.sleep(1.5) # wait because automate loads for no reason when youre done typing
click_next = driver.find_element_by_css_selector("#root > div > div > div.login-login > div > div:nth-child(3) > div.CwButton-wrap > div").click() 
time.sleep(1.5)
pw = driver.find_element_by_id('loginPassword')
time.sleep(0.5) 
pw.send_keys(passwd + Keys.RETURN)
print_green("#### -- Automate Control Center Login Sumbitted.. Awaiting Token.. -- ####")#-----------------------------------------------------------------------------------------------------
time.sleep(1.5)
print_blue(pre + "[BrinxBot]: A Token is needed to login! Opening new tab... and switching to it to login into O365!")
# the 74-765 lines after this comment are meant to collect the current window handle info. --#
# Opening Tab 2 up [Office 365 Email Inbox]
first_tab_handle = driver.current_window_handle
print_yellow("#### -- first_tab_handle : " + str(first_tab_handle) + "-- ####")
print_blue(pre + "[BrinxBot]: Logging into Office... ")
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
print_blue(pre + "[BrinxBot]: Switched to second tab. Focus is here currently.")
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1611956433&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de00d1cdc-7140-348d-ccae-406a5464dec6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld')
time.sleep(2)
# enter your email and password for your O365 login.
email = ''
epwd = ''

userN = driver.find_element_by_name('loginfmt')
userN.send_keys(email + Keys.RETURN)
time.sleep(2.5)
passwd = driver.find_element_by_name('passwd')
passwd.send_keys(epwd + Keys.RETURN)
passwd.send_keys(Keys.RETURN)
print_green("#### -- Office Account Has Been Signed in. -- ####")
# select 'No' to stay signed in.
time.sleep(1.5)
print_blue(pre + "[BrinxBot]: Selecting 'No'.. I dont want to stay signed in... continuing")
no = driver.find_element_by_css_selector("#idBtn_Back").click()
# time to open the email and grab the code...
print_blue(pre + "[BrinxBot]: Login to O365 was successful! Going to look for the email and save the code(the token)..")
time.sleep(7)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'BVgxayg_IGpXi5g7S77GK')))
search_email = driver.find_element_by_css_selector('._1Qs0_GHrFMawJzYAmLNL2x')
search_email.send_keys('Seamless data systems, inc. Monitoring' + Keys.RETURN)
time.sleep(4)
click_it = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]').click()
time.sleep(2)
try:
    save_it = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[3]").text
    pass
except NoSuchElementException:
    save_it = driver.find_element_by_css_selector('.rps_79e8 > div:nth-child(1)')
    pass
print_blue("[BrinxBot]: Below is the email contents I grabbed:")
print_yellow("#### -- EMAIL CONtENTS: [" + save_it + "] -- ####")
da_code = re.sub(r"\D", "", save_it)
print_blue(pre + "[BrinxBot]: I have split the original message to just the code!: " + da_code)
# now to switch back to tab 1.. [Automate Login Screen]
print_blue(pre + "[BrinxBot]: ...switching back to Automate Login Screen and inserting code to login")
time.sleep(3)
driver.switch_to.window(first_tab_handle) # automate login
time.sleep(2)
click_on_token = driver.find_element_by_id('loginToken')
click_on_token.send_keys(da_code + Keys.RETURN)
print_yellow("#### -- Automate Control Center Connecton Established... -- ####")
# check variable to see if it is the same. 
computer = pickle.load( open( "save.p", "rb"))
compenny_info = pickle.load( open( "company_info.p", "rb"))
print_yellow("#### -- Pickle has loaded in the following saved variable from main: " + computer + " -- #####")
try:#sometimes an error comes up when logging into automate.
    find_internal_error = driver.find_element_by_css_selector(".CwDialog-modal")
    click_ok_for_unhandled_exp = driver.find_element_by_css_selector(".CwDialog-buttons > div:nth-child(1) > div:nth-child(1)") 
    click_ok_for_unhandled_exp.click()
    print_yellow("#### -- There was an unhandled error but it is OK, Login is successful! -- ####")
except NoSuchElementException: 
    pass
    print_green("#### -- DashBoard Loaded Successfully with No Errors! -- ####")
print_green(pre + "[AC][BrinxBot]: I'm in! Looking for computer: " + computer + "!")
# now time to search for computer and double click on it
print_yellow("#### -- Searching in Automate for computer... -- ####")  
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div/span[1]/div/div[2]/input')))
search_for_comp = driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div/span[1]/div/div[2]/input")
time.sleep(1)
try:
    search_peny = driver.find_element_by_css_selector('.CwDataGrid-headerCanvas > span:nth-child(4) > div:nth-child(1) > div:nth-child(2) > input:nth-child(2)')
    search_peny.send_keys(compenny_info + Keys.RETURN)
    pass
except NoSuchElementException:
    print_yellow('#### -- BrinxBot did not find a company for ' + computer) 
    pass
print_blue(pre + "[BrinxBot]: Computer has been found clicking on it to continue the task...")
search_for_comp.send_keys(computer + Keys.RETURN)
time.sleep(3)
Agnt_Status = driver.find_elements_by_css_selector('.CwDataGrid-success')
s = len(Agnt_Status)
# check condition, if list size > 0, element exists
if(s>0):
    print_green('#### -- Agent Status: ONLINE! -- #####')
    pass
else:
    while True:
        print_red('#### -- Agent Status: OFFLINE! -- #####')
        decide = input("| Do you want to continue anyway? (y/n): ")
        if decide == 'y':
            pass
            break
        elif decide == 'n':
            print_yellow('#### -- !! Force Quitting !! -- ####')
            sys.exit()
            pass
        else:
            print_red(' #### -- ERROR: You need to enter either y/n. -- ####')
            continue
select_computer = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div:nth-child(3) > div.CwDataGrid-rowsContainer > div > div").click()
# save this tab so i can return to it in case a new window is launched.
second_tab_handle = driver.current_window_handle
print_yellow("#### -- second_tab_handle : "+str(second_tab_handle) + " -- ####") # right before computer screen 
script_start = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div > div > div > div").click()
time.sleep(0.5)
script_search = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div:nth-child(2) > div > input")
print_green(pre + "[BrinxBot]: ..searching for script.")
if ticket_type == '*Reboot*': # UPDATES pending tickets
            script_to_send = 'reboot script'
            pass
elif ticket_type == '*edgeupdate*': # service tickets where edgeupdate is stopped
            script_to_send = 'S_R_V'
            pass
elif ticket_type == '*Disk Cleanup*': # service tickets where Disk Clean up is needed
            script_to_send = 'Disk Cleanup'
            pass
elif ticket_type == '*NIC*': # service tickets where NIC packets are erroring and NicPactSolver script is needed
            script_to_send = 'NicPactSolver'
            pass
script_search.send_keys(script_to_send)
if ticket_type == '*Disk Cleanup*': #Disk clean up shows up lower in tthe script menu than the others as there are similary named scripts.
    script_run = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div:nth-child(2) > div > div.CwTreeDropdown-treeContainer > div > div > div.CwTreeViewNode-subTree > div:nth-child(2) > div.CwTreeViewNode-subTree > div:nth-child(2) > div > label").click()
    pass
else:
    script_run = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div:nth-child(2) > div > div.CwTreeDropdown-treeContainer > div > div > div.CwTreeViewNode-subTree > div > div > label").click()
    pass
print_blue(pre + "[BrinxBot]: Inside " + computer + " from " + compenny_info + " script launch menu now, launching the script...")
if ticket_type == '*edgeupdate*' or ticket_type == '*NIC*': # this just runs the script right away for edgeupdate or NIC tickets.
    pass
elif ticket_type == '*Reboot*' or ticket_type == '*Disk Cleanup*': # UPDATES(reboot) & Disk Clean up tickets
    # -- wait for dialog box to appear.. -- #
    print_blue(pre + "[BrinxBot]: waiting for dialog box..")
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div')))
    # -- check the do later box -- #
    print_blue(pre + "[BrinxBot]: checking the 'do later' option so the script runs at a different time.")
    do_later = driver.find_element_by_css_selector("#browse_computers_grid_toolbar_button_scripts_now_later_dialogscrollable_body_id > div.ScriptSchedulerDialog-radioButtonContainer > div.CwRadioButtonGroup-container > div:nth-child(2) > div > div > div > svg > circle.CwRadioButton-largeInnerCircle").click()
    # change the date for script to be ran at, usually at the moment or the next day at 12:00:00 AM
    print_blue(pre + "[BrinxBot]: Changing the date to tomorrow.")
    date = driver.find_element_by_css_selector("#browse_computers_grid_toolbar_button_scripts_now_later_dialogscrollable_body_id > div.ScriptSchedulerDialog-timeDateFields > div:nth-child(1) > div.CwDatePicker-datePickerRoot > div > input")
    date.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
    # a bit of time calculation going on here... 
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    NextDay_Date_Formatted = NextDay_Date.strftime ('%m' + '/' + '%d' + '/' + '%Y') # format the date to ddmmyyyy
    print_yellow('#### -- tomorrows date is ' + str(NextDay_Date_Formatted) + ' -- ####')
    time.sleep(1)
    date.send_keys(str(NextDay_Date_Formatted) + Keys.RETURN)
    date.send_keys(Keys.TAB) 
    print_green(pre + "[BrinxBot]: Date has been changed.")
    # change time script is ran to 12:00:00 AM
    print_blue(pre + "[BrinxBot]: Changing the time to 12am")
    tomrrw = driver.find_element_by_css_selector("#browse_computers_grid_toolbar_button_scripts_now_later_dialogscrollable_body_id > div.ScriptSchedulerDialog-timeDateFields > div:nth-child(2) > input")
    tomrrw.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
    tomrrw.send_keys("12a" + Keys.TAB)
    time.sleep(1)
    print_green(pre + "[BrinxBot]: Time has been changed")
    pass
# click SCHEDULE
print_blue(pre + "[BrinxBot]: Wrapping this up & selecting OK...")
click_ok = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div.Dialogs-dialogContainer > div.CwScrollableDialog-scrollableDialogContainer > div > div > div.CwDialog-buttons > div > div.ScriptSchedulerDialog-cancelNextContainer > div:nth-child(2) > div").click()
print_green(pre + "[BrinxBot]: I have completed the task assigned... shutting off after letting server know...")
# establish external connection to let server know job completed right
def Server_ReReConnect():# like in CW.py it is better to close the connection after the initial connection to save CPU/MEM usage.
    try:
        the_url = "https://bruhboxchat.nels277.repl.co/BrinxBot"
        options = webdriver.FirefoxOptions()
        options.headless = True
        driverTwo = webdriver.Firefox(options=options)
        driverTwo.get(the_url)

        time.sleep(1)
        Connection = driverTwo.find_element_by_css_selector("#message")
        Connection.send_keys("/name (CWA)BrinxBot" + Keys.RETURN)
        Connection.send_keys('Here is the ticket I completed today: [' + ticket_info + ']' + Keys.RETURN)
        Connection.send_keys("Computer ticket has been completed successfully in ConnectWise Automate Control Center for: " + computer + "!" + Keys.RETURN)
    except RuntimeError:
        print_red(pre + "Server Connection Failed. Continuing with shutdown.")
    driverTwo.quit()
Server_ReReConnect()
driver.quit()
execTym = (time.time() - now)
print_yellow("#### -- BrinxBot completed ticket for " + computer + " of " + compenny_info + "in: " + execTym + " seconds -- ####")
Connectionloss = colored('Connection to BrinxBot has been lost.', 'red', attrs=['reverse', 'blink'])
print_red(pre + Connectionloss)# oh no! 
while True:#my try at issuing a restart..
    prompt = input("Do you want to reconnect? (y/n): ")
    if prompt == 'y':
        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        pass
        break
    elif prompt == 'n':
        sys.exit()
        pass
    else:
        continue