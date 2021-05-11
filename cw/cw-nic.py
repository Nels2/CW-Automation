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
# USE ONLY FOR nic TICKETS!!!
#
#
#  --------------ConnectWise Automator, By Nelson Orellana -----------------
#
# Introducing a selenium + python script that logs into my ConnectWise, varies what it(where it is the ticket type) looks for depending on user input.
# Then completes via Automate, then logs what work was done into a time entry for the ticket BrinxBot worked..
# ---------------Built 2021.02.22 ------------------------------------------
# ---------------Updated 2021.03.12 ----------------------------------------
print_blue = lambda x: cprint(x, 'cyan')
print_yellow = lambda x: cprint(x, 'yellow')
print_alt_yellow = lambda x: cprint(x, 'yellow', attrs=['underline'])
print_red = lambda x: cprint(x, 'red', attrs=['bold'])
print_green = lambda x: cprint(x, 'green')
print_alt_green = lambda x: cprint(x, 'green', attrs=['bold'])
def startTym():
    start = timer()
    print_yellow(start)
    pickle.dump( start, open( "startTime.p", "wb"))
startTym()
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
#driver = webdriver.Firefox()
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(url)

# change the below fields to match your login info for YOUR connectwise site as well as the URL above it is specific to my login page.
def CWlogin():
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
CWlogin()
# so page can load then clicks on summary description and looks for the specifced ticket.    
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
search = driver.find_element_by_xpath("//input[@id='Summary-input']")
ticket_type = '*NIC Packets*'  # service tickets where a disk clean up is needed
pickle.dump( ticket_type, open( "ticket_info.p", "wb"))
ticket_type = pickle.load( open( "ticket_info.p", "rb"))
time.sleep(0.5)
status_of_tickets = driver.find_element_by_xpath('//*[@id="Description-input"]')
status_of_tickets.send_keys("New (Automate)")
time.sleep(1)
search.send_keys(ticket_type)
ticket_type = '*NIC*'
search.send_keys(Keys.RETURN)
# let the field populate... then searches for tickets that start with "UPDATES" then clicks on the first one
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
try:
    driver.implicitly_wait(3.5)
    ticket = driver.find_element_by_class_name("gwt-Label mm_label GE0S-T1CHBL detailLabel cw_CwLabel").click()
    action = ActionChains(driver)
    action.double_click(ticket)
    pass
except ElementNotInteractableException:
    print_yellow("#### -- Appears to be last ticket of this type("+ticket_type+"). -- ####")
    pass
except NoSuchElementException:
    print_yellow('#### -- Trying again...  -- ####')
    driver.implicitly_wait(1)
    try:
        ticket = driver.find_element_by_css_selector("tr.GE0S-T1CGWF:nth-child(1) > td:nth-child(6) > div:nth-child(1) > a:nth-child(1)").click()
        action = ActionChains(driver)
        action.double_click(ticket)
    except NoSuchElementException:
        print_red('#### -- There were no ticket founds for ticket type: ' + ticket_type + ' -- #####')
        print_yellow('#### -- !! Exiting.. !! -- ####')
        sys.exit()
        pass
    except ElementNotInteractableException:
        print_yellow('#### -- Ticket Function 2 Was Not Used!(NO TICKET FOUND) -- ####')
        pass
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
def MarkResolve():
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
        time.sleep(1.3)
        Mark_Resolved = driver.find_element_by_class_name('GE0S-T1COTH GE0S-T1CJUH cw_status')
        pass
    except NoSuchElementException:
        try:# sometimes you just have to try again.
            time.sleep(0.5)
            Mark_Resolved = driver.find_element_by_class_name('GE0S-T1COTH GE0S-T1CJUH cw_status')
            pass
        except NoSuchElementException:
            Mark_Resolved = driver.find_element_by_xpath('//input[@value="New (Automate)"]') # sometimes the input changes, dont know why.(Referring to Line 141.) best case scenario - use name.
            pass
    Mark_Resolved.click()
    Mark_Resolved.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
    Mark_Resolved.send_keys('Resolved' + Keys.RETURN)
    print_green("[BrinxBot]: Marked as Resolved.")
