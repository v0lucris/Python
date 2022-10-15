# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Enter number: 6
#[2.0, 2.25, 2.37, 2.44, 2.49, 2.52]



n = int(input())
lst = []
 
num = 0

for i in range(1, n+1):
    num = (1+(1/i))**i
    lst.append(round(num,2))
 
print(lst)
list_length=len(lst)
sumOfElements=0
for i in range(list_length):
    sumOfElements = sumOfElements + lst[i]
    

print("Sum of all the elements in the list is:", sumOfElements)
