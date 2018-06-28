#command
import os
def mycmd():
    
    command=input("Enter app name to open")
    if(command=="notepad"):
        os.system('notepad.exe')
        mycmd()
        os.system('echo off')
    elif(command=="paint"):
        os.system('mspaint.exe')
        mycmd()
    elif(command=="file"):
        os.system('explorer.exe')
        mycmd()
    elif(command=="date"):
        os.system('date.exe')
        mycmd()

        
            


