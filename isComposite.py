def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """
    if x<=1:
        return False
    if x<=3:
        return False
    if (x%2==0 or x%3==0):
        return True
    i=5
    while (i*i<=x):
        if (x%i==0 or x%(i+2)==0):
            return True
        i=i+6
        return False
    print(isComposite(9))
    print(isComposite(22))
    print(isComposite(3))
    print(isComposite(41))