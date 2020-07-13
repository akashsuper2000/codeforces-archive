for i in range(int(input())):
    n = int(input())
    s = 0
    while(n!=0):
        s+=n//10*10
        n = n//10+(n-(n//10)*10)
        if(n<10):
            s+=n
            break
    print(s)
