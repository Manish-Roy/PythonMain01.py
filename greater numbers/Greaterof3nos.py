n1=int(input('Enter the number'))
n2=int(input('Enter the number'))
n3=int(input('Enter the number'))

if n1==n2==n3:
    print('all three numbers are equal')
elif n1>n2 and n1>n3:
        print(n1,'is greater than', n2, n3)
elif n2>n1 and n2>n3:
        print(n2,'is greater than', n1, n3)
else:
        print(n3,'is greater than', n1, n2)