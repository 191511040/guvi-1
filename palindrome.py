n=int(input())
e=n
f=0
while(n>0):
    dig=n%10
    f=f*10+dig
    n=n//10
if(e==f):
    print "yes"
else:
    print "no"