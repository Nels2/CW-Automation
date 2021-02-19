# CW-Automation
Attempting to fully automate ticketing...
So far this script can **complete** 4 different ticket types: (Disk Cleanup, Reboot/Update Pending, service edgeupdate has stopped, & NIC packet issue tickets)
This is merely a project I decided to go about to learn how to web scrape. I actually plan to use this script to automate opening tickets/closing tickets in ConnectWise, along with running a script in ConnectWise Automate that handles the ticket's issue.
Feel Free to use..
Requires selenium and geckodriver.

# NOTICE: This is WIP project.
CW-Automation is project I took on to teach myself how to web-scrape, and to make noise tickets a thing of the past. This script(s) is product of hours of research and testing.
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
Open up a code editor of your choice, and open up both 'CW.py' and 'AutomateConnection.py'\
We will start first with 'CW.py'\
- Once inside the file, press CTRL+F, this will bring a search bar.
- First you need to search for 'url'(Line 48)
- **Change the url to match your connectwise login site.**
- In the search bar, again, you want type: userd \
This will bring you to THREE values you need to change.
- **'comp'**(line 53) is where you will input your company name **INSIDE**  the quotation marks. for example for us it is 'centurytest'
- **'userd'**(line 54) is your username for ConnectWise.** make sure you type it INSIDE the quotation marks.**
- **'pasd'**(line 55) is your password for ConnectWise.** make sure you type it INSIDE the quotation marks.**
That is all you need to do for CW.py. make sure you hit **SAVE!** You can now close CW.py
# Editing! Part 2 of 2
Now that CW.py is taken care of, go back and open up 'AutomateConnection.py' in your choice of code editor.\
Once the file 'AutomateConnection.py' is open, press CTRL+F\
- **You are going to CTRL+F more than once.**
- First you need to search for 'url' (line 37)
- **Change the url to match your hoested rmm automate login site.**
- Next you need to change another thing, on Line 78, change the following ```driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1611956433&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de00d1cdc-7140-348d-ccae-406a5464dec6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld')``` to ```driver.get('insert_your_o365_login_site_here')``` 
- You are now looking for the value **'usrname'**
Once it is found, you need to edit the values for **'usrname'** and **'passwd'**. Make sure you edit inside the the quotation marks( ' ' ). 
- 'usrname' is your username for your login at Automate Control Center. 
- 'passwd' is your password for your login at Automate Control Center.
Once these fields have been entered, press CTRL+F again.
- The next value we are looking for is **'epwd'**
This will take you down to the Office 365 login information values. Make sure to enter your data INSIDE the quotation marks.
- **'email'**(line 81) is your email for Office 365.
- **'epwd'**(line 82) is your password for Office 365.
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
- Instead type out: ```sudo chmod +x start.sh```
- And to run it type out: ```./start.sh``` with either 1-4 or CW as an arguement
- So for example run it as ```./start.sh 1``` would run OP1(Reboot ticket type)
- Another Example is ```./start.sh CW``` would run the script with v1.5-2 method of completing tickets.
- type ```./start.sh h``` to see more information.
The script will begin to run. Make sure to pay attention to the terminal as well. 
