from math import ceil,gcd
for i in range(int(input())):
    r,b,k = [int(j) for j in input().split()]
    if(r<b):
        r,b = b,r
    if(ceil(r/b)-1>=k or ceil((r//gcd(r,b))/b)>=k):
        print('REBEL')
    else:
        print('OBEY')
