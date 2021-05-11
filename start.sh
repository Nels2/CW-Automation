#!/bin/bash
clear
echo ---------------------------------------------------------------------------------
echo "_BBBBBB____RRRRRR___I__NN________N__X_________X__BBBBBB_______OO_____TTTTTTT__!!!_"
echo "_B_____B___R_____R__I__N_N_______N___X_______X___B_____B____OO__OO______T_____!!!_"
echo "_B______B__R_____R__I__N__N______N____X_____X____B______B__O______O_____T_____!!!_"
echo "_B_____B___RRRRRR___I__N___N_____N_____X___X_____B_____B___O______O_____T_____!!!_"
echo "_BBBBBB____R_R______I__N____N____N______X_X______BBBBBB____O______O_____T_____!!!_"
echo "_BBBBBB____R__R_____I__N_____N___N_______X_______BBBBBB____O______O_____T_____!!!_"
echo "_B_____B___R___R____I__N______N__N______X_X______B_____B___O______O_____T_____!!!_"
echo "_B_____ B__R____R___I__N_______N_N_____X___X_____B______B__O______O_____T_____!!!_"
echo "_B_____B___R_____R__I__N________NN____X_____X____B_____B____OO__OO______T_________"
echo "_BBBBBB____R_____R__I__N_________N___X_______X___BBBBBB_______OO________T______o__"
echo "[BrinxBot]: Hello, $USER. I am BrinxBot and I will solve your ticketing issues!"
if [ $1 == "T" ]
then 
    echo "[BrinxBot]: $USER! you can view tickets and autocomplete with 'TB' instead of 'T'!"
else
    echo "[BrinxBot]: $USER! I will complete the task!"
fi 

if [ $1 == "1" ]
then 
    vartype=Reboot
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running reboot ticket type solver with current method..."
    python3 cw/cw-reboot.py
fi
if [ $1 == "2" ]
then 
    vartype=edgeupdate
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running edgeupdate ticket type solver with current method..."
    python3 cw/cw-edgeu.py
fi
if [ $1 == "3" ]
then 
    vartype=Disk_Cleanup
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running Disk Cleanup ticket type solver with current method..."
    python3 cw/cw-diskcleanup.py
fi
if [ $1 == "4" ]
then 
    vartype=Nic_Packet_Error 
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running NIC Packet Error ticket type solver with current method..."
    python3 cw/cw-nic.py
fi
if [ $1 == "H" ]
then 
    clear
    echo  ----------- Ticket Types Information ----------------
    echo  OP1 is Reboot pending Ticket type...     ./start.sh 1      
    echo  OP2 is edgeupdate stopped Ticket type... ./start.sh 2 
    echo  OP3 is Disk Cleanup Ticket type...       ./start.sh 3 
    echo  OP4 is Nic Packet Error Ticket type...   ./start.sh 4 
    echo  -----------------------------------------------------
    echo  -----------  Additional Information  ----------------
    echo  T is to pull the Service Board to the Terminal...
    echo  TB is to pull srbrd and autocomplete tickets...
    echo  A is to pull All agent statuses....
    echo  -----------------------------------------------------
    echo Above are the following arguments you can use with start.sh.
    echo After the above, is the correct way to pass an argument to start.sh
fi
if [ $1 == "A" ]
then
    echo  ----------------- Pulling Agent Status of 150 Agents... -----------------------
    python3 cw/cw-automateAgents.py
fi
if [ $1 == "T" ]
then 
    echo  ----------------- Loading Ticket Information From Today.. -----------------------
    python3 cw/cw-srvcebrd.py
fi
if [ $1 == "TB" ]
then 
    echo  -----------------         Checking Ticket Amounts         ---------------------
    python3 cw/cw-srvcebrd.py
    file=ticket_types.txt
    DC=tickets/DC.p
    EU=tickets/EU.p
    NT=tickets/NT.p
    RT=tickets/RT.p
    if grep -q Reboot "$file"; then
        echo [BrinxBot]: Running reboot ticket type solver with current method...
        echo [BrinxBot]: There are a total of $(grep -ao '[0-9]*' $RT) reboot tickets today.
        python3 cw/cw-reboot.py
    else 
        echo "[BrinxBot]: No reboot type tickets according to ticket_types.txt, continuing to next ticket type..."
    fi 
    if grep -q edgeupdate "$file"; then
        echo [BrinxBot]: Running edgeupdate ticket type solver with current method...
        echo [BrinxBot]: There are a total of $(grep -ao '[0-9]*' $EU) edgeupdate tickets today.
        python3 cw/cw-edgeu.py
    else 
        echo "[BrinxBot]: No edgeupdate type tickets according to ticket_types.txt, continuing to next ticket type..."
    fi 
    if grep -q Cleanup "$file"; then
        echo [BrinxBot]: Running Disk Cleanup ticket type solver with current method...
        echo [BrinxBot]: There are a total of $(grep -ao '[0-9]*' $DC) Disk Cleanup tickets today.
        python3 cw/cw-diskcleanup.py
    else 
        echo "[BrinxBot]: No Disk Cleanup type tickets according to ticket_types.txt, continuing to next ticket type..."
    fi 
    if grep -q NIC "$file"; then
        echo [BrinxBot]: Running NIC Packet Error ticket type solver with current method...
        echo [BrinxBot]: There are a total of $(grep -ao '[0-9]*' $NT) NIC tickets today.
        python3 cw/cw-nic.py
    else 
        echo "[BrinxBot]: No NIC type tickets according to ticket_types.txt,..."
    fi 
    echo "[BrinxBot]: Done."
fi
echo "[BrinxBot]: EOL...Shutting Down..."

