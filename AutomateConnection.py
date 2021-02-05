from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import re
import pickle
import datetime
import main
from main import computerz


# -- -- -- -- -- -- -- -- -- #
#    Created by Nelson O.    #
#        2021.01.29          #
#    AutomateConnection      #
# -- -- -- -- -- -- -- -- -- #

# --
# This script is intended to login into Automate and grab the verification code from an email to login.
# Should be used before 'main.py'
# --

url = "https:/1/seamlessdata.hostedrmm.com/automate/login"
driver = webdriver.Firefox()
driver.get(url)
# time to make this easy to use as user for their info so it can login into their site...
print("------------------------------------------------------------------")
# change the below fields to match your login info.
usrname = ''
passwd = ''

print("...")
print("...")
print("...")
print("#### --------- Begin Automate Connection --------- ####")
print("#####     #####     #####   ##       #  #       # ")
print("#    #    #    #      #     # #      #   #     #  ")
print("#     #   #     #     #     #  #     #    #   #   ")
print("#    #    #    #      #     #   #    #     # #    ")
print("#####     # ###       #     #    #   #      #     ")
print("#    #    #    #      #     #     #  #     # #    ")
print("#     #   #     #     #     #      # #    #   #   ")
print("#    #    #      #    #     #       ##   #     #  ")
print("#####     #      #  #####   #        #  #       # ")
print("...")
print("...")
print("[BrinxBot]: starting out.. login in to Automate is first task... commencing...")
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
time.sleep(3)
enter_user = driver.find_element_by_id('loginUsername')
enter_user.send_keys(usrname + Keys.RETURN)
time.sleep(2)
pw = driver.find_element_by_id('loginPassword')
pw.send_keys(passwd + Keys.RETURN)
time.sleep(1.5)
print("[BrinxBot]: We just need the token now to login! Opening new tab... and switching to it!")
# now to login into my email and get code and go back to verify. Must be done withing 3-8 minutes or code is no longer valid.
# --- second tab --- #
# the 2 lines after this comment are meant to collect the current window handle info. --#
# Opening Tab 2 up [Office 365 Email Inbox]
first_tab_handle = driver.current_window_handle
print("first_tab_handle : "+str(first_tab_handle))
print("[BrinxBot]: Logging into Office... ")
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
print("[BrinxBot]: Switched to second tab. Focus is here currently.")
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1611956433&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de00d1cdc-7140-348d-ccae-406a5464dec6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld')
time.sleep(2)

email = ''
epwd = ''

userN = driver.find_element_by_name('loginfmt')
userN.send_keys(email + Keys.RETURN)
time.sleep(3)
passwd = driver.find_element_by_name('passwd')
passwd.send_keys(epwd + Keys.RETURN)
passwd.send_keys(Keys.RETURN)

# select 'No' to stay signed in.
time.sleep(1.5)
no = driver.find_element_by_css_selector("#idBtn_Back").click()
print("[BrinxBot]: No. I dont want to stay signed in... continuing")
# time to open the email and grab the code...
print("[BrinxBot]: I'm in! Going to look for the email and save the code..")
time.sleep(7)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'BVgxayg_IGpXi5g7S77GK')))
search_email = driver.find_element_by_css_selector('._1Qs0_GHrFMawJzYAmLNL2x')
search_email.send_keys('Seamless data systems, inc. Monitoring' + Keys.RETURN)
time.sleep(4)
click_it = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]').click()
time.sleep(2)
save_it = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[3]").text
print(save_it)
da_code = re.sub(r"\D", "", save_it)
print("[BrinxBot]: I have split the original message to just the code!: " + da_code)
# now to switch back to tab 1.. [Automate Login Screen]
print("[BrinxBot]: ...switching back to Automate Login Screen and inserting code to login")
time.sleep(3)
driver.switch_to.window(first_tab_handle) # automate login
time.sleep(2)
click_on_token = driver.find_element_by_id('loginToken')
click_on_token.send_keys(da_code + Keys.RETURN)
print("#### Login was successful ####")
# check variable to see if it is the same. 
computer = pickle.load( open( "save.p", "rb"))
print("#### Pickle has loaded in the following saved variable from main: " + computer)
print("[AC][BrinxBot]: I'm in! Looking for computer: " + computer + "!")
# now time to search for computer and double click on it
print("#### .....searching in automate.... ####")
time.sleep(6)
search_for_comp = driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div[2]/div[2]/div[3]/div[2]/div/span[1]/div/div[2]/input")
print("[BrinxBot]: Computer has been found clicking on it to continue the task...")
search_for_comp.send_keys(computer + Keys.RETURN)
element = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div:nth-child(3) > div.CwDataGrid-rowsContainer > div > div > span:nth-child(1) > div")
# save this tab so i can return to it
second_tab_handle = driver.current_window_handle
print("second_tab_handle : "+str(second_tab_handle)) # right before computer screen 
# the 3 lines below are to double click on the computer and open it.
action = ActionChains(driver)
action.double_click(on_element=element)
action.perform() # this will open a new screen to the computer itself to begin managing it.

