from selenium.common.exceptions import NoSuchElementException
from cw_howto import cwLogind, lookForNewTixOnly, serviceBoard_Pull, loadTicketAmt, nextPageClick, startTym, endTym, pickle, print_blue, print_alt_yellow, print_yellow, print_red
import re
# Created by Nelson Orellana (Nels2 @ GitHub), 2021.26.02 updated: 2022.05.10
# This script is intended to grab todays(date ran) service board to get an overview of tickets without having to login.
#
startTym()
cwLogind() #log into CW
lookForNewTixOnly() #enters 'New' for ticket type
serviceBoard_Pull() # pulls the service board
loadTicketAmt() # loads ticket amount from file(s) # fix
total_d = pickle.load( open( "tickets/DC.p", "rb"))
total_dc = int(total_d)
total_bml = pickle.load( open( "tickets/BM.p", "rb"))
total_bm = int(total_bml)
total_g = pickle.load( open( "tickets/GPKT.p", "rb"))
total_gpkt = int(total_g)
if total_gpkt <= 1 or total_dc <= 1:# run as long there are no tickets to do on page 1
    PGamt = pickle.load( open( "tickets/DC.p", "rb"))
    Amts = pickle.load( open( "tickets/DC.p", "rb"))
    if PGamt == Amts:# make sure this isnt the first page again by comparing total tickets on page versus total
        print_red('[BrinxBot]: #### -- There is not another page of tickets to pull. -- ####')
        pass
    else:
        nextPageClick()
        serviceBoard_Pull()
        loadTicketAmt()
        total_gpkt, total_bm=loadTicketAmt()
    if total_gpkt <= 1 or total_dc <= 1:#usually the final page, had to make some adjustments as it final page loads differently.
        if PGamt == Amts:
            print_red('[BrinxBot]: #### -- There is not another page of tickets to pull. -- ####')
            pass
        else:
            try:
                serviceBoard_Pull()
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
                print('[BrinxBot]: #### -- End of Ticket List for this Page'+ '(' + PGAmt + ' of '+ Amts + ') -- ####')
                print_green("[BrinxBot]: Generated ticket menu! displaying.. ")
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
                serviceBoard_Pull()
                loadTicketAmt()
    else:
        pass
else:
    pass
endTym()
