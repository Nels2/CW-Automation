from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import re


# -- -- -- -- -- -- -- -- -- #
#    Created by Nelson O.    #
#        2021.01.29          #
#    AutomateConnection      #
# -- -- -- -- -- -- -- -- -- #

# --
# This script is intended to login into Automate and grab the verification code from an email to login.
# --

url = "https://seamlessdata.hostedrmm.com/automate/login"
driver = webdriver.Firefox()
driver.get(url)

time.sleep(3)
enter_user = driver.find_element_by_id('loginUsername')
enter_user.send_keys('NOrellana' + Keys.RETURN)
time.sleep(2)
pw = driver.find_element_by_id('loginPassword')
pw.send_keys('SDS0313no!' + Keys.RETURN)
time.sleep(1.5)

# now to login into my email and get code and go back to verify. Must be done withing 3-8 minutes or code is no longer valid.
# --- second tab --- #
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1611956433&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de00d1cdc-7140-348d-ccae-406a5464dec6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld')
time.sleep(2)
userN = driver.find_element_by_name('loginfmt')
userN.send_keys('norellana@seamlessdata.com' + Keys.RETURN)
time.sleep(3)
passwd = driver.find_element_by_name('passwd')
passwd.send_keys('NoSeamless20' + Keys.RETURN)
passwd.send_keys(Keys.RETURN)

# select 'No' to stay signed in.
time.sleep(1.5)
no = driver.find_element_by_css_selector("#idBtn_Back").click();
# time to open the email and grab the code...
time.sleep(5)
search_email = driver.find_element_by_css_selector('._1Qs0_GHrFMawJzYAmLNL2x')
search_email.send_keys('seamless' + Keys.RETURN)
time.sleep(3)
click_it = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[3]').click();
save_it = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[3]").text
print(save_it)
r = [re.split(r'(\d+)', s) for s in (save_it)]
print(r)
print(r[0])

# now to switch back.
#click_on_token = driver.find_element_by_id('loginToken')
#click_on_token.send_keys('')
