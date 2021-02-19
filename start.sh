#!/bin/bash
clear
echo $1
echo [BrinxBot]: Hello, $USER. I am BrinxBot and I will solve your ticketing issues!
echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $1.
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
