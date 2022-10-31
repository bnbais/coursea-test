# Logical operator 'and', 'or', 'not'
# Logical operator are used to combine conditional statements
from traceback import print_tb



# AND  operator return 'True' if both condition is true otherwise it will return 'False'
print('===========================================AND Operator========================================================')
# Check 2 and 3 is greater than 4
print(2 and 3 > 4) # It will return boolean value 'False'
print(2 and 3 < 4) # It will return boolean value 'True'
print(2/3 and 3/2 )
print(2/3 and 3/2 > 1) # It will return 'True'
print(2>1 and 3<1) # It will return 'False'

# You can also compare two numbers
num1=2
num2=3
print(num1 and num2 >=1)
print('')
print('==============================OR operator============================\n')
# OR operator return 'True' if any condition is true, else return 'False'
print(2>3 or 3>1 ) # It will return 'True'
print(2>1 or 5>1 ) # It will return 'True'
print(2<1 or 3>4 ) # It will return 'False'
print('')
print('==============================NOT operator============================\n')
# NOT operator return true if condition is not true else return 'False'
print(not(2==3)) # It will return 'True'
print(not(2==2)) # It will return 'False'


