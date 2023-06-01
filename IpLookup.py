#By Vynix
import requests
import sys
import os
import random
from pystyle import *
import random
import requests
import time
import json
from urllib.request import urlopen

os.system("title IPLOOKUP ::: Made By Vynix")

os.system("cls")




banner = '''
██╗██████╗ ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██║██╔══██╗██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║██████╔╝██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║██╔═══╝ ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║██║     ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     

                    
       ╔══════════════════════════════════════════════╗
       ║                  IP LOOKUP                   ║
       ║              Developed By Vynix              ║
       ║                                              ║
       ╚══════════════════════════════════════════════╝               
'''


print(Colorate.Horizontal(Colors.green_to_red, Center.XCenter(banner)))
Write.Print("[+] Made By Vynix : https://github.com/Vynix7", Colors.blue_to_green, interval=0.04,)
print("")
ip = input("IP ADRESS : ")

url = "http://ip-api.com/json/" + ip
values = json.load(urlopen(url))

Write.Print("[+] Trying to find information", Colors.blue_to_green, interval=0.04,)
time.sleep(1)
print("")
print("..................................................")
print("[*] Ip Address - ", values['query'])
print("[*] Country - ", values['country'])
print("[*] City - ", values['city'])
print("[*] ISP - ", values['isp'])
print("[*] Region - ", values['regionName'])
print("[*] Timezone - ", values['timezone'])
print("[*] Zip - ", values['zip'])
print("[*] Latidude - ", values['lat'])
print("[*] Longitude - ", values['lon'])
print("[*] AS - ", values['as'])
Write.Print("[*] THANK FOR USING MY TOOL <3", Colors.dark_green, interval=0.04,)

os.system("pause >nul")
