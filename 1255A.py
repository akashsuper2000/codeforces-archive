for i in range(int(input())):
    a,b = [int(j) for j in input().split()]
    c = 0
    if(a==b):
        print(0)
    else:
        if(a<b):
            a,b = b,a
        a = a-b
        c = a//5
        a = a%5
        c+=a//2
        a=a%2
        c+=a
        print(c)
        
