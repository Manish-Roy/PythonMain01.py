# Reverse multiplication table

number = int(input("Enter a number -> "))


count = 10 
while count >= 1:
    mul = count * number
    print( number , 'X' , count , '=' , mul)
    count = count - 1 

