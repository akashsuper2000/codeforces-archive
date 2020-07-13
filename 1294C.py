from math import ceil,sqrt
def kFactors(n, k=3): 
    a = []
    for i in range(2, ceil(sqrt(n))): 
        if(n%i==0):
            n = n / i
            a.append(i) 
    if n > 2: 
        a.append(n)
    a = list(set(a))
    if len(a) < k: 
        return [-1]
    return [a[0],a[1]]

for i in range(int(input())):
    n = int(input())
    a = kFactors(n)
    if(a[0]==-1):
        print('NO')
    else:
        print('YES')
        print(int(a[0]),int(a[1]),int(n//(a[0]*a[1])))