MarkResolve()
def computerz():
    if ticket_type == '*NIC*':
        alt_t_info = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/span[1]/div").text
        ticket_info = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_initial_desc > div > div:nth-child(1) > div > div > div > div > div:nth-child(2) > div > div > div > div > div.CwPodCol-podCol.CwPodCol-podColWithoutSectionHeader.TicketNote-note.TicketNote-initialNote > div:nth-child(6) > div > label > p").text
        pickle.dump( ticket_info, open( "ticket.p", "wb"))
        pickle.dump( alt_t_info, open( "alt_ticket.p", "wb"))
        print_yellow("#### " + alt_t_info + "####")
        print_yellow("#### " + ticket_info + "####")
        str = ticket_info
        z = str.split("\\",1)[1]
        str = z
        computer = str.split(" at ",1)[0]
        if '_' in computer:
            print_yellow('#### -- ' + computer + ' contains an "_"! Removing the "_" & replacing with a space... -- #####')
            unique = computer.replace('_', ' ')
            uniqued = unique.split(" ",1)[0]
            computer = uniqued
            pass
        else:
            pass
        pickle.dump( computer, open( "save.p", "wb")) 
        company_info = driver.find_element_by_css_selector('#cw-manage-service_service_ticket_initial_desc > div > div:nth-child(1) > div > div > div > div > div:nth-child(2) > div > div > div > div > div.CwPodCol-podCol.CwPodCol-podColWithoutSectionHeader.TicketNote-note.TicketNote-initialNote > div:nth-child(6) > div > label > p').text # this is where the company name is stored
        str = company_info
        ci = str.split("on ",1)[1]
        str = ci
        ci_complete = str.split("\\",1)[0]
        pickle.dump( ci_complete, open( "company_info.p", "wb"))
        print_blue("[CW-Main][BrinxBot]: Looking for...: " + computer + " from " + ci_complete + "....")
        pass
    else:
        pass
