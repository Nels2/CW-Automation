#!/bin/bash
clear
echo ---------------------------------------------------------------------------------
echo $1
echo [BrinxBot]: Hello, $USER. I am BrinxBot and I will solve your ticketing issues!
echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $1.
if [ $1 == "H" ]
then 
    echo  ----------- Ticket Types Information ----------------
    echo  OP1 is Reboot pending Ticket type...     ./start.sh 1      
    echo  OP2 is edgeupdate stopped Ticket type... ./start.sh 2 
    echo  OP3 is Disk Cleanup Ticket type...       ./start.sh 3 
    echo  OP4 is Nic Packet Error Ticket type...   ./start.sh 4 
    echo  -----------------------------------------------------
    echo Above are the following arguments you can use with start.sh.
    echo After the ... above, is the correct way to pass an argument to start.sh
fi
if [ $1 == "1" ]
then 
    echo [BrinxBot]: Running reboot ticket type solver with new method...
    python3 cw-reboot.py
fi
if [ $1 == "2" ]
then 
    echo [BrinxBot]: Running edgeupdate ticket type solver with new method...
    python3 cw-edgeu.py
fi
if [ $1 == "3" ]
then 
    echo [BrinxBot]: Running Disk Cleanup ticket type solver with new method...
    python3 cw-diskcleanup.py
fi
if [ $1 == "4" ]
then 
    echo [BrinxBot]: Running NIC Packet Error ticket type solver with new method...
    python3 cw-nic.py
fi

