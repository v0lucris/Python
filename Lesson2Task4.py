#4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input("Write count: "))
lst1 = []
for i in range(-n,n+1):
    lst1.append(i)
    
print(lst1)

with open('file.txt', 'r') as my_file:
    data = my_file.read()
lst = data.split()    

res = [int(x) for x in lst]
print(res)

list_length = len(lst1)
POfElements = 1
for i in range(len(res)):
    POfElements = POfElements * lst1[res[i]]
    i = i + 1
  

print("P of all the elements in the list is:", POfElements)