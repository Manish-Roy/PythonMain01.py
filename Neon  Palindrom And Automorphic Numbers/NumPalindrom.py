number = int (input())
temp = number 
reverse=0


while (number>0):
    dig = number % 10
    reverse=reverse*10+dig
    number = number // 10



    if temp == reverse:
           print("number is palindrome")


    else:
        print("number is not palindrome")


