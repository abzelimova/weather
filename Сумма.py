sign = input("Введите знак + или -")
number = input("Введите 2 числа через пробел")
num = number.split(' ')
print(num[1])
if sign == '+':
    S = float(num[1]) + float(num[0])
    print(S)
elif sign == '-':
    S = float(num[0]) - float(num[1])
    print(S)
else:
    print('Введите + или -')