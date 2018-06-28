#deepu assistant
a=input("whats your name\n")
print("Hi awesome %s"%a)
c=['Hi!!','Hello!!!','welcome to ur assisitant','nice to see ']
#command
import os

def mycmd():
    
    command=input("Enter app name to open:\n")
    if(command=="notepad"):
        os.system('notepad.exe')
        mycmd()
        os.system('echo off')
    elif(command=="paint"):
        os.system('mspaint.exe')
        mycmd()
    elif(command=="file") or (command=="explorer") :
        os.system('explorer.exe')
        mycmd()
    elif(command=="date"):
        os.system('date.exe')
        mycmd()
    else:
        chat()

        
            



def calc():
    x=input("Enter equation:\n")
    plus=x.find('+')
    minus=x.find('-')
    mul=x.find('*')
    div=x.find('/')
    length=len(x)
    if plus>=0:
        a=x[0:plus]
        b=x[plus:length]
        print(int(a)+int(b))
        calc()
    elif mul>=0:
        a=x[0:plus]
        b=x[plus:length]
        print(int(a)*int(b))
        calc()

    elif div>=0:
        a=x[0:plus]
        b=x[plus:length]
        print(int(a)/int(b))
        calc()
    elif minus>=0:
        a=x[0:plus]
        b=x[plus:length]
        
        print(int(a)-int(b))
        calc()
    else:
        chat()



def chat():
    for i in range(100):
    
        b=input("")
        if (b=='hi')or (b=='hii')or (b=='hello'):
            print("Hi !!!!")
        elif (b=='good morning'):
            print("Have a very good morning dear")
        
        elif (b=='bye'):
            print("bye see you")
        elif (b=='calc'):
            #print("Have a very good morning dear")
            calc()
        elif (b=='i luv u') or (b=='I love you') or (b=='i love you')or (b=='i love u'):
            print("i like  u too,,,  But hey remember Imm datinvg with saurabh,\n my first and last love ")
        elif (b=='command') or (b=='cmd') or (b=='app') :
            mycmd()
chat()
