for i in range(int(input())):
    a,b = [int(j) for j in input().split()]
    if(a%b==0):
        print('YES')
    else:
        print('NO')
