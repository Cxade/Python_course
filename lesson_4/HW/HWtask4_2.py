# 2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

def multipliers(N):
    simple = []
    d = 2
    while d**2 <= N:
        while N % d == 0:
            simple.append(d)
            N = N / d
        d += 1
    if N > 1:
        simple.append(int(N))
    return simple

print(multipliers(165))

