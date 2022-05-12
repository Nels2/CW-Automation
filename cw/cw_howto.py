from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException as WDE_er
from selenium.common.exceptions import ElementNotInteractableException as E_er
from selenium.common.exceptions import StaleElementReferenceException as S_er
from selenium.webdriver.common.by import By
from termcolor import colored, cprint
from timeit import default_timer as timer
import onetimepass as otp
import pathlib
import os
import time
from time import sleep
import pickle
import datetime

print_blue = lambda x: cprint(x, 'white', attrs=['bold'])
print_yellow = lambda x: cprint(x, 'yellow')
print_alt_yellow = lambda x: cprint(x, 'yellow', attrs=['underline'])
print_red = lambda x: cprint(x, 'red', attrs=['blink'])
print_green = lambda x: cprint(x, 'green')
print_alt_green = lambda x: cprint(x, 'green', attrs=['bold'])
url = ""#your CW login site
options = webdriver.FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.get(url)

def cwLogind():
    comp = ''
    userd = ''
    pasd = ''

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
    except E_er:
        pass
    except NoSuchElementException:
        pass
    print_green("#### -- Logged in! -- ####")

def serviceBoard_Pull():
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, 'GE0S-T1CAVF')))
    try:
        #TotalAMTT = driver.find_element_by_css_selector(".GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").text
        TotalAMTT = driver.find_element(by=By.CSS_SELECTOR, value ='.GE0S-T1CERG > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').text
        pass
    except S_er:
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

def serverConnect():
    try:
        print_yellow("#### -- Establishing External Connection to Server .. -- ####")
        the_url = "https://bruhboxchat.icxnelly.repl.co/BrinxBot"
        options = webdriver.FirefoxOptions()
        options.headless = True
        driverTwo = webdriver.Firefox(options=options)
        driverTwo.get(the_url)
        time.sleep(1)
        Connection = driverTwo.find_element_by_css_selector("#message")
        Connection.send_keys("/name BrinxBot" + Keys.RETURN)
        Connection.send_keys("Connection has been established ..." + Keys.RETURN)
        print_green("#### -- SUCCESS -- #####")
    except WDE_er:
        print_red("#### -- FAIL -- ####")
        print_red("Server Connection Failed. No login was made to the Server. Continuing...")
    driverTwo.quit()

def itGlueLogind():
    first_tab = pickle.load( open( "first_tab.p", "rb"))
    now = datetime.datetime.now()
    url_second = "" # make sure this is for YOUR itglue, where-ever it is hosted..
    options = webdriver.FirefoxOptions()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.execute_script("window.open('about:blank','tab2');")
    driver.switch_to.window("tab2")
    pre = "[" + now.strftime('%Y-%m-%d %I:%M:%S %P') + "]: "
    print_blue(pre + "[BrinxBot]: Switched to second Window. Focus is here currently.")
    print_yellow("#### --------- Begin IT Glue Connection --------- ####")
    alt_logo = colored('#### -- BrinxBot, an ICX Creation | Version 5.4 -- ####', 'red', attrs=['reverse', 'blink'])
    print(alt_logo)
    print_blue(pre + "[BrinxBot]: starting out.. login in to Automate is first task... commencing...")

    useremail = '' #usr login
    paswrd = ''

    usrEnter = driver.find_element(by=By.NAME, value='username')
    usrEnter.send_keys(useremail)
    passEnter = driver.find_element(by=By.NAME, value='password')
    passEnter.send_keys(paswrd)
    passEnter.send_keys(Keys.RETURN)
    # MFA junk....
    secret = 'bjs3obz3yphrvgq7olvlukc4uttldysh'
    mfacode = otp.get_totp(secret)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, 'mfa')))
    print_blue("MFA Code: " + str(mfacode))
    mfa_e = driver.find_element(By.NAME, "mfa")
    mfa_e.send_keys(mfacode)
    mfa_e.send_keys(Keys.RETURN)
    LoginVerify = True
    while LoginVerify:
        try:
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label.form-label:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')))
            print_green("#### -- Logged in! -- ####")
            pass
            break
        except ValueError:
            print_red("#### -- Unable to login. -- #####")
            pass 

def startTym():
    start = timer()
    print_yellow(start)
    pickle.dump( start, open( "startTime.p", "wb"))

def companyCheck():
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