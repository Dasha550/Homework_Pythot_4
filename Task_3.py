#Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


import random 
numbers= [] 
num = int(input('Ведите количество элементов в списке: '))
for i in range(num):
    num2=int(input('Ведите элемент в список: '))
    numbers.append(num2)
print(numbers)

def uniNumbers(numbers):
    uniList = []

    for number in numbers:
        if number in uniList:
            continue
        else:
            uniList.append(number)
    return uniList

print(uniNumbers(numbers))