#4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = '1 четверть, 2 четверть, 3 четверть, 4 четверть'
quarterstr = quarter.split(', ')
index = int(input("введите номер четверти: "))


if  quarterstr[index - 1] == '1 четверть':
    print('x > 0 and y > 0')
elif  quarterstr[index - 1] == '2 четверть':
    print('x < 0 and y > 0')
elif  quarterstr[index - 1] == '3 четверть':
    print('x < 0 and y < 0')
elif  quarterstr[index - 1] == '4 четверть':
    print('x > 0 and y < 0')
else:
    pass
