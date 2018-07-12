#deepu assistant
a=input("whats your name\n")
print("Hi awesome %s"%a)
c=['Hi!!','Hello!!!','welcome to ur assisitant','nice to see ']
#command
import os
import webbrowser
import bs4
import requests
import random
def lyricservice(lstring):
    #lstring='Perfect ed sheeran'
    res=requests.get('https://search.azlyrics.com/search.php?q=%s'%lstring)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    result=soup.find_all('td',{"class":"text-left"})
    i=1

    x=['0']*10

    for link in result [0:5]:
        print(link.text)
        x[i]=link.find('a').get('href')
    
        i=i+1
    linkss=int(input("Enter song number ........"))
    linksss=x[linkss]
    lres=requests.get(linksss)
    lsoup=bs4.BeautifulSoup(lres.text,'lxml')

    lresult=lsoup.find_all('div',{'class':'col-xs-12'})
    check='<!-- MxM banner -->'
    for lyric in lresult [1:2]:
        lyricss=lyric.text
    print("********************Saurabh Lyrical service***********")
    lindex=lyricss.find('Android')
    print(lyricss[10:lindex])
    print("********************Saurabh Lyrical service***********")

def movie():
    
    search=input("Search movie name.....")
    if(search=='chat'):
        chat()
    else:
        res=requests.get('https://www.imdb.com/find?q='+search+'&s=tt&ref_=fn_al_tt_mr')
        soup=bs4.BeautifulSoup(res.text,'lxml')

        n=0
        x=['0']*10
        result=soup.select('.result_text')
        for i in result [0:5]:
    
            print(i.getText())
            x[n]="http://www.imdb.com/"+i.find('a').get('href')
            n=n+1

        click=int(input("Enter which from 0 to 5:"))
        movieurl=requests.get(x[click])
        ms=bs4.BeautifulSoup(movieurl.text,'lxml')
        title=ms.select('.title_wrapper')
        summary=ms.select('.plot_summary')
		
        print(title[0].getText())
        print(summary[0].getText())
        movie()



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

def search():
    searchin=input("Enter search entry\n")
    if (searchin=='chat'):
        chat()
    else:
        webbrowser.open_new("http://google.co.in/search?q=%s"%searchin)
        search()        



def calc():
    x=input("Enter equation:\n")
    plus=x.find('+')
    minus=x.find('-')
    mul=x.find('*')
    div=x.find('/')
    mod=x.find('%')
    
    length=len(x)
    if plus>=0:
        a=x[0:plus]
        b=x[plus:length]
        print(int(a)+int(b))
        calc()
    elif mul>=0:
        a=x[0:mul]
        b=x[mul+1:length]
        print(int(a)*int(b))
        calc()

    elif div>=0:
        a=x[0:div]
        b=x[div+1:length]
        print(int(a)//int(b))
        calc()
    elif minus>=0:
        a=x[0:minus]
        b=x[minus+1:length]
        
        print(int(a)-int(b))
        calc()
    
    elif mod>=0:
        a=x[0:mod]
        b=x[mod+1:length]
        
        print(int(a)%int(b))
        calc()
    else:
        chat()
ilist1=['hi','hello','hii','listen']
olist1=['hiiii','hello wassup !','nice to meet u!!','Hi how can i help u']
ilist2=['good morning','morning','gm']
olist2=['Have a very good morning','Morning ! what can i do for u ! ']
ilist3=['bye','good bye','see you']
olist3=['Bye','Bye,see you !!']
ilist4=['i luv u','luv u','i love you','i love u','love u']
olist4=['i like  u too,,,  But hey remember Imm datinvg with saurabh,\n my first and last love ','Thank you !!!!']
def chat():
    for i in range(100):
    
        
		b=input("")
        le=len(b)
        if (b[0:5]=='lyric'):
            lyricservice(b[6:le])
                       
        elif b.lower() in ilist1:
            print(random.choice(olist1))
        elif b.lower() in ilist3:
            print(random.choice(olist3))
        elif b.lower() in ilist2:
            print(random.choice(olist2))
        elif b.lower()
        in ilist4:
            print(random.choice(olist4))
        elif (b=='calc'):
            #print("Have a very good morning dear")
            calc()
        elif (b=='command') or (b=='cmd') or (b=='app') :
            mycmd()
        elif (b=='search'):
            search()
        elif (b=='movie'):
            movie()
chat()
