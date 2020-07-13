for i in range(int(input())):
    n,m = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    if(n==2 or m<n):
        print(-1)
    else:
        b = [j+1 for j in range(n)]
        c = list(sorted(zip(a,b)))
        a,b = [j[0] for j in c], [k[1] for k in c]
        print(int(sum(a)*2+(m-n)*(a[0]+a[1])))
        for j in range(n):
            print(b[j-1],b[j])
        for k in range(m-n):
            print(b[0],b[1])
