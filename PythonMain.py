import Greaterof3nos

if n1==n2==n3:
    print('all three numbers are equal')
elif n1>n2 and n1>n3:
        print(n1,'is greater than', n2, n3)
elif n2>n1 and n2>n3:
        print(n2,'is greater than', n1, n3)
else:
        print(n3,'is greater than', n1, n2)



import AutomorphicNo

def is_automorphic (num:int) :
       
          num=int(input('Enter a number'))
          temp=num
          res=int()

          while temp:
              last_digit=temp%10
              res+= last_digit
              temp//=10


              num = int(input('Enter a number'))
              sqrt=num**2
              temp= num
              boolean=True


          while temp:
              if temp%10 !=sqrt%10
              boolean=False
              break



if res == num:
                Print(f'number={num} and result={res} are same so it is automorphic number')

else:
                print(f'number={num} and result={res} are not automorphic number')
                




import ArmstrongofNnos


if num == sum:
    print(num, "is an Armstrong no .")
else:
        print(num, " is not an Armstrong number")



import Armstrong01


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



import AnyArmstrongNo

if(sum==num):
        print(f'{num} is an Armstrong no.')
else:
            print(f'{num} is not an Armstrong no.')




import ANoMultipleofanotherno 


if num2 % num1 ==0:
    print('{} is a  multiple of {}'.format(num1,num2))

else:
    print('{} is not multiple of {}' .format(num1, num2))



import MultipleofAnother


if num2 % num1== 0:
    print('{} is a multiple of {}'.format(num1, num2))
else:
        print('{} is not multiple of {}'.format(num1, num2))





import Calculator

result1= Calculator.add(2, 3)
print(result1)



result2= Calculator.sub(6, 3)
print(result2)



result3= Calculator.mul(3, 3)
print(result3)



result4= Calculator.div(12, 2)
print(result1)