computerz()
first_tab_handle = driver.current_window_handle
current_url = driver.current_url
pickle.dump( current_url, open( "url.p", "wb"))
pickle.dump( first_tab_handle, open( "first_tab.p", "wb"))
print_yellow("#### -- first_tab_handle : " + str(first_tab_handle) + "-- ####")
time.sleep(2)
driver.quit()
def AutomateConnection():
    first_tab = pickle.load( open( "first_tab.p", "rb"))
    now = datetime.datetime.now()
    url_second = "https://seamlessdata.hostedrmm.com/automate/login" # make sure this is for YOUR automate, where-ever it is hosted..
    #driver = webdriver.Firefox()
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.execute_script("window.open('about:blank','tab2');")
    driver.switch_to.window("tab2")
    pre = "[" + now.strftime('%Y-%m-%d %I:%M:%S %P') + "]: "
    print_blue(pre + "[BrinxBot]: Switched to second Window. Focus is here currently.")
    driver.get(url_second)
    # change the below fields to match your login info for automate login.
    usrname = ''
    passwd = ''

    print_yellow("#### --------- Begin Automate Connection --------- ####")
    alt_logo = colored('#### -- BrinxBot, an ICX Creation | Version 5.4 -- ####', 'red', attrs=['reverse', 'blink'])
    print(alt_logo)
    print_blue(pre + "[BrinxBot]: starting out.. login in to Automate is first task... commencing...")
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-loginContainer'))) 
    time.sleep(3)
    enter_user = driver.find_element_by_id('loginUsername')
    time.sleep(0.5)
    enter_user.send_keys(usrname) # for some reason usrname + Keys.RETURN does not owkr on this script but works fine with CW.py... will just click 'Next' instead of sending return,
    
    time.sleep(3) # wait because automate loads for no reason when youre done typing
    try:
        click_next = driver.find_element_by_css_selector("#root > div > div > div.login-login > div > div:nth-child(3) > div.CwButton-wrap > div").click() 
        pass
    except ElementClickInterceptedException:
        time.sleep(2)
        click_next = driver.find_element_by_css_selector("#root > div > div > div.login-login > div > div:nth-child(3) > div.CwButton-wrap > div").click()
        pass 
    driver.implicitly_wait(1.5)
    pw = driver.find_element_by_id('loginPassword')
    driver.implicitly_wait(1)
    pw.send_keys(passwd + Keys.RETURN)
    print_green("#### -- Automate Control Center Login Submitted.. Awaiting Token.. -- ####")#-----------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print_blue(pre + "[BrinxBot]: A Token is needed to login! Opening new tab... and switching to it to login into O365!")
    second_tab_handle = driver.current_window_handle
    print_yellow("#### -- second_tab_handle : " + str(second_tab_handle) + "-- ####")
    print_blue(pre + "[BrinxBot]: Logging into Office... ")
    driver.execute_script("window.open('about:blank', 'tab3');")
    driver.switch_to.window("tab3")
    print_blue(pre + "[BrinxBot]: Switched to third tab. Focus is here currently.")
    msft = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1611956433&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de00d1cdc-7140-348d-ccae-406a5464dec6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld"
    driver.get(msft)
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
    time.sleep(2.5)
    print_blue(pre + "[BrinxBot]: Selecting 'No'.. I dont want to stay signed in... continuing")
    try:
        no = driver.find_element_by_css_selector("#idBtn_Back").click()
    except NoSuchElementException:
        time.sleep(1)
        passwd.send_keys(epwd + Keys.RETURN)
        time.sleep(3)
        no = driver.find_element_by_css_selector("#idBtn_Back").click()
    # time to open the email and grab the code...
    print_blue(pre + "[BrinxBot]: Login to O365 was successful! Going to look for the email and save the code(the token)..")
    time.sleep(7)
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'BVgxayg_IGpXi5g7S77GK')))
    search_email = driver.find_element_by_css_selector('._1Qs0_GHrFMawJzYAmLNL2x')
    search_email.send_keys('Seamless data systems, inc. Monitoring' + Keys.RETURN)
    time.sleep(4)
    click_it = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div').click()
                                            
    time.sleep(2)
    try:
        save_it = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/div/div").text
        pass
    except NoSuchElementException:
        save_it = driver.find_element_by_css_selector('.rps_79e8 > div:nth-child(1)')
        pass
    print_blue("[BrinxBot]: Below is the email contents I grabbed:")
    print_yellow("#### -- EMAIL CONTENTS: [" + save_it + "] -- ####")
    da_code = re.sub(r"\D", "", save_it)
    splitFr = (list(str(da_code)))
    da_actual_code = (splitFr[0] + splitFr[1] + splitFr[2] + splitFr[3] + splitFr[4] + splitFr[5])
    print_blue(pre + "[BrinxBot]: I have split the original message to just the code!: " + da_actual_code)
    # now to switch back to tab 1.. [Automate Login Screen]
    print_blue(pre + "[BrinxBot]: ...switching back to Automate Login Screen and inserting code to login")
    time.sleep(3)
    driver.switch_to.window(second_tab_handle) # automate login
    time.sleep(2)
    click_on_token = driver.find_element_by_id('loginToken')
    click_on_token.send_keys(da_actual_code + Keys.RETURN)
    try:
        time.sleep(2)
        click_login = driver.find_element_by_css_selector('.CwButton-innerStandardActive').click()
    except NoSuchElementException:
        driver.implicitly_wait(2)
        try:
            click_login = driver.find_element_by_css_selector('.CwButton-innerStandardActive').click()
        except NoSuchElementException:
            pass
    print_yellow("#### -- Automate Control Center Connecton Established... -- ####")
    # check variable to see if it is the same. 
    computer = pickle.load( open( "save.p", "rb"))
    def company():
        compenny = pickle.load( open( "company_info.p", "rb"))
        if 'Fanestil Meats' in compenny:
            print_yellow("#### -- renaming " + compenny + " to just 'Fanestil' as 'Fanestil Meats' does not exist in Automate")
            replaced = compenny.replace('Fanestil Meats', 'Fanestil')
            compenny = replaced
            pickle.dump( compenny, open( "company_info.p", "wb"))
            pass
        elif 'SR Coffman Construction' in compenny:
            print_yellow("#### -- Renaming " + compenny + " to just 'Coffman Construction' as 'SR Coffman Construction' does not exist in Automate")
            replaced = compenny.replace('SR Coffman Construction Inc.', "Coffman Construction")
            compenny = replaced
            pickle.dump( compenny, open( "company_info.p", "wb"))
            pass
        elif 'Dr. Marlin Flanagin, DDS' in compenny:
            print_yellow("#### -- Renaming " + compenny + " to just 'Dr. Marlin Flanagin' as 'Dr. Marlin Flanagin, DDS' does not exist in Automate")
            replaced = compenny.replace('Dr. Marlin Flanagin, DDS', "Dr Marlin Flanagin")
            compenny = replaced
            pickle.dump( compenny, open( "company_info.p", "wb"))
            pass
        elif 'Lore & Hagemann, Inc' in compenny:
            print_yellow("#### -- Renaming " + compenny + " to just 'Lore' as '&'cannot literally be entered in web version of Automate, this a is a bug on their end.")
            replaced = compenny.replace('Lore & Hagemann, Inc', "Lore")
            compenny = replaced
            pickle.dump( compenny, open( "company_info.p", "wb"))
            pass
        elif 'Lyon Co Title' in compenny:
            print_yellow("#### -- Renaming " + compenny + " to just 'Lyon County Title LLC' as 'Lyon Co Title' does not exist in Automate")
            replaced = compenny.replace('Lyon Co Title', "Lyon County Title LLC")
            compenny = replaced
            pickle.dump( compenny, open( "company_info.p", "wb"))
            pass
        else:
            pass  
    company()
    compenny = pickle.load( open( "company_info.p", "rb"))
    print_yellow("#### -- Pickle has loaded in the following saved variable from CW: " + computer + " -- #####")
    print_yellow("#### -- Pickle has loaded in the following saved variable from CW: " + compenny + " -- #####")
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
    print_yellow("#### -- Searching in Automate for " + computer + " from " + compenny + "... -- ####")   
    driver.implicitly_wait(5)
    try:
        search_for_comp = driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div/span[1]/div/div[2]/input")
        pass
    except NoSuchElementException:
        search_for_comp_alt = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div/span[1]/div/div[2]/input')
        pass
    time.sleep(1)
    try:
        search_peny = driver.find_element_by_css_selector('.CwDataGrid-headerCanvas > span:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(2)')
        search_peny.send_keys(compenny + Keys.RETURN)
        pass
    except NoSuchElementException:
        print_red('#### -- BrinxBot did not find a company for ' + computer) + ' -- ####' 
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
        print_red('#### -- Agent Status: OFFLINE! -- #####')
        print_yellow('#### -- Continuing anyway! -- #####')
    select_computer = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div:nth-child(3) > div.CwDataGrid-rowsContainer > div > div").click()
    # save this tab so i can return to it in case a new window is launched.
    second_tab_handle = driver.current_window_handle
    print_yellow("#### -- second_tab_handle : "+str(second_tab_handle) + " -- ####") # right before computer screen 
    script_start = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div > div > div > div").click()
    time.sleep(0.5)
    script_search = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div:nth-child(2) > div > input")
    print_green(pre + "[BrinxBot]: ..searching for script.")
    # service tickets where Disk Clean up is needed
    script_to_send = 'NicPactSolver'
    script_search.send_keys(script_to_send)
    if ticket_type == '*Disk Cleanup*': #Disk clean up shows up lower in tthe script menu than the others as there are similary named scripts.
        script_run = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div:nth-child(2) > div > div.CwTreeDropdown-treeContainer > div > div > div.CwTreeViewNode-subTree > div:nth-child(2) > div.CwTreeViewNode-subTree > div:nth-child(2) > div > label").click()
        pass
    else:
        script_run = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div > div:nth-child(2) > div > div.CwTreeDropdown-treeContainer > div > div > div.CwTreeViewNode-subTree > div > div > label").click()
        pass
    print_blue(pre + "[BrinxBot]: Inside " + computer + " from " + compenny + " script launch menu now, launching the script...")
    if ticket_type == '*NIC*': # this just runs the script right away for edgeupdate or NIC tickets.
        pass
    driver.implicitly_wait(5)
    search_for_comp = driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div/span[1]/div/div[2]/input")
        # click SCHEDULE
    print_blue(pre + "[BrinxBot]: Wrapping this up & selecting OK...")
    click_ok = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div.CwToolbar-cwToolbar.CwGridToolbar-container > div.CwGridToolbar-leftContainer > div.ComputersGridWithToolbar-scriptsButton > div.Dialogs-dialogContainer > div.CwScrollableDialog-scrollableDialogContainer > div > div > div.CwDialog-buttons > div > div.ScriptSchedulerDialog-cancelNextContainer > div:nth-child(2) > div").click()
    print_alt_green(pre + "[BrinxBot]: I have completed the task assigned... Entering time entry into CW..")
    # establish external connection to let server know job completed right
    driver.quit()
