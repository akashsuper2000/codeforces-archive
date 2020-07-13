def fun(a,b,c):
    return abs(a-b)+abs(b-c)+abs(c-a)

for i in range(int(input())):
    a,b,c = [int(j) for j in input().split()]
    p = [-1,0,1]
    m = fun(a,b,c)
    for j in range(3):
        for k in range(3):
            for l in range(3):            
                m = min(m,fun(a+p[j],b+p[k],c+p[l]))
    print(m)
