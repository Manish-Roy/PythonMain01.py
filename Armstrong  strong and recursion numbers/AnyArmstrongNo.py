n= int(input("Enter the number"))
sum=0
order=len(str(n))

num=n


while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10


    if(sum==num):
        print(f'{num} is an Armstrong no.')
    else:
            print(f'{num} is not an Armstrong no.')
            