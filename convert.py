f = open("test1.txt",'r')

#print(f.read())
g = open("out.txt",'w')

#with open("test.txt",'w',encoding = 'utf-8') as g:
i=0
j=0
#print(x)
#print(len(x))

#x=" "
#while f.readline():

 
x=str(f.readline())
while x:
    # print(x[0:3])

    if("int" in x):
        for i in range(len(x)):
            if(x[i]=="=" and i+1<len(x)):
                j=i+1
                c=0
                while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                    #print(x[j])
                    if(x[j+1]=="," or x[j+1]==";"):
                        g.write("{}".format(x[j].ljust(4-c," ")))
                        j+=1
                    else:
                        g.write("{}".format(x[j]))
                        j+=1
                        c+=1

    if("float" in x):
        for i in range(len(x)):
            if(x[i]=="=" and i+1<len(x)):
                j=i+1
                d=0
                while(x[j]!=',' and x[j]!=';' and j+1<len(x)):
                    #print(x[j])
                    if(x[j+1]=="," or x[j+1]==";"):
                        #print(x[j].ljust(8," "))
                        g.write("{}".format(x[j].ljust(8-d," ")))
                        j+=1
                    else:
                        g.write("{}".format(x[j]))
                        j+=1
                        d+=1



    g.write("\n")
    x=str(f.readline())
    

f.close()
g.close()
