#-- coding: utf-8--
#4 задание
def summa(n):
    if n == 0:
        return 0
    else:
        return n % 10 + summa(n // 10)

N = int(input('введите число'))
results = summa(N)
print(results)

#-- coding: utf-8--
# 2 задание
def chislo(spisok):
    chis = int(input('Введите число последовательности (0 для окончания): '))
    if chis == 0:
        return spisok
    else:
        spisok.append(chis)
        return chislo(spisok)

def second(lst,enum):
    vast = max(lst)
    if enum == 1:
        return vast
    else:
        lst.remove(vast)
        enum += 1
        return second(lst,enum)

numbers = []

print(f'Второе по величине число последовательности: {second(chislo(numbers),0)}')
