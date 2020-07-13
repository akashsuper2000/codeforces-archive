n,k = [int(i) for i in input().split()]
s = list(input())
a = set([i for i in input().split()])
l = 0
ans = 0
for i in range(n):
    if(s[i] not in a):
        ans+=(l*(l+1))//2
        l = 0
    else:
        l+=1
ans+=(l*(l+1))//2
print(ans)

