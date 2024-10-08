def fun(n):
    s=""
    for i in n:
        s=s+i
        a=s[::-1]
        if(a==s and len(a)>1):
            print(s)
n=input()
l=[]
for i in range(len(n)):
    l.append(n[i:])
for j in l:
    fun(j)
    
