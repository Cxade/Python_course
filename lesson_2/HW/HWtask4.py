# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


def RandomList(N):
    list = [-N]
    x = -N
    for i in range(-N, N):
        x +=1
        list.append(x)
    return list


def recordPosition(list):
    with open ('HWtask4_text.txt', 'w') as data:
        for i in range(len(list)):
            data.write(f'{list[i]}\n')


def multiPosition(x1, x2):
    file = open('HWtask4_text.txt', 'r')
    s = file.readlines()
    s = [line.rstrip() for line in s]
    print(s)
    multi = int(s[x1-1])*int(s[x2-1])
    return(multi)


list_1 = RandomList(6)
recordPosition(list_1)
print(multiPosition(2, 4))




# def multiPosition():
#     file = open('HWtask4_text.txt', 'r')
#     s = file.readlines()
#     print(s)
#     s.remove('\n')
#     print(s)
#     file.close()
#     exit()

# multiPosition()


# def multiPosition():
#     path = 'HWtask4_text.txt'
#     data = open(path, 'r')
#     for line in data:
#         print(line)
#     data.close()
#     exit()

# list_1 = RandomList(4)
# print(list_1)
# recordPosition(list_1)

# path = 'HWtask4_text.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()



# with open ('HWtask4_text.txt', 'a') as data:
#     data.write(f'1) {list[1]}\n')