ifrom selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import re
import pickle
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

url = "https://seamlessdata.hostedrmm.com/automate/login"
driver = webdriver.Firefox()
driver.get(url)


print("#### ---- Begin Automate Connection ---- ####")
print("~  #####     #####     #####   ##       #  #       #    #####       #####    #########    ")
print("~  #    #    #    #      #     # #      #   #     #     #    #     #     #       #        ")
print("~  #     #   #     #     #     #  #     #    #   #      #     #   #       #      #        ")
print("~  #    #    #    #      #     #   #    #     # #       #    #    #       #      #        ")
print("~  #####     # ###       #     #    #   #      #        #####     #       #      #        ")
print("~  #    #    #    #      #     #     #  #     # #       #    #    #       #      #        ")
print("~  #     #   #     #     #     #      # #    #   #      #     #   #       #      #        ")
print("~  #    #    #      #    #     #       ##   #     #     #    #     #     #       #        ")
print("~  #####     #      #  #####   #        #  #       #    #####       #####        #        ")
print("~")
print("~")
print("[BrinxBot]: starting out.. login in to Automate is first task... commencing...")
time.sleep(3)
enter_user = driver.find_element_by_id('loginUsername')
enter_user.send_keys('' + Keys.RETURN)
time.sleep(2)
pw = driver.find_element_by_id('loginPassword')
pw.send_keys('' + Keys.RETURN)
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
userN = driver.find_element_by_name('loginfmt')
userN.send_keys('' + Keys.RETURN)
time.sleep(3)
passwd = driver.find_element_by_name('passwd')
passwd.send_keys('' + Keys.RETURN)
passwd.send_keys(Keys.RETURN)

# select 'No' to stay signed in.
time.sleep(1.5)
no = driver.find_element_by_css_selector("#idBtn_Back").click();
print("[BrinxBot]: No. I dont want to stay signed in... continuing")
# time to open the email and grab the code...
print("[BrinxBot]: I'm in! Going to look for the email and save the code..")
time.sleep(7)
search_email = driver.find_element_by_css_selector('._1Qs0_GHrFMawJzYAmLNL2x')
search_email.send_keys('Seamless data systems, inc. Monitoring' + Keys.RETURN)
time.sleep(4)
click_it = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]').click();
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
search_for_comp = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div:nth-child(3) > div.CwDataGrid-headerViewport > div > span:nth-child(1) > div > div.CwDataGrid-filterContainer > input")
print("[BrinxBot]: Computer has been found clicking on it to continue the task...")
search_for_comp.send_keys(computer + Keys.Return)
element = driver.find_element_by_css_selector("#root > div > div > div > div.browse-container > div.company-container > div.company-content > div:nth-child(3) > div.CwDataGrid-rowsContainer > div > div > span:nth-child(1) > div")
# save this tab so i can return to it
second_tab_handle = driver.current_window_handle
print("second_tab_handle : "+str(second_tab_handle)) # right before computer screen 
# the 3 lines below are to double click on the computer and open it.
action = ActionChains(driver)
action.double_click(on_element=element)
action.perform() # this will open a new screen to the computer itself to begin managing it.
