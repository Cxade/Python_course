# 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def transform(N):
    result = []
    while N > 0:
        result.append(N % 10)
        N //= 10

    result.reverse()
    return(result)


def non_recurring(list1):
    result = []
    for i in range(len(list1)):
        if list1.count(list1[i]) == 1:
            result.append(list1[i])
    return result


print(non_recurring(transform(47756688399943)))
print(non_recurring(transform(1113384455229)))
print(non_recurring(transform(1115566773322)))

# либо можно было в одну строчку
# result = [i for i in list1 if list1.count(i) == 1]









