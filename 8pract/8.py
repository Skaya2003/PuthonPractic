#-- coding: utf-8 --
#вариант 3
x = int(input('Введите 1 катет 1 треуг'))
y = int(input('Введите 2 катет 1 треуг'))
x1 = int(input('Введите 1 катет 2 треуг'))
y1 = int(input('Введите 2 катет 2 треуг'))
def gip():
    if x**2 + y**2 > x1**2 + y1**2:
        print('Гипотенуза первого больше')
    else:
        print('Гипотенуза второго больше')

gip()

# --coding: utf-8 --
def sor(str):
    return ''.join(sorted(str))

str = input('Введите строку')
print(sor(str))