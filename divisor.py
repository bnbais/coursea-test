""" Returns a list with all divisors of the given number n.
    As a reminder, a divisor is a number that evenly divides another number.
    The returned list should include 1 and the given number n itself.
    The order of the returned list doesn't matter.

    For example:
    - If we call divisors(10), we'll get [1,2,5,10] in return
    - If we call divisors(1), we'll get [1] in return
    """
def divisor(strings):
    div=[]
    for n in range(1,num+1):
        if num%n==0:
            div.append(n)
    return div

num=int(input())
print(divisor(num))