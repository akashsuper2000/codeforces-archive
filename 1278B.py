from math import ceil
for i in range(int(input())):
    a,b = [int(j) for j in input().split()]
    c=abs(a-b)
    d = ceil(pow(c,0.5))
    if((d*(d+1))/2>c):
        print(d+1)
    else:
        print(d)
