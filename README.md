# CW-Automation
Attempting to fully automate ticketing...
So far this script can **complete** 4 different ticket types: 

- Reboot/Update Pending(./start.sh 1) \
FILES TO EDIT: cw-reboot.py 
- service edgeupdate has stopped(./start.sh 2) \
FILES TO EDIT: cw-edgeu.py 
- Disk Cleanup(./start.sh 3) \
FILES TO EDIT: cw-disckcleanup.py
- NIC packet issue tickets(./start.sh 4) \
FILES TO EDIT: cw-nic.py
*You also need to edit this file:* cw-srvcebrd.py
This is merely a project I decided to go about to learn how to web scrape. I actually plan to use this script to automate opening tickets/closing tickets in ConnectWise, along with running a script in ConnectWise Automate that handles the ticket's issue.
Feel Free to use..
Requires selenium and geckodriver.
# NOTICE: This is a WIP project.
CW-Automation is project I took on to teach myself how to web-scrape, and to make noise tickets a thing of the past. These/this script(s) is product of hours of research and testing.
# Step 1 - Starting Out
To start you **need** a *nix VM or *nix Machine. Works on mac as well(Tested on Big Sur) You need Python 3.5+ & Distro does not matter. I used Arch btw.

- You need to have the geckodriver in your /usr/local/bin directory.
geckodriver is a program that provides the HTTP API described by the WebDriver protocol to communicate with Gecko browsers, such as Firefox. It translates calls into the Marionette remote protocol by acting as a proxy between the local- and remote ends.
- You can grab the latest release from: https://github.com/mozilla/geckodriver/releases

# Step 2 - The Set Up
Next is to open up a terminal on your *nix install. 
- First you need to install the file requirements which are 1. selenium and 2. pyfiglet.
you can install both using ```pip install selenium``` and ```pip install pyfiglet``` \
Great! next is cloning my repository from GitHub and changing into its directory.
- In a terminal, type out: ```git clone https://github.com/Nels2/CW-Automation.git```
after it is finished, change into its' directory by typing out: ```cd CW-Automation```
That is all for this step.

# Editing! Part 1 of 2
Open up a code editor of your choice, and open up both 'cw-diskcleanup.py', 'cw-edgeu.py', 'cw-nic.py', 'cw-reboot.py' 
We will start first with the 'cw-xxx.py' files \
- Once inside the file(s)(you need to do this for all 4!), press CTRL+F, this will bring a search bar.
- First you need to search for 'url'
- **Change the url to match your connectwise login site.**
- In the search bar, again, you want type: userd \
This will bring you to THREE values you need to change.
- **'comp'** is where you will input your company name **INSIDE**  the quotation marks. for example for us it is 'centurytest'
- **'userd'** is your username for ConnectWise.** make sure you type it INSIDE the quotation marks.**
- **'pasd'** is your password for ConnectWise.** make sure you type it INSIDE the quotation marks.**
That is all you need to do for CW.py. make sure you hit **SAVE!** You can now close all cw-xxx.py files
# Editing! Part 2 of 2 inside 
Now that in cw-xxx.py the connectwise login information has been taken care of, keep open up all **4** 'cw-xxx.py' files in your choice of code editor.\
once again, in the file(s) 'cw-xxx.py' are open(start with any, but make sure you do all four!), press CTRL+F\
the next part is changing the Automate Login / your O365 Login.
- **You are going to CTRL+F more than once.**
- First you need to search for 'url' 
- **Change the url to match your hoested rmm automate login site.**
- Next you need to change another thing, on Line 78, change the following ```driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1611956433&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de00d1cdc-7140-348d-ccae-406a5464dec6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld')``` to ```driver.get('insert_your_o365_login_site_here')``` 
- You are now looking for the value **'usrname'**
Once it is found, you need to edit the values for **'usrname'** and **'passwd'**. Make sure you edit inside the the quotation marks( ' ' ). 
- 'usrname' is your username for your login at Automate Control Center. 
- 'passwd' is your password for your login at Automate Control Center.
Once these fields have been entered, press CTRL+F again.
- The next value we are looking for is **'epwd'**
This will take you down to the Office 365 login information values. Make sure to enter your data INSIDE the quotation marks.
- **'email'** is your email for Office 365.
- **'epwd'** is your password for Office 365.
That is all for this step!, you should be good to go.

# Optional Step - Watch Live Steps at Server!
This is probably easier if you have to two displays, but:\
Open a browser up to a new tab and go to BruhBoxChat | BrinxBot (nels277.repl.co)\
this website chats with the Bot or in other words the script. You can see the status of the script here as it runs.\

# Running the script!
Now that everything has been configured, you are ready to begin the automation!\
- Open a terminal up and make sure you change into the CW-Automation directory, type out: ```cd CW-Automation```
- Next to run the script, type out: ```python3 AutomateConnection.py```\
#Optional
- Open a terminal up and make sure you change into the CW-Automation directory, type out: ```cd CW-Automation```
- Next type out: ```sudo chmod +x start.sh```
- And to run it type out: ```./start.sh``` with either 1-4, T, or TB as an arguement
So for example run it as ```./start.sh 1``` would run OP1(Reboot ticket type) would run.
- Alternatively, type out ```./start.sh TB``` for an alternate method that auto completes tickets for you *unless* the machine is offline, you will have to input y/n if you want the script to complete the ticket for it anyway(*Not recommended to complete anyway*). 
If you want just a return of the tickets on the service board, type out: ```./start.sh T``` and you can decide from there which OP to run ```./script.sh (1-4)```.
- type ```./start.sh H``` to see more information.
The script will begin to run. Make sure to pay attention to the terminal as well. 
