# CW-Automation
Attempting to fully automate ticketing or at least help in some way...
this script is to be used to **complete** following ticket types: 

**You need to edit this file(s):** cw/cw_howto.py \
This is merely a project I decided to go about to learn how to web scrape. I actually plan to use this script to automate opening tickets/closing tickets in ConnectWise, along with running a script in ConnectWise Automate that handles the ticket's issue.
Feel Free to use..
Requires selenium and geckodriver.
# NOTICE: This project is now being worked on again. it will be slow, but there will be a re-write and more to come soon!
CW-Automation is project I took on to teach myself how to web-scrape, and to make noise tickets a thing of the past. These/this script(s) is product of hours of research and testing.
# Step 1 - Starting Out
To start you **need** a *nix VM or *nix Machine. Works on mac as well(Tested on Big Sur) You need Python 3.5+ & Distro does not matter. I used Arch btw.

- You need to have the geckodriver in your /usr/local/bin directory.
geckodriver is a program that provides the HTTP API described by the WebDriver protocol to communicate with Gecko browsers, such as Firefox. It translates calls into the Marionette remote protocol by acting as a proxy between the local- and remote ends.
- You can grab the latest release from: https://github.com/mozilla/geckodriver/releases

# Step 2 - The Set Up
Next is to open up a terminal on your *nix install. 
- First you need to install the file requirements which are
1. selenium 
2. pyfiglet 
3. termcolor 
4. pickle \
You can install both using ```pip install selenium```, ```pip install pyfiglet```, ```pip install termcolor``` \
Great! next is cloning my repository from GitHub and changing into its directory.
- In a terminal, type out: ```git clone https://github.com/Nels2/CW-Automation.git```
after it is finished, change into its' directory by typing out: ```cd CW-Automation```
That is all for this step.

# Editing! Part 1 of 2
Open up a code editor of your choice, and open up `cw_howto.py` 
We will start first with the 'cw-xxx.py' files \
- Once inside the file(s), press CTRL+F, this will bring a search bar.
- First you need to search for 'url'
- **Change the url to match your connectwise login site.**
- In the search bar, again, you want type: userd \
This will bring you to THREE values you need to change.
- **'comp'** is where you will input your company name **INSIDE**  the quotation marks. for example for us it is 'centurytest'
- **'userd'** is your username for ConnectWise.** make sure you type it INSIDE the quotation marks.**
- **'pasd'** is your password for ConnectWise.** make sure you type it INSIDE the quotation marks.**
That is all you need to do for CW.py. make sure you hit **SAVE!** 
# Editing! Part 2 of 2 inside 
Now that in cw_howto.py the connectwise login information has been taken care of.\
the next part is changing the IT Glue Login.
- **You are going to CTRL+F more than once.**
- First you need to search for 'url_second=' 
- **Change the url to match your hoested rmm automate login site.**
- Next you need to change another thing in the cw-xxx.py files, change the following ```url_second=``` to ```url_second= "insert_your_itGlue_login_site_here"```
- You are now looking for the value **'useremail ='**.
Once it is found, you need to edit the values for **'useremail ='** and **'paswrd ='**. Make sure you edit inside the the quotation marks( ' ' ). 
- 'usrname' is your username for your login at Automate Control Center. 
- 'passwd' is your password for your login at Automate Control Center.
Once these fields have been entered, press CTRL+F again.
- The next value we are looking for is **'epwd'**
This will take you down to the ITglue login information values. Make sure to enter your data INSIDE the quotation marks.
- **'useremail'** is your email for ITglue.
- **'paswrd'** is your password for ITglue.
That is all for this step!, you should be good to go.

# Optional Step - Watch Live Steps at Server!
This is probably easier if you have to two displays, but:\
Open a browser up to a new tab and go to BruhBoxChat | BrinxBot (icxnelly.repl.co)\[https://bruhboxchat.icxnelly.repl.co/BrinxBot
this website chats with the Bot or in other words the script. You can see the status of the script here as it runs.\

# Running the script!
Now that everything has been configured, you are ready to begin the automation!\
- Open a terminal up and make sure you change into the CW-Automation directory, type out: ```cd CW-Automation```
- to run the script, type out: ```./start.sh T```. -**Note. This pulls the CW service board.**
- And to run the script for On-Core tickets: ```./start.sh 1```.
So for example run it as ```./start.sh 1``` would run OP1(Backup Missed ticket type) would run.
- type ```./start.sh H``` to see more information. 

After starting the script with your chosen arguement **(1,T,H)**, the script will run. **Make sure to pay attention to the terminal as well.** 
