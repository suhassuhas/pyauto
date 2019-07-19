from pyautogui import *


input_file = open("rty.txt",'r')
parentheses = []
top = -1

q=""
def char2hex(n,bits=8):
    if(type(n)==int):
        if n < 0:
            x=hex((1 << bits) + n)
            return x[2:].rjust(2,"0")
        else:
            x=hex(n)
            return x[2:].rjust(2,"0")


i=0
j=0
line = str(input_file.read())
l=0
##while(line[l]!='/'):
##    print(line[l])
##    l+=1
    
if(line[0]!='\n'):
    
    while(i<len(line)):
        if(line[i]=='/'):
            print("Hurar")
        #print(line[i],end="")
        
            
        while(i<len(line) and line[i]!=',' and line[i]!='/'):
            if(line[i]!='{' and line[i]!='}' and (ord(line[i])>47 and ord(line[i])<58)):
                q+=line[i]
            
            i+=1
        try:
            #print(line[i])
            h = char2hex(int(q))
            print(q)
            q=""
            #print(h)
        except:
            #print("jnuj")
            pass
            q=""

        #print(i)
        
        i+=1



    
        
        
      

        
        
