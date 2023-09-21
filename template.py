import os
import random
import colorama
import tempfile
import subprocess

appName = "-payload"

payloadInfo = {
    "origin": "",
    "mediaurl": "",
    "medianame": "",
    "interval": "2",
    "filename": ""
}

mainPath = os.path.join(os.getcwd(), "backdoor", appName)
outputPath =  os.path.join(os.getcwd(), "output")

def code():
    payVars = '''
    ORIGIN = "''' + payloadInfo['origin']+'''";
    MEDIAURL = "'''+payloadInfo['mediaurl']+'''";
    MEDIANAME = "'''+payloadInfo['medianame']+'''";
    INTERVAL = '''+payloadInfo['interval']+'''* 1000;
'''
    with open(os.path.join(mainPath, "temp.txt"), "r") as f:
        return payVars + f.read()
    
def options():
    print(f"{colorama.Fore.CYAN}+=== OPTIONS ===+{colorama.Style.RESET_ALL}")
    for i in payloadInfo:
        print("{:<10} : {}".format(i, payloadInfo[i]))

def settingInfo(command):
    try:
        key, value = command.split(" ")
        payloadInfo[key]

        if len(value) > 0:
            payloadInfo[key] = value
        else: print(f"{colorama.Fore.RED}value not found.{colorama.Style.RESET_ALL}")
    except:
        print(f"{colorama.Fore.RED}command error.{colorama.Style.RESET_ALL}")

def create(type):
    programCode = code()

    if not os.path.exists(outputPath): os.mkdir(outputPath)

    # checking values 
    for i in payloadInfo:
        if len(str(payloadInfo[i])) == 0:
            print(f"{colorama.Fore.RED}{i} not found. set the {i}.{colorama.Style.RESET_ALL}")
            return
    
    if type == "-o":
        print(f"{colorama.Fore.GREEN}CREATING PAYLOAD [BINARY]{colorama.Style.RESET_ALL}")
        apps = []

        for a in apps:
            try:
                subprocess.check_call([a, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"{colorama.Fore.GREEN}[+] {a} FOUND.{colorama.Style.RESET_ALL}")
            except:
                print(f"{colorama.Fore.RED}[-] ERROR: {a} NOT FOUND.{colorama.Style.RESET_ALL}")
                return False
            
        print("PROCESS creating.....")
        tempPath = os.path.join(tempfile.gettempdir(), f"black-panther-temp-{str(random.randint(1000, 10000))}")
        
        
        print(f"EXE binary file coverted. PATH: {outputPath}")

    elif type == "-c":
        print(f"{colorama.Fore.GREEN}CREATING PAYLOAD [CODE]{colorama.Style.RESET_ALL}")
        filePath = os.path.join(outputPath, "")
        with open(filePath, "w") as f:
            f.write(programCode)
        
        print(f"CODE IN: {outputPath}")

def cHelp():
    print("""
+=== MENU ===+
> help               Help menu.
> options            Show the required options for the payload.
> set <KEY> <VALUE>  Setting value for the payload. 
> create -o          Create a compiled version.
> create -c          Create program source code. 
> back               Exit from current payload.
""")

print(f"{colorama.Fore.CYAN}+=== {appName.upper()} PAYLOAD ===+{colorama.Style.RESET_ALL}")
while True:
    try:
        userInput = input(f"[CREATE/{appName}]> ")

        if len(userInput) == 0:
            continue
        elif userInput == "help":
            cHelp()
        elif userInput == "back":
            break
        elif userInput == "options":
            options()
        elif userInput[0:4] == "set ":
            settingInfo(userInput[4:])
        elif userInput[0:7] == "create ":
            create(userInput[7:].strip())
        else:
            print(f"{colorama.Fore.RED}ERROR command not found.{colorama.Style.RESET_ALL}")

    except KeyboardInterrupt:
        exit()