# ---------- Computer screen -----------#
# !!!! ----- I need to implement a check to see if agent is active. ----- !!!!! #
print("[BrinxBot]: Inside " + computer + " now, launching script...")
start_script_menu = driver.find_element_by_css_selector("#root > div > div > div.computerScreen-background > div.Header-header > div.core-container > div.Header-commandsToolbar > div.Header-scriptHeaderButton > div > div > div > div").click()
time.sleep(2)
# now to run the script, in this case the reboot script.. 
# -- locate script -- #
print("[BrinxBot]: ...locating the script using the search bar..")
start_script = driver.find_element_by_css_selector("#root > div > div > div.computerScreen-background > div.Header-header > div.core-container > div.Header-commandsToolbar > div.Header-scriptHeaderButton > div > div:nth-child(2) > div > input")
start_script.send_keys("reboot script" + Keys.RETURN)
# -- run the script --#
click_script = driver.find_element_by_css_selector("#root > div > div > div.computerScreen-background > div.Header-header > div.core-container > div.Header-commandsToolbar > div.Header-scriptHeaderButton > div > div:nth-child(2) > div > div.CwTreeDropdown-treeContainer > div > div > div.CwTreeViewNode-subTree > div > div > label").click()
print("[BrinxBot]: ..script has been found.")
# -- wait for dialog box to appear.. -- #
print("[BrinxBot]: waiting for dialog box..")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div')))
# -- check the do later box -- #
print("[BrinxBot]: checking the 'do late' option so the script runs at a different time.")
do_later = driver.find_element_by_css_selector("div.CwRadioButtonGroup-column:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(2) > circle:nth-child(3)").click()
# change the date for script to be ran at, usually at the moment or the next day at 12:00:00 AM
print("[BrinxBot]: Changing the date to tomorrow.")
date = driver.find_element_by_css_selector("input.CwTextField-textField:nth-child(1)")
date.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)

# a bit of time calculation going on here... 
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
NextDay_Date_Formatted = NextDay_Date.strftime ('%m' + '-' + '%d' + '-' + '%Y') # format the date to ddmmyyyy
print ('#### tomorrows date is ' + str(NextDay_Date_Formatted))
time.sleep(1)
date.send_keys(str(NextDay_Date_Formatted))
print("[BrinxBot]: Date has been changed.")
# --------------------------------------
# change time script is ran to 12:00:00 AM
print("[BrinxBot]: Changing the time to 12a")
times = driver.find_elements_by_css_selector("input.CwTextField-textField:nth-child(2)")
times.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
time.sleep(1)
times.send_keys("12a" + Keys.RETURN)
print("[BrinxBot]: Time has been changed")
# -------------------------------
# click OK
print("[BrinxBot]: Wrapping this up & selecting OK...")
click_ok = driver.find_element_by_css_selector(".CwButton-innerStandardActive").click()
print("[BrinxBot]: I have completed the task assigned... shutting off")
print("$- Connection has been lost to BrinxBot.")
print("---------------------------------------------------------------")