for i in range(int(input())):
    c,s = [int(j) for j in input().split()]
    if(s<=c):
        print(s)
    else:
        a = s//c
        p = s%c
        print(int(pow(a,2)*(c-p)+pow(a+1,2)*(p)))
