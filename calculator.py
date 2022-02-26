print('this is a calculator\n\n')

operators = {
'double operand' : ['+' , '-' , '*' ,'/','power','^','log'],
'single operand' : ['sin' , 'cos' , 'tan' , 'cot' , 'factorial' , 'fact' , 'sqrt',]
}

while True:
    
    print_ui(operators)
    
    inputs = get_input(operators)
    
    if type(inputs) == tuple:
        operator,num1,num2 = inputs
    else:
        continue
    
    if operator == 'exit':
        break
    
    result = operation(operator,num1,num2)
    
    if result == 'error':
        continue
    else:
        print_result(operators,operator,num1,num2,result)
        
print('you exit calculator!')    
    

def print_ui(ops):
    print(ops['single operand'])
    print(ops['double operand'])
    print('type "exit" to exit the program\n\n')
    
    
def get_input(ops):
    operator = input('please select your operator from list: ')
    try:
        if operator.lower() == 'exit':
            return ('exit',None,None)
        elif operator.lower() in ops['single operand']:
            num = float(input('please enter your number: '))
            return (operator.lower(),num,None)
        elif operator.lower() in ops['double operand']:
            num1 = float(input('please enter your first number: '))
            num2 = float(input('please enter your second number: '))
            return (operator.lower(),num1,num2)
        else:
            print("you don't enter a valid operator\n")
            return (None,None,None)
    except:
        print("you don't enter valid input\n")

    
def operation(op,num1,num2):
    
    import math
    
    if op == '+':
        return num1+num2
    
    elif op == '-':
        return num1-num2
    
    elif op == '*':
        return num1*num2
    
    elif op == '/':
        if num2 == 0:
            print('Error dividing by zero\n')
            return 'error'
        else:
            return num1/num2
        
    elif op == 'power' or op == '^':
        return num1**num2
    
    elif op == 'log':
        if num1 >= 0 and num2 >= 0:
            return math.log(num1,num2)
        else:
            print("you don't enter valid number for this operator\n")
            return 'error'
    
    elif op == 'sin':
        return math.sin(num1)
    
    elif op == 'cos':
        return math.cos(num1)
    
    elif op == 'tan':
        return math.tan(num1)
    
    elif op == 'cot':
        return 1/math.tan(num1)
    
    elif op == 'factorial' or op == 'fact':
        return math.factorial(int(num1))
                              
    elif op == 'sqrt':
        if num1 >= 0:
            num**0.5
        else:
            print("you don't enter valid number for this operator\n")
            return 'error'
                              
        
def print_result(ops,op,num1,num2,result):
    if operator == 'log':
        print(f'log({num1}) in base of {num2} = {result}\n\n')
    elif op in ops['single operand']:
        print(f'{operator}({num1}) = {result}\n\n')
    elif op in ops['double operand']:
        print(f'{num1} {operator} {num2} = {result}\n\n')