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
from pathlib import Path
import termcolor
from termcolor import colored, cprint
import time
from time import sleep
import re
import sys
import os
import datetime
import pickle


#
# Made to check total online agents vs offline -- is handy.W. 
#
Path('misc/agntstat.txt').touch()
print_blue = lambda x: cprint(x, 'cyan')
print_yellow = lambda x: cprint(x, 'yellow')
print_red = lambda x: cprint(x, 'red', attrs=['bold'])
print_green = lambda x: cprint(x, 'green')
print_alt_green = lambda x: cprint(x, 'green', attrs=['bold'])
def AutomateConnect():
    now = datetime.datetime.now()
    url_second = "https://seamlessdata.hostedrmm.com/automate/login" # make sure this is for YOUR automate, where-ever it is hosted..
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.execute_script("window.open('about:blank','tab2');")
    driver.switch_to.window("tab2")
    pre = "[" + now.strftime('%Y-%m-%d %I:%M:%S %P') + "]: "
    print_blue(pre + "[BrinxBot]: Automate Login Screen is Active.")
    driver.get(url_second)
    # change the below fields to match your login info for automate login.
    usrname = ''
    passwd = ''

    print_yellow("#### --------- Begin Automate Connection --------- ####")
    alt_logo = colored('#### -- BrinxBot, an ICX Creation | Version 5.4 -- ####', 'red', attrs=['reverse', 'blink'])
    print(alt_logo)
    print_blue(pre + "[BrinxBot]: filling out login information..")
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
    time.sleep(1.5)
    pw = driver.find_element_by_id('loginPassword')
    time.sleep(0.5) 
    pw.send_keys(passwd + Keys.RETURN)
    print_green("#### -- Automate Control Center Login Submitted.. Awaiting Token.. -- ####")#-----------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print_blue(pre + "[BrinxBot]: A Token is needed to login! Opening new tab... and switching to it to login into O365!")
    second_tab_handle = driver.current_window_handle
    print_yellow("#### -- second_tab_handle : " + str(second_tab_handle) + "-- ####")
    print_blue(pre + "[BrinxBot]: Logging into Office... ")
    driver.execute_script("window.open('about:blank', 'tab3');")
    driver.switch_to.window("tab3")
    print_blue(pre + "[BrinxBot]: Office 365 window is active.")
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
    time.sleep(3)
    click_on_token = driver.find_element_by_id('loginToken')
    click_on_token.send_keys(da_actual_code + Keys.RETURN)
    try:
        time.sleep(3)
        click_login = driver.find_element_by_css_selector('.CwButton-innerStandardActive').click()
    except NoSuchElementException:
        driver.implicitly_wait(2)
        try:
            click_login = driver.find_element_by_css_selector('.CwButton-innerStandardActive').click()
        except NoSuchElementException:
            pass
    print_yellow("#### -- Automate Control Center Connecton Established... -- ####")
    # check variable to see if it is the same. 
    driver.implicitly_wait(5)
    PC_c = 150
    count = 1
    while count < PC_c:
        AgentName = "/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/span[1]/div"
        if "/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/span[1]/div" in AgentName:
            sreplacement = "/div[" + str(count) + "]/span[1]"
            suni = AgentName.replace('/div[1]/span[1]', sreplacement)
            AgentName = suni
            pass
        AgentStatus = '/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/span[2]/div/span[1]/div/div'
        if '' in AgentStatus:
            replacement = '/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[' + str(count) + ']/span[2]/div/span[1]/div/div'
            uni = AgentStatus.replace('/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/span[2]/div/span[1]/div/div', replacement)
            AgentStatus = uni
            pass
        AgentN = driver.find_element_by_xpath(AgentName).text
        agent = driver.find_elements_by_xpath(AgentStatus)
        for ii in agent:
            #print ii.tag_name
            try:
                pickle.load( open( "count.p", "rb"))
            except FileNotFoundError:
                pass
            tx = ii.get_attribute('class')
            if 'isvg loaded CwDataGrid-cellImage CwDataGrid-success' in tx:
                agentstat = 'Online'
                with open('misc/agntstat.txt', 'a') as f:
                    print("Agent Status: ", agentstat, file=f)
                print_alt_green("->> Found " + AgentN + ". | status: " + agentstat + ".")
                pass
            elif 'isvg loaded CwDataGrid-cellImage CwDataGrid-failed' in tx:
                agentstat = 'Offline'
                with open('misc/agntstat.txt', 'a') as f:
                    print("Agent Status: ", agentstat, file=f)
                print_red("->> Found " + AgentN + ". | status: " + agentstat + ".")
                pass
        count += 1
        pass
    total_online = 0
    total_offline = 0
    with open('misc/agntstat.txt') as f:
        for line in f:
            found_online = line.find('Online')
            if found_online != -1 and found_online != 0:
                total_online += 1
            found_offline = line.find('Offline')
            if found_offline != -1 and found_offline != 0:
                total_offline += 1
    print_blue("|>>    Online :  "+str(total_online)+"      ")
    print_blue("|>>    Offline:  "+str(total_offline)+"      ")
    os.remove('misc/agntstat.txt')
    # establish external connection to let server know job completed right
    driver.quit()
AutomateConnect()