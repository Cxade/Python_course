# Напишите программу, удаляющую из текста все слова, содерджащие 'абв'


from unittest import result


path = 'text.txt'

dataTxt = ''
with open(path, 'r', encoding='utf-8') as file:
    dataTxt = file.read()

print(dataTxt)
dataTxt = dataTxt.split()
print(dataTxt)

findTxt = input('Введите текст для проверки: ')


resultTxt = []

for word in dataTxt:
    if findTxt not in word:
        resultTxt.append(word)

print(resultTxt)