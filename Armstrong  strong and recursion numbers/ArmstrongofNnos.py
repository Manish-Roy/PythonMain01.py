num= n
sum= 0

temp =num
while temp>0 :
 last_digit= temp % 10
sum+= 10
temp //= 10

if num == sum:
    print(num, "is an Armstrong no .")
else:
        print(num, " is not an Armstrong number")
