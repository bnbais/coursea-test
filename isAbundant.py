def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum=sum+i
    if sum>x:
        print('The number is Abundent!')
    else:
        print('The number is not Abundent!')        
x=int(input())  
isAbundant(x)  