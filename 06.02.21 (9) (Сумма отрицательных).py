i = 0
itog = 0
stroka = [7,1,3,4,3,9,14,-5,-17,-13,-19,-18]

while i <= 11:
    if stroka[i]<0:
        itog += stroka[i]
    i += 1
print(stroka, '\nСумма отрицательных чисел = ', itog)
