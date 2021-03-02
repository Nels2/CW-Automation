#!/bin/bash
clear
echo ---------------------------------------------------------------------------------
echo "[BrinxBot]: Hello, $USER. I am BrinxBot and I will solve your ticketing issues!"
echo "[BrinxBot]: $USER! you can view tickets and autocomplete with 'TB' instead of 'T'!"
if [ $1 == "1" ]
then 
    vartype=Reboot
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running reboot ticket type solver with current method..."
    python3 cw-reboot.py
fi
if [ $1 == "2" ]
then 
    vartype=edgeupdate
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running edgeupdate ticket type solver with current method..."
    python3 cw-edgeu.py
fi
if [ $1 == "3" ]
then 
    vartype=Disk_Cleanup
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running Disk Cleanup ticket type solver with current method..."
    python3 cw-diskcleanup.py
fi
if [ $1 == "4" ]
then 
    vartype=Nic_Packet_Error 
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running NIC Packet Error ticket type solver with current method..."
    python3 cw-nic.py
fi
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
if [ $1 == "T" ]
then 
    echo  ----------------- Loading Ticket Information From Today.. ----------------------
    python3 cw-srvcebrd.py
fi
if [ $1 == "TB" ]
then 
    echo  ----------------- Loading Ticket Information From Today.. ----------------------
    python3 cw-srvcebrd.py
    echo  -----------         Checking Ticket Amounts         ----------------
    file=ticket_types.txt
    if grep -q Reboot "$file"; then
        echo [BrinxBot]: Running reboot ticket type solver with current method...
        python3 cw-reboot.py
    else 
        echo "[BrinxBot]: No reboot type tickets according to ticket_types.txt, continuing to next ticket type..."
    fi 
    if grep -q edgeupdate "$file"; then
        echo [BrinxBot]: Running edgeupdate ticket type solver with current method...
        python3 cw-edgeu.py
    else 
        echo "[BrinxBot]: No edgeupdate type tickets according to ticket_types.txt, continuing to next ticket type..."
    fi 
    if grep -q Cleanup "$file"; then
        echo [BrinxBot]: Running Disk Cleanup ticket type solver with current method...
        python3 cw-diskcleanup.py
    else 
        echo "[BrinxBot]: No Disk Cleanup type tickets according to ticket_types.txt, continuing to next ticket type..."
    fi 
    if grep -q NIC "$file"; then
        echo [BrinxBot]: Running NIC Packet Error ticket type solver with current method...
        python3 cw-nic.py
    else 
        echo "[BrinxBot]: No NIC type tickets according to ticket_types.txt,..."
    fi 
    echo "[BrinxBot]: Done."
fi
echo "[BrinxBot]: Shutting Down..."


