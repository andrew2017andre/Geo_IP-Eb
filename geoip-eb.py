import time
import requests
import os,sys
from termcolor import colored
os.system('clear')
time.sleep(1)

print(colored("""

               WELCOME TO BANgLADESH
                    BANgLADESH
                       V1.0 \n """, """green"""))

print(colored("=================GEO IP LOCATIONS=================  ", "red"))



inp=input(colored("Target IP: ", "green"))
def Geo_IP():
	if inp.startswith('http://'):
		print(colored("                 Sorry, You cannot use 'http://' ", "cyan"))
		time.sleep(1)
		print(colored("         Shutting down...", "red"))
		time.sleep(4)
		sys.exit()
	if inp.startswith("https://"):
		sys.exit("Sorry, You cannot use 'https://' ")
	try:
		get=requests.get(f"https://api.hackertarget.com/geoip/?q={inp}")
		print(get.text)
	except Exception:
		print(colored(f" °.° The address you entered '{inp}' is not Connectable ! \n Or check your Internet Connections, \nThank you.", "red"))

	save=input(colored("     Save info ? Y/n: ", "yellow"))
	if save=="y":
		file=open(f"./geo-{inp}.txt", "w")
		print(file.write(str(get.text)))
		print(colored(f"Informations saved from '{inp}' Check geo-{inp}.txt !", "green"))
	if save=="Y":
		file=open(f"./geo-{inp}.txt", "w")
		print(file.write(str(get.text)))
		print(colored(f"Informations saved from '{inp}' Check geo-{inp}.txt !", "green"))
	elif save=="n":
		sys.exit("Done!")
	elif save=="N":
		sys.exit("Done!")
	else:
		sys.exit()


Geo_IP()
