# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:
#- 6782 -> 23
#- 0,56 -> 11



count = float(input("Write count: "))
count1 = str(count)
print(type(count1))

print(tuple(count1)) # проебразовываем в кортеж
print(list(count1)) # преобразовываем в список
count2 = list(count1)
count2.remove('.') #удаляем точку
print(count2)
res = [int(x) for x in count2] # список строк преобразуем в список чисел
print(res)
list_length=len(res) #длина списка

sumOfElements=0
for i in range(list_length):
    sumOfElements = sumOfElements + res[i]
    

print("Sum of all the elements in the list is:", sumOfElements)
