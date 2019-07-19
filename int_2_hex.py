n=int(input("Enter number of integers"))
f=open("out.txt",'w')

def int_2_hex(n):
    x=hex(n)
    return x[2:].rjust(8,"0")

for i in range(n):
    x=int(input())
    s=int_2_hex(x)
    y=''.join(str(ord(c)) for c in s)
    f.write(y)


f.close()



