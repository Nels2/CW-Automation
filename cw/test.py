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
#MarkResolve()
def computerz():
    if ticket_type == '*BM*':
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
#computerz()



first_tab_handle = driver.current_window_handle
current_url = driver.current_url
pickle.dump( current_url, open( "url.p", "wb"))
pickle.dump( first_tab_handle, open( "first_tab.p", "wb"))
print_yellow("#### -- first_tab_handle : " + str(first_tab_handle) + "-- ####")
time.sleep(2)
print("driver wouldve quit here ---------")
driver.quit()
def itGlueConnection():
    itGlueLogind()
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
    print_blue(pre + "[BrinxBot]: ...switching back to CW")
    print_yellow("#### -- Establishing Connecton to CW ... -- ####")
itGlueConnection()
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
if ticket_type == '*BM*':
    enter_notes.send_keys('[BrinxBot]: Python 3.10.4 was used to help with this ticket!')
    enter_notes.send_keys(Keys.SHIFT + Keys.RETURN)
    enter_notes.send_keys('[BrinxBot]: No further action is needed, Documentation has been added to hopefully help with Backup Missed issues.')
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
    except WDE_er:
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