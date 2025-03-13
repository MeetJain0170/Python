def findPrime(n):
    is_Prime=True
    for i in range (2,n):
        if n%i==0:
            is_Prime=False
    if is_Prime==True:
        print(str(n)+" is a prime number")
    else:
        print(str(n)+" is not a prime number")    

n=int(input("Enter a Number: "))
findPrime(n)