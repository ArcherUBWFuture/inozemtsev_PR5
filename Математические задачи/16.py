
#Вычислить площадь круга S и длину окружности L. 

#правки
#добавить возможность выбора вычисления: площадь или периметр вписанного в окружность квадрата 
#добавить вычисление этих параметров
#добавить вычисление периметра и площади описанного квадрата
import math
r = float(input('Введите радиус круга и окружности: '))
print(f'Длина окружности с радиусом {r} равна: {2 * math.pi * r}', f'\nплощадь круга с радиусом {r} равна: {math.pi*(r**2)}')
SorP = int(input('Выберите что вычислить, площадь или периметр вписанного в окружность квадрата? \nЕсли площадь вписанного в окружность квадрата, нажмите цифру 1  \nЕсли периметр вписанного в окружность квадрата, нажмите цифру 2\nВаш выбор: '))
if SorP == 1:
    print(f'Площадь вписанного в окружность квадрата = {((r**2)*2)}')
elif SorP == 2:
    print(f'Периметр вписанного в окружность квадрата = {4*r*(math.sqrt(2))}')
print(f'Площадь описанного квадрата = {4*(r**2)}\nПериметр описанного квадрата = {8*r}')   
