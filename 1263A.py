for i in range(int(input())):
    a,b,c = sorted([int(j) for j in input().split()])
    s=min(c-b,a)
    c,a = c-s,a-s
    if(a==0):
        s+=min(c,b)
    else:
        s+=(a//2)*2
        s+=min(b,c)-a//2
    print(s)
    
