def main():
   num=int(input('Enter a no '))
   if is_automorphic(num):
       print(f'{num} is an automorphic number')
   else:
       print(f'{num} is not an automorphic number')
       

       def is_automorphic (num:int) 
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



            if res=num:
                Print(f'number={num} and result={res} are same so it is automorphic number')

            else:
                print(f'number={num} and result={res} are not automorphic number')
                