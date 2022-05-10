from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
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
import pathlib
import datetime
import pickle

# Created by Nelson Orellana (Nels2 @ GitHub), 2021.26.02 updated: 2022.05.10
# This script is intended to grab todays(date ran) serviceboard to get an overview of tickets without having to login.
# If used with arguement 'TB' (./start.sh TB), service board will e pulled and then tickets are completed in the following order: Reboot -> Edge Update -> Disk Cleanup -> NIC, this method is fully automated.
#
print_blue = lambda x: cprint(x, 'white', attrs=['bold'])
print_yellow = lambda x: cprint(x, 'yellow')
print_alt_yellow = lambda x: cprint(x, 'yellow', attrs=['underline'])
print_red = lambda x: cprint(x, 'red', attrs=['blink'])
print_green = lambda x: cprint(x, 'green')
url = "https://connect.meriplex.com/v4_6_release/ConnectWise.aspx?locale=en_US&session=new#XQAACACcAQAAAAAAAAA9iIoG07$U9XZqpLgsNhRsI0O_rEHSzQCIbZUnpNMnJHh0NVQu8_9CNKe1j4TEYyVEdozpnPQYwn2gHajNKgAhBQ4qyXulgFoHPkqbF7cPfraUe46uW_k4OgSN159DL3G5fxtlMUXJDZKDNh2SwRdfedRXG0hAOkUKYzWib8MBD79p7v1Say1m82f4d9d_jr3kJNeiSsjWbqQF4KrfCnUdS6G$P7bjyHwTH$DzOFUxpwlaeAVL$dH8gw==??ServiceBoard"#your CW login site
options = webdriver.FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.get(url)

def CWlogind():
    comp = 'meriplex'
    userd = 'nelson.orellana'
    pasd = 'Meriplex2022!'

    u = driver.find_element(by=By.NAME, value='CompanyName')
    u.send_keys(comp)
    s = driver.find_element(by=By.NAME, value='UserName')
    s.send_keys(userd)
    p = driver.find_element(by=By.NAME, value='Password')
    p.send_keys(pasd)
    p.send_keys(Keys.RETURN)
    # MFA junk....
    time.sleep(3)
    driver.switch_to.frame('authenticationFrame')
    mfacode = input("enter mfa code please: ")
    mfa_e = driver.find_element(By.NAME, "auth_pin")
    mfa_e.send_keys(mfacode)
    mfa_e.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.switch_to.default_content()
    # clicking proceed so i can continue
    try:
        time.sleep(3)
        #pro_clk = driver.find_element_by_xpath("//input[@value='Proceed']")
        pro_clk = driver.find_element(by=By.XPATH, value ='//input[@value="Proceed"]')
        pro_clk.click()
        print_yellow("#### -- Proceed was clicked -- ####")
    except ElementNotInteractableException:
        pass
    except NoSuchElementException:
        pass
    print_green("#### -- Logged in! -- ####")
