# -- coding: utf-8 --
n = int(input('Введите ЧИСЛО'))
def main(n):
    for i in range(n):
        if i**2 <= n:
            print(i**2)
main(n)

# -- coding: utf-8 --
def res():
    chis = 0
    while chis < 2:
        chis = int(input('Введите число, не меньшее 2: '))
        if chis >= 2:
            break
        else:
            print('Число должно быть не меньше 2')
    return chis

def main():
    n = res()
    for i in range(2, n + 1):
        if n % i == 0:
            return i

print(main())

# -- coding: utf-8 --
n = int(input('Введите N: '))
def main(n):
    a = 2
    b = 1
    while a <= n:
        a *= 2
        b += 1
    return(f'Показатель: {b - 1}, Степень: {a // 2}')

print(main(n))

# -- coding: utf-8 --
x = int(input('Введите X: '))
y = int(input('Введите Y: '))

def fx(x):
    percent = (x / 100)*10
    x += percent
    return x

def days(x, y):
    days = 0
    while x <= y:
        x = fx(x)
        days += 1
    return days

print(days(x,y))
# -- coding: utf-8 --
def main():
    n = 0
    while int(input('Введите число последовательности: ')) != 0:
        n += 1
    return n
print(main())
# -- coding: utf-8 --
def main():
    i = 1
    n = 0
    list = []
    while i != 0:
        i = int(input('Введите число последовательности: '))
        n += 1
        list.append(i)
    return (sum(list)/(n-1))
print(main())
# -- coding: utf-8 --
def main():
    r = 1
    n = 0
    list = []
    while r != 0:
        r = int(input('Введите число последовательности: '))
        n += 1
        list.append(r)
    return (sum(list)/(n-1))
print(main())
# -- coding: utf-8 --
def main():
    r = 1
    n = 0
    list = []
    while r != 0:
        r = int(input('Введите число последовательности: '))
        list.append(r)
    for x in range(1, len(list)):
        if list[x] > list[x -1]:
            n += 1
    return n
print(main())
# -- coding: utf-8 --
def main():
    z = 1
    x = 1
    y = 1
    list = []
    while z != 0:
        z = int(input('Введите число последовательности: '))
        list.append(z)
    for n in range(1, len(list)):
        if list[n] == list[n - 1]:
            x += 1
        else:
            x = 1
        if x > y:
            y = x
    return y
print(main())