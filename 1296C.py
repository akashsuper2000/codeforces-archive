for i in range(int(input())):
    n = int(input())
    m = 3e5
    mi,ma = 0,0
    s = {(0,0):0}
    st = [0,0]
    d = {'L':[-1,0],'R':[1,0],'U':[0,1],'D':[0,-1]}
    ch = input()
    c = 0
    for j in range(n):
        c+=1
        st[0]+=d[ch[j]][0]
        st[1]+=d[ch[j]][1]
        if(tuple(st) in s):
            if(c-s[tuple(st)]<m):
                m = c-s[tuple(st)]
                ma = c
                mi = s[tuple(st)]
            s[tuple(st)] = c
        else:
            s[tuple(st)] = c
    if(mi==0 and ma==0):
        print(-1)
    else:
        print(mi+1,ma)
