import os
import sys
import colorama

print(f"""{colorama.Fore.CYAN}
 ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ██▓███   ▄▄▄       ███▄    █ ▄▄▄█████▓ ██░ ██ ▓█████  ██▀███  
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██░  ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██░ ██▓▒▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒██▒ ░  ░ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░▓█▒░██▓░▒████▒░██▓ ▒██▒
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░▒ ░       ▒   ▒▒ ░░ ░░   ░ ▒░    ░     ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░ ░░         ░   ▒      ░   ░ ░   ░       ░  ░░ ░   ░     ░░   ░ 
 ░          ░  ░     ░  ░░ ░      ░  ░                  ░  ░         ░           ░  ░  ░   ░  ░   ░     
      ░                  ░                                                           [CREATOR]                   
                                                                                    {colorama.Fore.GREEN} - Designed by madhan{colorama.Style.RESET_ALL}
                                                                                    {colorama.Fore.GREEN} - https://github.com/madhanmaaz{colorama.Style.RESET_ALL}
                                                                                    {colorama.Fore.GREEN} - https://madhanmaaz.netlify.app{colorama.Style.RESET_ALL}
""")

platform = sys.platform
exe = "python"
allPayloads = {}

if platform != "win32": exe = "python3"

def cHelp():
    print("""
=== MENU ===
> help                  Help menu.
> payloads              List out the payloads.
> goto <payload-id>     To enter in payload
> exit                  App exit.
""")
    

def payloads(show):
    allBackdoorFolders = os.listdir(os.path.join(os.getcwd(), "backdoor"))
    
    if show : print(f"{colorama.Fore.GREEN}\n+=== PAYLOADS ===+")
    if show : print("{:<3}{}".format(f"ID", f"Languages{colorama.Style.RESET_ALL}"))

    for i, folder in enumerate(allBackdoorFolders):
        if show : print("{:<3}{}".format(i, folder))
        allPayloads[i] = folder

payloads(False)   

def goto(id):
    try:
        id = int(id)
        payload = allPayloads[id]
        dirPath = os.path.join(os.getcwd(), 'backdoor', payload, "main.py")
        os.system(f'{exe} -u "{dirPath}"')
    except Exception as e:
        print(f"{colorama.Fore.RED}Error id not found.{colorama.Style.RESET_ALL}")

while True:
    try:
        userInput = input("[CREATE]> ")

        if len(userInput) == 0:
            continue
        elif userInput == "exit":
            exit()
        elif userInput == "help":
            cHelp()
        elif userInput == "payloads":
            payloads(True)
        elif userInput[0:5] == "goto ":
            goto(userInput[5:])
        else:
            print(f"{colorama.Fore.RED}Error command not found.{colorama.Style.RESET_ALL}")
        
    except KeyboardInterrupt:
        exit()
    
    except Exception as e:
        print(e)