# EliteLogs
Reads elite dangerous commander's log to the console in real time.
To use this, you must install Python 3. I usually run it by opening windows powershell and using `python cmdrlog.py`. **To be able to run python files in PowerShell watch out while installing python for an option to "Add Python to your PATH" and make sure it is selected**.

You can also run it using IDLE, which is bundled with python. To do that, simply use file -> open from IDLE to open `cmdrlog.py` then run it using F5.

When you launch the program it will ask you for the name of your windows user folder. You can find this by opening a file browser and going to `Local Disk (C:)` and then to the `Users` folder. You need the name you see there that corresponds to your user. You can also manually type in the folder locations by typing `1` instead.

Once you start this program it will begin watching the commander's log and printing its contents to the screen in real time. Some events, such as jumps, have a description added by me, and others simply print the raw JSON to the screen.

At any time, you can use the built in commands. Type `help` to list them! I'll also produce the manual here:
Available commands are:
ship

*Asks for and sets information about your ship, used for calculating jump range.
    
cargo [number]

*Sets the amount of cargo tonnage you are currently hauling.
    
origin [system name]

*Sets the system to display distances relative to. i.e. after `origin Merope` on FSD jump
     it might say "you've arrived in the Pleiades xy-z 3834 system and are 32 light years from Merope".
     
help

*Lists available commands (prints this message)
    
exit

*Quits the program

Fly safe!
