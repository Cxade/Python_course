# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

solution = [1, 4, 8, 7, 5]

def findmax(solution):
    max = solution[0]
    for i in solution:
        if i > max:
            max = i
    return max

print(findmax(solution))