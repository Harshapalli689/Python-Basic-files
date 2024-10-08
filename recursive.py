def sume(n):
    s=0
    if n>0:
        s+=n
        print(s)
        sume(n-1)
        print(s)
    return s
n=int(input())
print(sume(n))
