# --coding: utf-8 --
# 8 вариант

x = int(input('Введите количество'))
def numeric(x):
    massive = []
    for i in range(x):
        massive.append(int(input('введите число')))
    return massive

massive = numeric(x)
def pro(massive):
    proizv = 1
    for r in massive:
        proizv *= r
    return proizv

proizv = pro(massive)
sum_chisel = sum(massive)
print(f'Сумма чисел:{sum_chisel}\nПроизведение:{proizv}')

# --coding: utf-8 --
list = [5, 0, 2.5, 0, 134, -5, -84.9]
def arifm(list):
    s = sum(list)
    sr_arefm = s / 7
    list = [sr_arefm if n == 0 else n for n in list]
    print(list)
arifm(list)
