#!/bin/bash
clear
echo "CW-Automation [BrinxBot] v6.1, Created by Nels2. 2022"
echo ""
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
echo ""
echo "[BrinxBot]: Hello, $USER. I am BrinxBot and I will solve your ticketing issues!"
if [ $1 == "T" ]
then 
    echo "[BrinxBot]: $USER! you can view tickets and autocomplete with 'TB' instead of 'T'!"
else
    echo "[BrinxBot]: $USER! I will complete the task!"
fi 

if [ $1 == "1" ]
then 
    vartype=Back_up_Missed
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running ticket type solver with current method..."
    python3 cw/cw_oncore.py
fi
if [ $1 == "2" ]
then 
    vartype=GPKT
    echo [BrinxBot]: OK $USER! I Will complete the following ticket type: $vartype
    echo "[BrinxBot]: Running ticket type solver with current method..."
    python3 cw/cw_gpkt.py
fi
if [ $1 == "H" ]
then 
    clear
    echo  "-------------| BrinxBot, a small script to help with automation.
|------------| Ticket Types Information |----------------------------------
|
|--> OP1 is Backup Missed Ticket type ...         ./start.sh 1  
|--> OP2 is Get Product Keys Failed type ...      ./start.sh 2 
|------------|  Additional Information  |----------------------------------
|
|--> T is to pull the Service Board ticket list to the Terminal ...
|--> Above are the following arguments you can use with start.sh.
|--> After the above, is the correct way to pass an argument to start.sh
|
|--------------------------------------------------------------------------"
fi
if [ $1 == "T" ]
then 
    echo "[BrinxBot]: Loading Ticket Information From Today .."
    python3 cw/cw_srvcebrd.py
fi

if [ $1 == "TB" ]
then 
    echo "[BrinxBot]: This option doesn't exist yet!"
fi
echo "[BrinxBot]: End of script...Shutting Down..."