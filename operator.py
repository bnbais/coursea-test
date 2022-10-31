# Arithmatic operator
from math import floor

print('===========================Addition=================') 
print(2+3)
print(12+34)
print(2.3+4.5)
print(34.5+1)
# floor value
print(floor(34.5+1))
# Round value
print(round(34.5+1))
print('\n')
# You can initialize a variable
num1=39
num2=65
print(num1+num2)
print('\n')
# You can take input from user
num1=int(input('enter num1='))
num2=int(input('enter num2='))
print('{} + {} = {}'.format(num1,num2,num1+num2))
print('\n')
print('=================Subtraction================')
print('\n')
print(5-1)
print(34.5-4.5)
print(3.1-1)
# Floor value
print(floor(23.4-12.3))
#Round Value
print(round(34.5-2))
print('')
# You ca initialize a variable also
num1=45
num2=34
print(num1-num2)
print('\n')
# You can store it by another variable
num1=45
num2=10
num3=num1-num2
print(num3)
print('\n')
# You can also take input from user
num1=int(input('Enter num='))
num2=int(input("Enter num2="))
print('Subtract=',num1-num2)
print('===================================Multiplication====================================\n')
print(3*4)
print(2.3*2)
print(-2.3*2)
# You can initialize a variable
num1=3
num2=4
print(num1*num2)
# You can also take input from user
num1=int(input('Enter num1='))
num2=int(input("Enter num2="))
print('Multiplication=',num1*num2)
print('===================================Division============================================\n')
print(3/2) #It will return float value
print(3//2) #It will return integer value
print('')
# You can initialize a variable also 
num1=34
num2=12
print(num1/num2)
print(num1//num2)
print('')
# You can also take input from user
num1=int(input('Enter num1='))
num2=int(input('Enter num2='))
print('Float division=',num1/num2)
print('Integer division=',num1//num2)
print('')
print('========================Modulo Operator======================================\n')
# Modulo '%' return  Remainder
print(3%2) # It will return remainder 1
print((3*2)%2) # it will retrun  0

print('======================Exponent operator============================================\n')
# Exponent operator is used for power taht means 2 raise to the power 3 can be written in 2**3
print(2**3) # It will return 8 that is 2*2=4*2=8

print('=====================floor division==================')
# It will return floor value
print(12//2) #It will return 6