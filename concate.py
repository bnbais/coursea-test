""" Concatenates the given list of strings into a single string.
    Returns the single string.
    If the given list is empty, returns an empty string.

    For example:
    - If we call concatenate(["a","b","c"]), we'll get "abc" in return
    - If we call concatenate([]), we'll get "" in return

    Hint(s):
    - Remember, you can create a single string from a list of multiple strings by using the join() function
    """
    
    
    
def concatenate(strings):
    for ch in name:
        if ch=="":
            return str(''.join(name))
    else:
        s=''.join(name)
    return str(s)

name=[str(i) for i in input().split(',')]
print(concatenate(name))