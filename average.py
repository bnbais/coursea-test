# write a programe to take input from user until they wont enter number
# If user want to find average of entered numbers display average of all number which is entered.
from secrets import choice
from numpy import average


num_lst=[]
i=0
playing= True
while playing==True:
    num=int(input('Enter number='))
    # check if num==-1 then exit loop.
    if num==-1:
        playing=False
    else:
        num_lst.append(num)
        i+=1
num_sum=0
for num in num_lst:
    num_sum+=num
num_avg=num_sum/i
print('average=',num_avg)
            
        