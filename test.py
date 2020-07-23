def compute(expression):
#blah
#blah2
#blah3
#blah5
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    if operator == '+':
        return num0 + num1
    else:
        print('unknown operator!')
        return 0
