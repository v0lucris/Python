# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

week = 'Понедельний вторник среда четверг пятница суббота воскресенье'
weekstr = week.split()
index = int(input("Write count: "))
#while index < (len(weekstr) + 2):
    #print(weekstr[index - 1])
    #break

if  weekstr[index - 1] == 'суббота' or weekstr[index - 1] == 'воскресенье':
    print('Yes')
else:
    print('No')
