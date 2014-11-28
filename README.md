FiniteTime
==

Uses
--

1. When downloading large files at night, you can just tell FiniteTime to shutdown your computer in, for example, 3 hours.

2. You can use it to prank your siblings! There is a prank version that, if you can configure it to run automatically on your victim's computer with admin rights, will shutdown the victim's computer after one minute of it opening. I didn't want to make it *too* dangerous so I made it wait one minute before executing the shutdown command.

3. You can use it when you're rendering videos late at night and want to go to bed but don't want to leave your computer on all night. Just set it to about 30 minutes after that video editor's ETA and go to sleep :)

Usage (Executable Binaries)
--
1. If you're running on Windows, navigate to the WindowsExecutable folder and right-click on FiniteTime.exe and select "Run As Administrator"
2. If you're running on Linux, open a terminal and cd to the LinuxExecutable directory. Then type in :
sudo ./FiniteTime
3. Choose the desired mode. Enter 'r' to restart the computer or 's' to shut it down.

4. Then enter the amount of time, for e.g. 5s for five seconds, 5m for five minutes, or 5h for five hours.

5. The script will shutdown the computer once the time has elapsed 


Usage (Python Script)
--
1. Open a Linux terminal or open a command prompt using Run As Administrator.

2. Download and extract FiniteTime.py to your user's home directory (on Linux) or your user directory on Windows

3. In your terminal or command prompt, type in:
python FiniteTime.py

4. Choose the desired mode. Enter 'r' to restart the computer or 's' to shut it down.

5. Then enter the amount of time, for e.g. 5s for five seconds, 5m for five minutes, or 5h for five hours.

6. The script will shutdown the computer once the time has elapsed 
