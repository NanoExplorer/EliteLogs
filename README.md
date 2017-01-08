# EliteLogs
Reads elite dangerous commander's log to the console in real time.
To use this, you must install Python 3. I usually run it by opening windows powershell and using `python cmdrlog.py`. **To be able to run python files in PowerShell watch out while installing python for an option to "Add Python to your PATH" and make sure it is selected**.

You can also run it using IDLE, which is bundled with python. To do that, simply use file -> open from IDLE to open `cmdrlog.py` then run it using F5.

When you launch the program it will ask you for the name of your windows user folder. You can find this by opening a file browser and going to `Local Disk (C:)` and then to the `Users` folder. You need the name you see there that corresponds to your user.

Once you start this program it will begin watching the commander's log and printing its contents to the screen in real time. Some events, such as jumps, have a description added by me, and others simply print the raw JSON to the screen.

Fly safe!

Note: This script has logic for calculating jump range. It is currently tailored to only work on the Asp Explorer, and only mine. If you'd like me to make this feature more robust, let me know.
