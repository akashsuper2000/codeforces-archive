from math import ceil
n,a,b,k = [int(i) for i in input().split()]
ar = [int(i) for i in input().split()]
d = [0 for i in range(b)]
if(a==1 and b==1):
    r = 0
    for i in range(n):
        if(ar[i]%2==0):
            r+=1
        else:
            d[0]+=1
    d[0]+=min(k,r)
else:
    for i in range(n):
        c = ar[i]%(a+b)
        if(c<=a and c>0):
            d[0]+=1
        elif(c==0):
            d[ceil(b/a)]+=1
        else:
            d[ceil((c-a)/a)]+=1
    i = 1
    while(len(d)>i):
        if(k>=d[i]*i):
            k-=d[i]*i
            d[0]+=d[i]
            i+=1
        else:
            d[0]+=k//i
            break
print(d[0])
    
