#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
diap = [0,1] 
print(type(diap))
flag = True
for x in diap:
    for y in diap:
        for z in diap:
            f1 = not (x or y or z)
            f2 = not x and not y and not z
            print(x,y,z,f1 == f2)
            if f1 != f2:
                flag = False
if flag:    
    print('Доказано')
else:
    print('Это не так')
    