CWlogind()
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'Summary-input')))
#status_of_tickets = driver.find_element_by_xpath('//*[@id="Description-input"]')
status_of_tickets = driver.find_element(by=By.XPATH, value ='//*[@id="Description-input"]')
status_of_tickets.send_keys("New")
status_of_tickets.send_keys(Keys.RETURN)
time.sleep(1)
def ServiceBoard_Pull():
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
    try:
        #TotalAMTT = driver.find_element_by_css_selector(".GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        TotalAMTT = driver.find_element(by=By.CSS_SELECTOR, value ='.GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').text
        pass
    except StaleElementReferenceException:
        #TotalAMTT = driver.find_element_by_css_selector(".GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        TotalAMTT = driver.find_element(by=By.CSS_SELECTOR, value ='.GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').text
    stri = TotalAMTT
    Amt = stri.split("- ",1)[1]
    stri = Amt
    PGAmt = stri.split(" of",1)[0]
    PGAmt4loop = 40
    stri = TotalAMTT
    Amts = stri.split("of ",1)[1]
    driver.implicitly_wait(2)

    x = int(PGAmt4loop)
    i = int(1)
    file = pathlib.Path("ticket_types.txt")
    if file.exists():
        os.remove("ticket_types.txt")
        print_yellow("ticket_types.txt has been cleared!")
        creatd = open('ticket_types.txt', 'w')
        creatd.close()
    else:
        pass
    while i < x:
        path2 = "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[2]" # ticket number
        if "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[2]" in path2:
            sreplacement = "/tr[" + str(i) + "]/td[2]"
            suni = path2.replace('/tr[1]/td[2]', sreplacement)
            path2 = suni
            pass
        path1 = "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[7]" # ticket description
        if "/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/table/tbody[2]/tr[1]/td[7]" in path1:
            replacement = "/tr[" + str(i) + "]/td[7]"
            uni = path1.replace('/tr[1]/td[7]', replacement)
            path1 = uni
            pass
        path0 = 'tr.GE0S-T1CGWF:nth-child(1) > td:nth-child(6) > div:nth-child(1)' # ticket company it belongs to.
        if 'tr.GE0S-T1CGWF:nth-child(1) > td:nth-child(6) > div:nth-child(1)' in path0:
            dreplacement = "tr.GE0S-T1CGWF:nth-child(" + str(i) + ") > td:nth-child(6) > div:nth-child(1)"
            duni = path0.replace('tr.GE0S-T1CGWF:nth-child(1) > td:nth-child(6) > div:nth-child(1)', dreplacement)
            path0 = duni
            pass
        #print(i)
        if i > x:
            i = 1
            pass
        pickle.dump( str(PGAmt), open( "tickets/PGAmt.p", "wb"))
        pickle.dump( Amts, open( "tickets/Amts.p", "wb"))
        #TicketNumber = driver.find_element_by_xpath(path2).text
        TicketNumber = driver.find_element(by=By.XPATH, value =(path2)).text
        #Ticketlist = driver.find_element_by_xpath(path1).text
        Ticketlist = driver.find_element(by=By.XPATH, value =(path1)).text
        TicketCompany = driver.find_element(by=By.CSS_SELECTOR, value =(path0)).text
        if 'Reboot' in Ticketlist:
            ticketT = 'Reboot Type'
            pass
        elif 'Get Product Keys Script Failed' in Ticketlist:
            ticketT= 'GPK Type'
            pass
        elif 'Drive Space Critical' in Ticketlist:
            ticketT = 'Disk Cleanup Type'
            pass
        elif 'Drive Error' in Ticketlist:
            ticketT= 'Drive Error Type'
            pass
        elif 'Offline' in Ticketlist:
            ticketT = 'Out of Date PC'
            pass
        elif 'Webroot' in Ticketlist:
            ticketT = 'WebRoot Error'
            pass
        elif 'Machine' in Ticketlist:
            ticketT= 'Machine Missing Patches Type'
            pass
        elif 'TCP' in Ticketlist:
            ticketT = 'TCP Error Type'
            pass
        elif 'Brute Force Attack' in Ticketlist:
            ticketT= 'Brute Force Attack Type'
            pass
        elif 'Backup Missed' in Ticketlist:
            ticketT = 'Backup Missed Type'
            pass
        else:
            ticketT = 'Unknown'
            pass
        with open('ticket_types.txt', 'a') as f:
            print("Ticket Type: ", ticketT, file=f)
        print_alt_yellow('Ticket Number[#] & Type: ' + TicketNumber + ' & ' + ticketT + ": ")
        print_blue('->> Ticket Company Name: ' + TicketCompany)
        print_blue('->> Ticket Information:  ' + Ticketlist)
        print_blue('-*-*-*-*-*--*-*-*-*-*--*-*-*-*-*--*-*-*-')
        if i == x:
            break
        else:
            i += 1
        pass
    total_gpk = 0
    total_mmp = 0
    total_tcp = 0
    total_bfa = 0
    total_dc = 0
    total_de = 0
    total_bm = 0
    total_reb = 0
    total_OD = 0
    total_WE = 0
    total_UT = 0
    count = 0
    with open('ticket_types.txt') as f:
        for line in f:
            found_gpk = line.find('GPK Type')
            if found_gpk != -1 and found_gpk != 0:
                total_gpk += 1
            found_mmp = line.find('Machine Missing Patches Type')
            if found_mmp != -1 and found_mmp != 0:
                total_mmp += 1
            found_tcp = line.find('TCP Error Type')
            if found_tcp != -1 and found_tcp != 0:
                total_tcp += 1
            found_bfa = line.find('Brute Force Attack Type')
            if found_bfa != -1 and found_bfa != 0:
                total_bfa += 1
            found_bm = line.find('Backup Missed Type')
            if found_bm != -1 and found_bm != 0:
                total_bm += 1
            found_dc = line.find('Disk Cleanup Type')
            if found_dc != -1 and found_dc != 0:
                total_dc += 1
            found_de = line.find('Drive Error Type')
            if found_de != -1 and found_de != 0:
                total_de += 1
            found_reb = line.find('Reboot Type')
            if found_reb != -1 and found_reb != 0:
                total_reb += 1
            found_OD = line.find('Out of Date PC')
            if found_OD != -1 and found_OD != 0:
                total_OD += 1
            found_WE = line.find('WebRoot Error')
            if found_WE != -1 and found_WE != 0:
                total_WE += 1
            found_UT = line.find('Unknown')
            if found_UT != -1 and found_UT != 0:
                total_UT += 1
    print('#### -- End of Ticket List for this Page'+ '(' + PGAmt + ' of '+ Amts + ') -- ####')
    print_yellow("#### -- Total Amount of Tickets Today Under the Alerts Board: " + Amts + " -- ####")
    print_yellow("#### -- Total Amount of Tickets Today Under This Page Only:   " + PGAmt + " -- ####")
    print_alt_yellow('#### -- Total Amount of Each Ticket Type Today On This Page -- ####')
    print_blue("|    Out of Date/Offline PC:                   "+str(total_OD)+"      ")
    print_blue("|    Disk Cleanup Type:                        "+str(total_dc)+"      ")
    print_blue("|    Drive Error Type:                         "+str(total_de)+"      ")
    print_blue("|    WebRoot Error Type:                       "+str(total_WE)+"      ")
    print_blue("|    Machine Missing Patches Type:             "+str(total_mmp)+"     ")
    print_blue("|    'Get Product Keys Failed' Type:           "+str(total_gpk)+"     ")
    print_blue("|    TCP Error Type:                           "+str(total_tcp)+"     ")
    print_blue("|    Brute Force Attack Type:                  "+str(total_bfa)+"     ")
    print_blue("|    Backup Missed Type:                       "+str(total_bm)+"     ")
    print_blue("|    Unknown:                                  "+str(total_UT)+"      ")
    print_alt_yellow('#### --   Ticket Types That BrinxBot Can Work(red.):  -- ####')
    print_blue("|    Out of Date/Offine PC Type:               "+str(total_OD)+"      ")
    pickle.dump( str(total_OD), open( "tickets/OD.p", "wb"))
    pickle.dump( str(count), open( "count/OD_count.p", "wb"))
    print_blue("|    Disk Cleanup Type:                        "+str(total_dc)+"      ")
    pickle.dump( str(total_dc), open( "tickets/DC.p", "wb"))
    pickle.dump( str(count), open( "count/dc_count.p", "wb"))
    print_blue("|    Drive Error Type:                         "+str(total_de)+"      ")
    pickle.dump( str(total_de), open( "tickets/DE.p", "wb"))
    pickle.dump( str(count), open( "count/de_count.p", "wb"))
    print_blue("|    WebRoot Error Type:                       "+str(total_WE)+"      ")
    pickle.dump( str(total_WE), open( "tickets/WE.p", "wb"))
    pickle.dump( str(count), open( "count/WE_count.p", "wb"))
    print_blue("|    'Get Product Keys Failed' Type:           "+str(total_gpk)+"      ")
    pickle.dump( str(total_gpk), open( "tickets/GPKT.p", "wb"))
    pickle.dump( str(count), open( "count/gpkt_count.p", "wb"))
    print_blue("|    TCP Error Type:                           "+str(total_tcp)+"      ")
    pickle.dump( str(total_tcp), open( "tickets/TCP.p", "wb"))
    pickle.dump( str(count), open( "count/TCP_count.p", "wb"))
    print_yellow('#### ---------------------------------------------------------- ####')
