# function :- 
# Block of organized, reusable code that is used to perform a single, related action or operation.
# It provides better modularity for your application and a high degree of code reusing.
# Built-in function (part of core language)
# Define your function.
# Python built-in function:- print(print output),input(taking input), int(integer),float(float number),round(float,int),
#max(arg1,arg2,...,argN),min(arg1,arg2,........,argN),len(find length),range(n,n-1),
# User define function:-
# function convension:-
       # Name a function based on what it does
       # whitespace is important 
# sometimes function taking an input
       # These are called parameters
       # When you call(or use) them you should provide arugments to satisfy the parameters
# sometime function give output
       # This is call function return value.
# You define a function by using keyword 'def' followed by function_name and followed by 'paranthesis'
       # def function_name(parameter1,parameter2,.......paramterN):
              #statements
              #return
    #Parenthesis consisting optional paramter treating them as variable
    #Function optionally return a value
    
 
 
 # Define a function Square 
          # It takes one number as a parameter.   
          # Return result by quaring that number.
'''
def Square(num):
    y=num*num
    return y
result=Square(10)
print(result)
print('')
print('===========================================================================================\n')



def Square(num):
    y=num*num
    return y
x=int(input("enter number="))
result=Square(x)
print(result)
print('')
print('==============================================================================================\n')


# Define a function greater_num.
         # It take two number as input
         # Return True if 1st number is greater than the 2nd number.
def greater_num(num1,num2):
    if num1>num2:
        return True                  
    else:
        return False
print(greater_num(1,2))        
print('')
print('================================================================================================\n')


def greater_num(num1,num2):
    if num1>num2:
        return True          
    else:
        return False
num1=2
num2=1   
result=greater_num(num1,num2)
print('{} is greater than {}:{}'.format(num1,num2,result))


def greater_num(num1,num2):
    if num1>num2:
        return 'Num1 is greater'            
    else:
        return 'Num2 is greater'
num1=int(input('Enter num1='))
num2=int(input('Enter num2='))    
result=greater_num(num1,num2)
print(result)


print('')
print('============================= User define function: docstring ================================================\n')

# You can(and should )provide documentation string for your function
    # A docstring describes the operation of the function(or class)
# A docstring is for someone who is using your function and wants to know 'What it does ?',at a high level.
# It is different form a comment, which is for a programmer who might be reading your code
# and wants to know the details of 'How it works ?'
# To create a docstring, include a string as the first statement in the function definition
# def greater_than(x,y):
#     """" Returns True if x is greater than y else return False """
       # if X>y:
       #     return True
       # else: 
       #     return False
# print(greater_than(2,3))    
         
# The docstring is accessible to a user of your program by getting 'help' on the function. 
# help(greater_than).
# It is also accessible directly,
#     print(greater_than.__doc__)  
# Note:- __doc__ Doc has two underscore before and after 'doc'. 



print('')
print('==============================================================================================================\n')
# Define a function get_factor:- 
# It takes as integer as a parameter and returns a list of factors of that parameter.
# basically take number from 1 to given number and check number is evenly divided and return that number.
def get_factor(x):
    # Creating docsting
    """Returns the list of factor of the given number""" 
    factor=[]
    # iterate number from 1 to itself.
    for i in range(1,x+1):
        # Check if i divided number x evenly
        if x%i==0:
            factor.append(i)
    return factor
num=int(input('Enter number='))
#help(get_factor)      calling     Docstring
#print(get_factor.__doc__)  calling  Docstring
print(get_factor(num))    
print('')
print('============================================================================================================\n')

# define a function unique_list list of numbers that takes a list of numbers 
# and returns a new list with the unique values
# Approach: -
         # create a new empty list
         # Use a for loop to iterate over the provided list of numbers
         # Add values to the new list if they don't exits already!
         # Return new list!
def unique_list(l):  
    """ Return a list of unique value of list l"""
    # Create a new list
    x=[]
    # iterate list
    for i in l:
        # Check if element which is not present in x
        if i not in x:
            x.append(i)
    return x
print(unique_list([1,1,2,3,1,2,3,4,4,5,4,3,1]))
print('')


def unique_list(l):  
    """ Return a list of unique value of list l"""
    # Create a new list
    x=[]
    # iterate list
    for i in l:
        # Check if element which is not present in x
        if i not in x:
            x.append(i)
    return x
print(unique_list([1,1,2,1,2,3,1,2,3,4,1,2,3,2,1,3,1,3,2,4,5,5,6,4,3,2,5,6,4,3,2,6,7,5,4,3,3,2,3,4,5,4,3])) 
 '''    
print('=======================Vowel/word counter Program===========================\n')                 
# Create a new script file. Write a program does the following:- 
# - Counts the number of vowel in string.
# - counts the number of words in a senetence.

# Conunts number of vowel in stirng
def vowel_count(string):
    """ Counts the number of vowel in the given stirng!
    for exit enter negative one 
    """
    vow_count=0
    # Iterate a loop over string
    for char in string:
        if char in 'aeiou':
            vow_count+=1
    return vow_count

# Counts number of words in a sentence.
def word_count(sentence):
    # Remove white space from start and end of sentence.
    #sentence=sentence.strip()
    # Initialize counter variable
    space_counter=0
    # Iterate a for loop over sentence.
    for char in sentence:
        if char in ' ':
            space_counter+=1
    word_counter=space_counter+1
    return word_counter

# define main function
def main():
    while 1==1:
        #input_string=input('enter string=')
        input_sentence=input('Enter  sentence=').strip()
        #if input_string=='-1':
        if input_sentence=='-1':
            break
        #print(vowel_count.__doc__)
        #print(vowel_count(input_string),'number of vowels in ',input_string)  
        print(word_count(input_sentence),'words in ','\'',input_sentence,'\'')
# to execute main function.
if __name__== '__main__':
    main()        
         
