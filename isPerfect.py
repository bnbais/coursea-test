def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    
    sum=0
    
    for i in range(1,x):
        if x%i==0:
            sum=sum+i
    if sum==x:
        print('The number is perfect!')
    else:
        print('The number is not perfect!')        
x=int(input())  
isPerfect(x)   
    #   for j in sum:
       # final_sum=final_sum+sum[j]
       # print(final_sum,end=' ')
        #if final_sum==x:
           # return True
       # else:
        #    return False
x=int(input())
isPerfect(x)