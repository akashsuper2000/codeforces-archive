import heapq
n = int(input())
a = [int(i) for i in input().split()]
eve = {i:{} for i in range(n)}
ans = [0 for i in range(n)]
eve[-1] = {}
odd = eve.copy()
odd[-1] = {}
for i in range(n):
    if(a[i]%2==0):
        eve[-1][i]=0
    else:
        odd[-1][i]=0
    if(i-a[i]>=0):
        eve[i-a[i]][i]=1
        odd[i-a[i]][i]=1
    if(i+a[i]<n):
        eve[i+a[i]][i]=1
        odd[i+a[i]][i]=1

def dijk(g,src):
    dist = [int(1e5) for i in range(n+1)]
    dist[src] = 0
    h = [[j,i] for i,j in enumerate(dist)]
    h[-1][1] = -1
    for i in range(n+1):
        heapq.heapify(h)
        u = heapq.heappop(h)
        dist[u[1]] = u[0]
        for j in h:
            if(j[1] in g[u[1]] and j[0]>u[0]+g[u[1]][j[1]]):
                j[0] = u[0]+g[u[1]][j[1]]
    return dist

dist = dijk(eve,-1)
for i in range(n):
    if(a[i]%2!=0):
        ans[i] = dist[i]
        if(ans[i]==100000):
            ans[i]=-1
dist = dijk(odd,-1)
for i in range(n):
    if(a[i]%2==0):
        ans[i] = dist[i]
        if(ans[i]==100000):
            ans[i]=-1
print(*ans)
