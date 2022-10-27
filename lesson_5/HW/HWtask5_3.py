# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


def RLE_enc(text: str):
    count = 1
    encoded_str = ''
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count +=1
        elif count == 1:
            encoded_str += str(count) + text[i-1]
        else:
            encoded_str += str(count) + text[i-1]
            count = 1
        if i == len(text)-1:
            encoded_str += str(count) + text[i]
    return(encoded_str)



def RLE_dec(text: str):
    decoded_str = ''
    for i in range(len(text)):
        if text[i].isdigit():
            decoded_str += int(text[i]) * str(text[i+1])
    return(decoded_str)

with open('file_encode.txt', 'w') as file:
    file.write('AAAAAAAAAVENGERSssssssDA')


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = RLE_enc(decoded_string)
    file.write(encoded_string)

print('Decoded string: ' + decoded_string)
print('Encoded string: ' + RLE_enc(decoded_string))


