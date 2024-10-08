def palind(k):
    if k==k[::-1] and len(k)>1:
        print(k)
        return True


s=input()
for i in range(1,len(s)-1):
    k=s[:i]
    if palind(k):
        for j in range(i,len(s)+1):
            s2=s[i:j]
            palind(s2)
            s3=s[j:]
            palind(s3)
