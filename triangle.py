num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
num3 = int(input('enter third number: '))

if num1< num2+num3 and num2<num1+num3 and num3<num1+num2:
    print('this is a triangle')
else:
    print('it is not a triangle')