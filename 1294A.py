for i in range(int(input())):
    a,b,c,n = [int(j) for j in input().split()]
    a,b,c = sorted([a,b,c])
    if((c-a + c-b)<=n) and ((n-(c-a + c-b))%3==0):
        print('YES')
    else:
        print('NO')
