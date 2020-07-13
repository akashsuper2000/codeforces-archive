n = int(input())
a = [int(i) for i in input().split()]
b = [1]
l = 1
for i in range(1,n):
    if(a[i]>a[i-1]):
        l+=1
        b.append(l)
    else:
        l = 1
        b.append(l)
l = b[-1]
c = [l]
for i in range(2,n+1):
    if(b[n-i]<b[n-i+1]):
        c.append(l)
    else:
        l = b[n-i]
        c.append(l)
c = c[::-1]
ans = max(c)
for i in range(1,n-1):
    if(a[i-1]<a[i+1]):
        ans = max(ans,b[i-1]+c[i+1]-b[i+1]+1)
print(ans)
