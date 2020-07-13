for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    e,o = 0,0
    for j in a:
        if(j%2==0):
            e = 1
        else:
            o = 1
    if(sum(a)%2!=0 or (e==1 and o==1)):
        print('YES')
    else:
        print('NO')
