num = int (input ('Enter the number: '))
sqrt = int ((num**0.5))
count=0
for n in range (2, sqrt+1):
    if num % n ==0:
        count+=1
        break
    if count ==0:
        print(f'{num} is prime')
        else :
            print(f'{num} is not prime')