num1= int(input ('enter the number to be checked: '))
num2 = int(input('Enter the number: '))
if num2 % num1 ==0:
    print('{} is a  multiple of {}'.format(num1,num2))

else:
    print('{} is not multiple of {}' .format(num1, num2))