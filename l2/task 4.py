print('введите первое число')
a = int(input())
print ('введите операцию')
c = (input())
print('введите второе число')
b = int(input())

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('Ошибка!')
elif c == '//':
    print('Ошибка!')
elif c == '%':
    print('Ошибка!')


