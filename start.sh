#!/bin/bash
clear
echo $1
echo [BrinxBot]: Hello, $USER. I am BrinxBot and I will solve your ticketing issues!
echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $1.
if [ $1 == "H" ]
then 
    echo ------------ Ticket Types Information -------------
    echo  OP1 are Reboot pending Ticket types...start.sh 1
    echo  OP2 are edgeupdate stopped Ticket types... start.sh 2
    echo  OP3 are Disk Cleanup Ticket types... start.sh 3
    echo  OP4 are Nic Packet Error Ticket types...start.sh 4
    echo  CW is a compatability mode using the v1.5-5 method....start.sh CW
    echo above are the following arguments you can use with start.sh.
    echo after the ... above, is the correct way to pass an argument to start.sh
fi
if [ $1 == "1" ]
then 
    echo [BrinxBot]: Running reboot ticket type solver with new method...
    python3 ac-reboot.py
fi
if [ $1 == "2" ]
then 
    echo [BrinxBot]: Running edgeupdate ticket type solver with new method...
    python3 ac-edgeu.py
fi
if [ $1 == "3" ]
then 
    echo [BrinxBot]: Running Disk Cleanup ticket type solver with new method...
    python3 ac-diskcleanup.py
fi
if [ $1 == "4" ]
then 
    echo [BrinxBot]: Running NIC Packet Error ticket type solver with new method...
    python3 ac-nic.py
fi
if [ $1 == "CW" ]
then
    echo [BrinxBot]: Using Original Method to Complete Tickets...
    echo [BrinxBot]: WARNING: This method is not fully automated and requires your terminal attention.
    python3 AutomateConnection.py
fi
if [ $1 == "B1" ]
then 
    echo [BrinxBot]: Running BETA method w/ intergrated AC.py to check for computer before work...
    python3 cw-reboot.py
fi
if [ $1 == "B2" ]
then 
    echo [BrinxBot]: Running BETA method w/ intergrated AC.py to check for computer before work...
    python3 cw-edgeu.py
fi
if [ $1 == "B3" ]
then 
    echo [BrinxBot]: Running BETA method w/ intergrated AC.py to check for computer before work...
    python3 cw-diskcleanup.py
fi
if [ $1 == "B4" ]
then 
    echo [BrinxBot]: Running BETA method w/ intergrated AC.py to check for computer before work...
    python3 cw-nic.py
fi


