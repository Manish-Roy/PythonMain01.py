num= int(input('Enter a number: -> '))
temp = num
res = int()


while temp:
    last_digit = temp % 10
    res += last_digit
    temp //= 10



    if res == num:
        print(f' number={num} and result = {res} are same so it is a Neon number')


    else:
        print(f' number={num} and result = {res} are not same so it is not a Neon number')