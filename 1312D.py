def modi(a, m) :
    p = 1
    while (a > 1) :
        p*=a
        p = p%m
        a-=1
    return p 

mod = 998244353
n,m = [int(i) for i in input().split()]
q = ((modi(n-1,mod)*modi(m-n+1,mod))%mod)
q = ((modi(m,mod)+mod)/q)%mod
print(q)
