#Enter the number to check
print(' Enter the number:')
n=int(input())
#save the number in another variable 
temp=n 
sum=0
#Implementation
while(temp):
    r=temp%10 # r will have the value of the unit place digit
    temp=temp//10
    fac=1
    for i in range(1,r+1): #finding factorial
        fac=fac*i 
        
    sum+=fac #adding all the factorial
    
if(sum==n):
    print('Yes', n ,'is a strong number')
    
    
else:
    print('No' , n, 'is not a strong number')