for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(n):
        a.append([int(k) for k in input().split()])
    a.sort()
    curx,cury = 0,0
    s = ''
    for j in a:
        if(j[0]<curx or j[1]<cury):
            print('NO')
            break
        s=s+(j[0]-curx)*'R'+(j[1]-cury)*'U'
        curx,cury = j
    else:
        print('YES')
        print(s)
