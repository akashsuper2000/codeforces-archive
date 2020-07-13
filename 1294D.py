q,x = [int(i) for i in input().split()]
mex = 0
a = set()
for i in range(q):
    p = int(input())
    if(p<=mex):
        p = p+x*(max(0,mex-p)//x)
        while(p in a):
            p+=x
        a.add(p)
    elif(p>mex):
        p = p-x*((p-mex)//x)
        while(p in a):
            p+=x
        a.add(p)
    while(mex in a):
        mex+=1
    print(mex)
