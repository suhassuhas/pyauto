#########################################################################################
# This is the program to write hex values from a text file to flash development toolkit #
# Conditons to be followed before using this Program                                    #
# position of fdk application in taskbar must be seventh from leftClick                 # 
# Dont change the width of editor window                                                #
#########################################################################################

from pyautogui import *
import sys

num_seconds = 3
leftClick(x=397, y=998)

##confirmation =confirm(text='Are you sure to continue?', title='Confirmation', buttons=['OK', 'Cancel'])
##
##if(not confirmation):
##    exit()

leftClick(x=545,y=387)
doubleClick(x=232,y=402)  # move mouse to XY coordinates over num_second seconds
typewrite("100000")
press("enter")


f = open("test1.txt",'r')


i=0
j=0
next_addrs=1
addrs = {1:"100050",2:"102000",3:"104000",4:"106000",5:"107000"}

def int_2_hex(number, bits=32):
    """ Return the 2'complement hexadecimal representation of a number """

    if number < 0:
        x=hex((1 << bits) + number)
        return x[2:].rjust(8,"0")
    else:
        x=hex(number)
        return x[2:].rjust(8,"0")


def char_2_hex(n,bits=8):
    
    if(type(n)== str):
        x=hex(ord(n))
        print(x[2:].rjust(2,"0"))
        return x[2:].rjust(2,"0")
    if(type(n)==int):
        if n < 0:
            x=hex((1 << bits) + n)
            return x[2:].rjust(2,"0")
        else:
            x=hex(n)
            return x[2:].rjust(2,"0")



if __name__ == "__main__":
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
                        if(x[j]!='{'):
                            while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                                #print(x[j])
                                q+=x[j]
                                j+=1
                            d=(int_2_hex(int(q)))    
                            #print(d)
                            typewrite(d)
                            q=""
                        else:
                            j+=1
                            while(x[j]!='}'and x[j]!=';'):
                                while(x[j]!=',' and x[j]!='}'):
                                    q+=x[j]
                                    j+=1
                                d=(int_2_hex(int(q)))    
                                #print(d)
                                typewrite(d)
                                q=""
                                j+=1
                                print(j)


            if("char" in x):
                for i in range(len(x)):
                    if(x[i]=="=" and i+1<len(x)):
                        j=i+1
                        if(x[j]=="'"):
                            while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                                #print(x[j])
                                q+=x[j]
                                j+=1
                            print(q)
                            d=(char_2_hex(q[1]))    
                            print(d)
                            typewrite(d)
                            q=""

                        elif(x[j]=='"'):
                            j+=1
                            while(x[j]!='"'):
                                d=(char_2_hex(x[j]))    
                                j+=1
                                print(d)
                                typewrite(d)
                                q=""

                        else:
                            while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                                #print(x[j])
                                q+=x[j]
                                j+=1
                            print(q)
                            d=(char_2_hex(int(q)))    
                            print(d)
                            typewrite(d)
                            q=""





        else:
            if next_addrs<6:
                    doubleClick(x=232,y=402)  # move mouse to XY coordinates over num_second seconds
                    typewrite(addrs[next_addrs])
                    press("enter")
                    next_addrs+=1
                    #print(next_addrs)


        x=str(f.readline())


    f.close()
    alert(text="Task Completed.",title="ALERT!!!",button="OK")