AutomateConnection()
time.sleep(3)
try: # to open aanother page load up CW again..
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.execute_script("window.open('about:blank', 'tab4');")
    driver.switch_to.window("tab4")
    print_blue("[BrinxBot]: re-opening CW window...")
    da_url = pickle.load( open( "url.p", "rb"))
    driver.get(da_url)
    print_alt_green("[BrinxBot]: CW is open again.")
except TypeError:
    print_red('There was a serious error, could spawn CW instance. Ticket was completed but BrinxBot can not open CW to confirm with a time entry.')
# ---- The above saves to a variable called 'computer' for use in AutomateConnection.py when this file(CW) is imported in.
# make sure internal note section is selected.
CWlogin()
time.sleep(3)
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cw-manage-service_service_ticket_discussion > div > div:nth-child(1) > div > div > div > div > div > div.CwButton-wrap.TicketNote-newNoteButton > div > div')))
MarkResolve()
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
if ticket_type == '*NIC*':
    enter_notes.send_keys('[BrinxBot]: Python was used to complete this ticket!')
    enter_notes.send_keys(Keys.SHIFT + Keys.RETURN)
    enter_notes.send_keys('[BrinxBot]: Issuing NICPactSolver script to machine....done!')
    enter_notes.send_keys(Keys.SHIFT + Keys.RETURN)
    enter_notes.send_keys('[BrinxBot]: No further action is needed, the NICPactSolver script has investigated and resolved NIC packet issues.')
    print_alt_green('[BrinxBot]: Time Entry Has Been Entered.')
    pass
