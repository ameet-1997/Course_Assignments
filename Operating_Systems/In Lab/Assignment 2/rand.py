import random
import sys
k=sys.argv[1]
m=random.randint(1,500)
n=random.randint(1,500)
p=random.randint(1,500)
sys.stdout.write(str(k)+'\n'+str(m)+" "+str(n)+" "+str(p)+"\n")
for i in range(0,m):
    for j in range(0,n):
        sys.stdout.write(str(random.randint(0,1000))+"\n")
for i in range(0,n):
    for j in range(0,p):
        sys.stdout.write(str(random.randint(0,1000))+"\n")
