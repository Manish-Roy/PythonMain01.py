num1= int(input('Enter a number->'))
num2= int(input('Enter a number->'))
num3= int(input('Enter a number->'))


if num1>num2 and num1>num3:
    print('{} greater than {} and {}', format(num1, num2, num3))
    elif num2>num3:
        print('{} greater than {} and {}', format (num2, num1, num3))
        else:
            print('{} greater than {} and {}', format (num3, num1, num2))