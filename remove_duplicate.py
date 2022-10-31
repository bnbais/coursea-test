""" Returns the given list without duplicates.
    The order of the returned list doesn't matter.

    For example:
    - If we call remove_duplicates([1,2,1,3,4]), we'll get [1,2,3,4] in return
    - If we call remove_duplicates([]), we'll get [] in return

    Hint(s):
    - Remember, you can create a set from a string, which will remove the duplicate elements
    """
def remove_duplicates(strings):
    if name!=[]:
        s=set(name)
        s=list(s)
        return s
    else:
        return name
name=[i for i in input().split(',')]   
print(remove_duplicates(name))
