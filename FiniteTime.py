#Written by Luke Chen Shui
#FINITE TIME!
import os
import time
import platform
import sys
import ctypes
import psutil
def shutdownOrReboot(mode):

	if(mode == "s"):
		if(platform.system() == 'Linux'):
			os.system("sudo shutdown -h -P now")
		elif(platform.system() == 'Windows'):
			os.system("shutdown /s")
	elif(mode == "r"):
		if(platform.system() == 'Linux'):
			os.system("sudo shutdown -h -r now")
		elif(platform.system() == 'Windows'):
			os.system("shutdown /r")
	
def printCPUValues():
	for proc in psutil.process_iter():
		print proc

def searchProcess(name):
	found = False
	idNum = 0
	for proc in psutil.process_iter():
		try:
			if (proc.name() == name):
				found = True
				idNum = proc.pid
		except:
       			print "Permission error or access denied on process"
			sys.exit(0)
	return found, idNum
	
#This function checks to see if the character is a number, or a letter
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
	#return false if it's a letter

#checks to see if the user has admin/root priviledges
#If not, the user must restart the script with sudo or Run As Administrator...
try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0


#If the user is an administrator, let the program execute
if(is_admin):


	print "Welcome to Finite Time!"
	print ""
	print "-----------------------"
	print ""
	print "This program works in two ways."
	print "1. Shutdown/restart the computer after a certain amount of time."
	print "2. Shutdown/restart the computer when the CPU usage of a process"
	print "goes above or below a certain threshold."
	
	mode = 0
	while (mode != 1 and mode != 2):
		print "Please enter 1 or 2 to indicate which mode you've chosen."
		mode = int(raw_input())

	if (mode == 1):
		countDownTime = 0
		
		#The mode tells the program whether or not the user wants to restart
		#or shutdown the computer

		mode = ""
		#Error-checking loop
		while (mode != "r" and mode != "s"):
			print "Enter the mode. 's' for shutdown or 'r' for restart."
			mode = raw_input()
			if  (mode != "r" and mode != "s"):
				print "Invalid mode entered"
		#Kinda hard to do an error-checking loop for this one, so whatever....
		print "Please enter desired amount of time."
		print "Examples:\n 1m for 1 minute,\n 2h for two hours,\n 5s for five seconds."
		enteredTime = raw_input()

		containsNumbers = False
		amountOfLetters = 0

		#iterates throughout the command for error-checking
		for character in enteredTime:
			if is_number(character) == False:
				amountOfLetters+=1
			else:
				containsNumbers = True;

		#The command must only contain one letter, e.g. 5s, which says you want to execute the mode in 5 seconds
		if amountOfLetters > 1:
			print "Invalid command entered: Command cannot contain more than one letter"
		#The command must contain at least one number, or else what would be the point lolz?

		elif containsNumbers == False:
			print "Your command must contain numbers."
		#The last letter of the command must be the time unit specifier, e.g. h for hours, seconds for seconds, minutes for minutes
		elif  enteredTime[len(enteredTime)-1] != "h" and enteredTime[len(enteredTime)-1] != "m" and  enteredTime[len(enteredTime)-1] != "s":
			print "The last character in the command must be either 's', 'm' or 'h' to indicate the unit of time to use."
		else:

			lastLetter = enteredTime[len(enteredTime)-1]
			enteredTime = enteredTime[:-1]

			countDownTime = int(enteredTime)
			#converts the string to a number, which is then decremented once per second


			#Does time unit conversions...
			if lastLetter == "m":
				countDownTime = countDownTime * 60
			elif lastLetter == "h":
				countDownTime = countDownTime * 60 * 60

			while(countDownTime > 0):
				#This is the decrementing loop
				print "Time Remaining:", countDownTime," seconds/ ", countDownTime/60, " minutes/ ","%.4f" % float(float(countDownTime)/(60*60)), " hours","\r",
				sys.stdout.flush()	
				time.sleep(1)
				countDownTime-=1
			print ""
			print "Time is done!"

			#When time is done, the script will execute the shutdown or restart commands based on whether or not the
			#user is on Linux or Windows
			shutdownOrReboot(mode)

	elif (mode == 2):
		status = False
		id = 0
		printCPUValues()
		process = "asasdasda"
		while (status == False):
			print "Please enter the name of the process you want to monitor."
			process = raw_input()
			status, id = searchProcess(process)
 
		threshold = -50
		while (threshold < 0 or threshold > 100):
			print "Please enter the numeric threshold for the CPU usage."
			threshold = int(raw_input())

		mode = ""
		#Error-checking loop
		while (mode != "r" and mode != "s"):
			print "Enter the mode. 's' for shutdown or 'r' for restart."
			mode = raw_input()
			if  (mode != "r" and mode != "s"):
				print "Invalid mode entered"

		comparison = " "
		while (comparison  != "<" and comparison != ">"):
			print "Enter '>' if you want to shutdown/restart if the CPU usage is greater than the threshold."
			print "Enter '<' if you want to shutdown/restart if the CPU usage is lower than the threshold."
			comparison = raw_input()
		if (comparison == ">"):

			while(psutil.Process(id).get_cpu_percent(interval = 0.1) <= threshold):

 						
				print "Name :%s CPU Usage: %f" % (psutil.Process(id).name,psutil.Process(id).get_cpu_percent(interval = 0.1))
		elif(comparison == "<"):
			while(psutil.Process(id).get_cpu_percent(interval = 0.1) >= threshold):

				print "Name :%s CPU Usage: %f" % (psutil.Process(id).name,psutil.Process(id).get_cpu_percent(interval = 0.1))
		
		shutdownOrReboot(mode)			
else:
	print "You need to be root or an Administrator to run this."
	print "Try using sudo or Run As Administrator..."
