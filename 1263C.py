def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    a = []
    for p in range(n + 1): 
        if prime[p]: 
            a.append(p)
    return a

for i in range(int(input())):
    n = int(input())
    a = SieveOfEratosthenes(n)
    a.insert(0,0)
    a.insert(1,1)
    if(a[-1]!=n):
        a.append(n)
    if(len(a)>3):
        a.pop(-2)
    if(2*a[-2]>n):
        a[-2]-=1
    print(len(a))
    print(*a)
    