else:
    print_red("Unknown Ticket type. BrinxBot does not know what to do here.")
#will now check the resolution box 
mark_as_done = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-content > div > div.TicketNote-newNoteDialogTopPadding > div > div:nth-child(1) > div:nth-child(3) > div > div > div").click()
#and finally.. hit SAVE!
done = driver.find_element_by_css_selector("#cw-manage-service_service_ticket_discussion > div > div:nth-child(2) > div > div > div.CwDialog-buttons > div.CwButton-wrap.TicketNote-newNoteDialogSaveButton").click()
driver.implicitly_wait(3)
click_yes = driver.find_element_by_css_selector(".GE0S-T1CANG > div:nth-child(1) > div:nth-child(1)").click()
time.sleep(2)
driver.quit() # uncomment when running in production (using to complete tickets or you will have to force close this window. )
end = timer()
ticket_type = pickle.load( open( "ticket_info.p", "rb"))
ticket_info = pickle.load( open( "ticket.p", "rb"))
alt_t_info = pickle.load( open( "alt_ticket.p", "rb"))
start = pickle.load( open( "startTime.p", "rb"))
compenny = pickle.load( open( "company_info.p", "rb"))
computer = pickle.load( open( "save.p", "rb"))
now = datetime.datetime.now()
print_alt_yellow("Script Completetion Time:")
print_alt_green(end - start)
pre = "[" + now.strftime('%Y-%m-%d %I:%M:%S %P') + "]: "
print_alt_yellow("#### -- " + alt_t_info + " -- ####")
print_alt_yellow("#### -- " + ticket_info + " -- ####")
print_green("#### -- BrinxBot completed ticket for " + computer + " from " + compenny + " -- ####")
print_alt_green(pre + "[BrinxBot]: I have completed the task assigned... letting server know...")
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
        ticket_info = pickle.load( open( "ticket.p", "rb"))
        alt_t_info = pickle.load( open( "alt_ticket.p", "rb"))
        Connection.send_keys('Here is the ticket I completed today: [' + alt_t_info + ']' + Keys.RETURN)
        Connection.send_keys('Here is the ticket I completed today: [' + ticket_info + ']' + Keys.RETURN)
        Connection.send_keys('Script Completetion Time:')
        Connection.send_keys(str(end- start))
        Connection.send_keys(Keys.RETURN)
        Connection.send_keys("Computer ticket has been completed successfully in ConnectWise Automate Control Center for: " + computer + "/" + compenny + "!" + Keys.RETURN)
        pass        
    except WebDriverException:
        print_red("#### -- FAIL -- ####")
        print_red("Server Connection Failed. No login was made to the Server. Continuing...")
    driverTwo.quit()
Server_ReReConnect()
Connectionloss = colored('Connection to BrinxBot has been lost.', 'red', attrs=['reverse', 'blink'])
print_red(pre + Connectionloss)# oh no! 
NT_total = pickle.load( open( "tickets/NT.p", "rb"))
NT = int(NT_total)
count = 0 
count += 1
try:
    ct = pickle.load( open( "count/nt_count.p", "rb"))
    cti = int(ct)
    count = cti
    print_yellow('count when script started:')
    print_alt_green(count)
except FileNotFoundError:
    pass
except IndexError:
    pass
while (count <= NT): 
    print_alt_yellow("#### -- Restarting BrinxBot... -- ####")
    if (count == NT):
        print_red('#### -- No tickets left for ' + ticket_type + ' type... -- #####')
        print_yellow('#### -- Starting next script... -- #####')
        sys.exit()
        pass
    else:
        pass
    count += 1
    print_yellow('count after completion:')
    print_alt_green(count)
    pickle.dump( str(count), open( "count/nt_count.p", "wb"))
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    pass
print_red('#### -- No tickets left for ' + ticket_type + ' type... -- #####')
print_yellow('#### -- Starting next script... -- #####')