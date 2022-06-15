from cw_howto import cwLogind, cwTicketTypeSearch, serverConnect, serverMessageSend, startTym, endTym, clickOnTicket, grabClientInfo, grabTicketInfo, saveCurrentWebLink, identify_POP, identify_VIP, itGlueLogind, itGlueSearch, itGlueLoadDocPage, pickle
# USE ONLY FOR gpkt TICKETS!!!
#  -----ConnectWise AutoBot, By Nels2------Built 2022.05.12 ----
# --------------------------------------------------------------
clientVIPStatus = False # this will show to be relevant later...
ticket_type = 'Get Product Keys Script Failed'  # service tickets where a backup is missed
pickle.dump( ticket_type, open( "tickets/ticket_info.p", "wb"))# dump ticket type so cwTicketSearch() can use it.
startTym()# Start timer to keep track of how long script takes to run.
serverConnect()#connect to my chat site to keep records of the work BrinxBot does.
cwLogind()# logs into ConnectWise.
cwTicketTypeSearch()# let the field populate... then searches for tickets that start with "Get Product Keys Failed" then clicks on the first one
clickOnTicket()#Next is viewing what the ticket is about to make sure it is correct before continuing...
identify_POP()# identify if there is a pop up on the screen, if so to close it.
print("[BrinxBot]: #### -- Downloading Ticket & Client Information ... -- ####")
identify_VIP()#identify if client is VIP or not.
grabClientInfo()# --grabbing client information-- 
grabTicketInfo()# -- grabbing ticket information --
saveCurrentWebLink()# saves current ticket page's link for future use.
serverMessageSend() # sends message to server of what brinxbot is currently working on.
itGlueLogind()# logs into IT Glue
itGlueSearch()# Searches in IT Glue for the company that was in the ticket.
itGlueLoadDocPage()# load "Documents" page of whatever comapny is loaded up.
endTym()# ends timer n prints time 