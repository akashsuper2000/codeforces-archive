from math import log
for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    d = set()
    f = 0
    for j in range(n):
        while(a[j]!=0):
            p = int(round((log(a[j],k)),5))
            if(p in d):
                print('NO')
                f = 1
                break
            d.add(p)
            a[j]-=pow(k,p)
        if(f==1):
            break
    else:
        print('YES')
            
