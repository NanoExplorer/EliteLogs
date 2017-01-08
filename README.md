# EliteLogs
Reads elite dangerous commander's log to the console in real time
To use this, you must install Python 3. I usually run it by opening windows powershell and using `python cmdrlog.py`.
Before you begin, you must make sure the path_to_watch variable (currently on line 26) points to the directory your journal is in.

Once you start this program it will begin watching the commander's log and printing its contents to the screen in real time. Some events, such as jumps, have a description added by me, and others simply print the raw JSON to the screen.

Fly safe!

Note: This script has logic for calculating jump range. It is currently tailored to only work on the Asp Explorer, and only mine. If you'd like me to make this feature more robust, let me know.
