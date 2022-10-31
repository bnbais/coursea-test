def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """
    count=0
    if x>1:
        for i in range(2,x):
            if x%i==0:
                count+=1
                break
    if count==0:
        return True
    else:
        return False    
x=int(input())
isPrime(x)
            