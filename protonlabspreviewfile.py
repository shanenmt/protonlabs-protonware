import sys
import os
import time
import webbrowser
import wmi

ProtonLabsNetworkPlaceholder = False



osusername = os.getlogin()

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

def typeWriter(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

typeWriter("Connecting to Proton Labs Network")
time.sleep(1)
typeWriter('.')
time.sleep(1)
typeWriter('.')
time.sleep(1)
typeWriter('.\n')
typeWriter('ProtonWare v0.3 Version Alpha last updated 9:14 PM EST 10/1/2022\n')
time.sleep(3)
ProtonLabsNetworkPlaceholder = True
os.system('cls')

typeWriter('By Proton Labs\n')
typeWriter('')
typeWriter("this is v0.3 Version Alpha  of ProtonWare.py\n")

os.system('cls')


typeWriter(f"welcome to ProtonWare, {osusername}.\n")
time.sleep(1)
print(" ")
typeWriter("where would you like to go?\n")
time.sleep(1)
typeWriter("""
1 - Not A Rickroll
2 - Coming Soon
3 - Coming Soon
4 - Quit\n
        """)
time.sleep(1)

protonhub1 = input()

if protonhub1 == '1':
    os.system('cls')
    print(" ")
    typeWriter("LOL it is a rick roll but now it's too late for you to stop it\n")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1)
    time.sleep(1)
    os.system('cls')

if protonhub1 == '2':
    os.system('cls')
    typeWriter("This is coming soon!\n")
    time.sleep(1)
    os.system('cls')

if protonhub1 == '3':
    os.system('cls')
    typeWriter("This is coming soon!\n")
    time.sleep(1)
    os.system('cls')

if protonhub1 == '4':
    os.system('cls')
    typeWriter('closing')
    time.sleep(1)
    typeWriter('.')
    time.sleep(1)
    typeWriter('.')
    time.sleep(1)
    typeWriter('.')
    time.sleep(1)
    exit(0)
