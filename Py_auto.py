from pyautogui import *
import sys

num_seconds = 3
leftClick(x=397, y=998)
doubleClick(x=263,y=402)  # move mouse to XY coordinates over num_second seconds
typewrite("100000")
press("enter")


f = open("test1.txt",'r')


i=0
j=0
next_addrs=1
addrs = {1:"100050",2:"102000",3:"104000",4:"106000",5:"107000"}

def int_2_hex(n):
    x=hex(n)
    return x[2:].rjust(8,"0")

def char_2_hex(n):
    x=hex(ord(n))
    print(x[2:].rjust(2,"0"))
    return x[2:].rjust(2,"0")

q=""
x=str(f.readline())
while x:
    #print(x[0:3])
    #print(x[0])
    if(x[0]!="\n"):
        if("int" in x):
            for i in range(len(x)):
                if(x[i]=="=" and i+1<len(x)):
                    j=i+1
                    while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                        #print(x[j])
                        q+=x[j]
                        j+=1
                    d=(int_2_hex(int(q)))    
                    #print(d)
                    typewrite(d)
                    q=""



        if("char" in x):
            for i in range(len(x)):
                if(x[i]=="=" and i+1<len(x)):
                    j=i+1
                    while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                        #print(x[j])
                        q+=x[j]
                        j+=1
                    print(q)
                    d=(char_2_hex(q[1]))    
                    print(d)
                    typewrite(d)
                    q=""           
            
    else:
        if next_addrs<6:
                doubleClick(x=263,y=402)  # move mouse to XY coordinates over num_second seconds
                typewrite(addrs[next_addrs])
                press("enter")
                next_addrs+=1
                #print(next_addrs)

    
    x=str(f.readline())
    

f.close()
alert(text="Task Completed.",title="ALERT!!!",button="OK")
