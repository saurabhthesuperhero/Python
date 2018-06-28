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
elif mul>=0:
    a=x[0:plus]
    b=x[plus:length]
    print(int(a)*int(b))
elif div>=0:
    a=x[0:plus]
    b=x[plus:length]
    print(int(a)/int(b))
elif minus>=0:
    a=x[0:plus]
    b=x[plus:length]
    print(int(a)-int(b))