ServiceBoard_Pull()
total_ood = pickle.load( open( "tickets/OD.p", "rb"))
total_OD = int(total_ood)
total_d = pickle.load( open( "tickets/DC.p", "rb"))
total_dc = int(total_d)
total_def = pickle.load( open( "tickets/DE.p", "rb"))
total_de = int(total_d)
total_w = pickle.load( open( "tickets/WE.p", "rb"))
total_WE = int(total_w)
total_d = pickle.load( open( "tickets/DC.p", "rb"))
total_dc = int(total_d)
total_g = pickle.load( open( "tickets/GPKT.p", "rb"))
total_gpkt = int(total_g)
total_tet = pickle.load( open( "tickets/TCP.p", "rb"))
total_tcp = int(total_tet)
#print('run1pull: ' + str(total_reb) + ' | ' + str(total_gpkt) + ' | ' + str(total_egu) + ' | ' + str(total_dc) + ' | ' + str(total_dc) + ' | ' + str(total_nic))
pass
if total_gpkt <= 1 or total_dc <= 1:
    print_yellow('#### -----------Pulling Page 2-------- ####')
    driver.find_element_by_css_selector('div.GE0S-T1CIRG:nth-child(4)').click()
    driver.implicitly_wait(8)
    print_yellow('#### -----------Page 2 Pull:  -------- ####')
    ServiceBoard_Pull()
    total_ood = pickle.load( open( "tickets/OD.p", "rb"))
    total_OD = int(total_ood)
    total_d = pickle.load( open( "tickets/DC.p", "rb"))
    total_dc = int(total_d)
    total_def = pickle.load( open( "tickets/DE.p", "rb"))
    total_de = int(total_d)
    total_w = pickle.load( open( "tickets/WE.p", "rb"))
    total_WE = int(total_w)
    total_d = pickle.load( open( "tickets/DC.p", "rb"))
    total_dc = int(total_d)
    total_g = pickle.load( open( "tickets/GPKT.p", "rb"))
    total_gpkt = int(total_g)
    total_tet = pickle.load( open( "tickets/TCP.p", "rb"))
    total_tcp = int(total_tet)
    #print('run2pull: ' + str(total_reb) + ' | ' + str(total_gpkt) + ' | ' + str(total_egu) + ' | ' + str(total_dc) + ' | ' + str(total_dc) + ' | ' + str(total_nic))
    pass
    if total_gpkt <= 1 or total_dc <= 1:#usually the final page, had to make some adjustments as it final page loads differently.
        print_yellow('#### -----------Pulling Page 3-------- ####')
        driver.find_element_by_css_selector('div.GE0S-T1CIRG:nth-child(4)').click()
        driver.implicitly_wait(8)
        print_yellow('#### -----------Page 3 Pull:  -------- ####')
        try:
            ServiceBoard_Pull()
        except NoSuchElementException:
            total_gpk = 0
            total_mmp = 0
            total_tcp = 0
            total_bfa = 0
            total_dc = 0
            total_de = 0
            total_bm = 0
            total_reb = 0
            total_OD = 0
            total_WE = 0
            total_UT = 0
            count = 0
            with open('ticket_types.txt') as f:
                for line in f:
                    found_gpk = line.find('GPK Type')
                    if found_gpk != -1 and found_gpk != 0:
                        total_gpk += 1
                    found_mmp = line.find('Machine Missing Patches Type')
                    if found_mmp != -1 and found_mmp != 0:
                        total_mmp += 1
                    found_tcp = line.find('TCP Error Type')
                    if found_tcp != -1 and found_tcp != 0:
                        total_tcp += 1
                    found_bfa = line.find('Brute Force Attack Type')
                    if found_bfa != -1 and found_bfa != 0:
                        total_bfa += 1
                    found_bm = line.find('Backup Missed Type')
                    if found_bm != -1 and found_bm != 0:
                        total_bm += 1
                    found_dc = line.find('Disk Cleanup Type')
                    if found_dc != -1 and found_dc != 0:
                        total_dc += 1
                    found_de = line.find('Drive Error Type')
                    if found_de != -1 and found_de != 0:
                        total_de += 1
                    found_reb = line.find('Reboot Type')
                    if found_reb != -1 and found_reb != 0:
                        total_reb += 1
                    found_OD = line.find('Out of Date PC')
                    if found_OD != -1 and found_OD != 0:
                        total_OD += 1
                    found_WE = line.find('WebRoot Error')
                    if found_WE != -1 and found_WE != 0:
                        total_WE += 1
                    found_UT = line.find('Unknown')
                    if found_UT != -1 and found_UT != 0:
                        total_UT += 1
            Amts = pickle.load( open( "tickets/Amts.p", "rb"))
            PGAmt = pickle.load( open( "tickets/PGAmt.p", "rb"))
            print('#### -- End of Ticket List for this Page'+ '(' + PGAmt + ' of '+ Amts + ') -- ####')
            print_yellow("#### -- Total Amount of Tickets Today Under the Alerts Board: " + Amts + " -- ####")
            print_alt_yellow('#### -- Total Amount of Each Ticket Type Today On This Page -- ####')
            print_blue("|    Out of Date/Offline PC:                   "+str(total_OD)+"      ")
            print_blue("|    Disk Cleanup Type:                        "+str(total_dc)+"      ")
            print_blue("|    Drive Error Type:                         "+str(total_de)+"      ")
            print_blue("|    WebRoot Error Type:                       "+str(total_WE)+"      ")
            print_blue("|    Machine Missing Patches Type:             "+str(total_mmp)+"     ")
            print_blue("|    'Get Product Keys Failed' Type:           "+str(total_gpk)+"     ")
            print_blue("|    TCP Error Type:                           "+str(total_tcp)+"     ")
            print_blue("|    Brute Force Attack Type:                  "+str(total_bfa)+"     ")
            print_blue("|    Backup Missed Type:                       "+str(total_bm)+"     ")
            print_blue("|    Unknown:                                  "+str(total_UT)+"      ")
            print_alt_yellow('#### --   Ticket Types That BrinxBot Can Work(red.):  -- ####')
            print_blue("|    Out of Date/Offine PC Type:               "+str(total_OD)+"      ")
            pickle.dump( str(total_OD), open( "tickets/OD.p", "wb"))
            pickle.dump( str(count), open( "count/OD_count.p", "wb"))
            print_blue("|    Disk Cleanup Type:                        "+str(total_dc)+"      ")
            pickle.dump( str(total_dc), open( "tickets/DC.p", "wb"))
            pickle.dump( str(count), open( "count/dc_count.p", "wb"))
            print_blue("|    Drive Error Type:                         "+str(total_de)+"      ")
            pickle.dump( str(total_de), open( "tickets/DE.p", "wb"))
            pickle.dump( str(count), open( "count/de_count.p", "wb"))
            print_blue("|    WebRoot Error Type:                       "+str(total_WE)+"      ")
            pickle.dump( str(total_WE), open( "tickets/WE.p", "wb"))
            pickle.dump( str(count), open( "count/WE_count.p", "wb"))
            print_blue("|    'Get Product Keys Failed' Type:           "+str(total_gpk)+"      ")
            pickle.dump( str(total_gpk), open( "tickets/GPKT.p", "wb"))
            pickle.dump( str(count), open( "count/gpkt_count.p", "wb"))
            print_blue("|    TCP Error Type:                           "+str(total_tcp)+"      ")
            pickle.dump( str(total_tcp), open( "tickets/TCP.p", "wb"))
            pickle.dump( str(count), open( "count/TCP_count.p", "wb"))
            print_yellow('#### ---------------------------------------------------------- ####')
            ServiceBoard_Pull()
            total_ood = pickle.load( open( "tickets/OD.p", "rb"))
            total_OD = int(total_ood)
            total_d = pickle.load( open( "tickets/DC.p", "rb"))
            total_dc = int(total_d)
            total_def = pickle.load( open( "tickets/DE.p", "rb"))
            total_de = int(total_d)
            total_w = pickle.load( open( "tickets/WE.p", "rb"))
            total_WE = int(total_w)
            total_d = pickle.load( open( "tickets/DC.p", "rb"))
            total_dc = int(total_d)
            total_g = pickle.load( open( "tickets/GPKT.p", "rb"))
            total_gpkt = int(total_g)
            total_tet = pickle.load( open( "tickets/TCP.p", "rb"))
            total_tcp = int(total_tet)
            #print('run3pull: ' + str(total_reb) + ' | ' + str(total_gpkt) + ' | ' + str(total_egu) + ' | ' + str(total_dc) + ' | ' + str(total_dc) + ' | ' + str(total_nic))
            pass
    else:
        pass
else:
    pass
driver.quit()
