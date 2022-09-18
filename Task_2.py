#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

List = [1]
num = int(input('Введите натуральное число: '))
for i in range (2, num+1):
    if num!=1:
        while num%i==0:
            num= num/i
            List.append(i)
    elif num>1:
        List.append(num)
        break

print(List)