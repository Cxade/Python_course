# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего 
# на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 
# просто пропускаем данную итерацию степени


from random import choice


def polynomial(num: int, name:str):
    if num < 1:
        return 0

    poly = ""
    num_list = range(0, 20)

    with open(name, "a", encoding="utf-8") as my_file:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')} "

        my_file.write(f"{poly}{choice(num_list)} = 0\n")


polynomial(5, "poly.txt")
polynomial(5, "poly_2.txt")



