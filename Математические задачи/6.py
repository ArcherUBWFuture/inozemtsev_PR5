#Известны координаты двух точек на плоскости.
#Вычислить расстояние между точками.

#правки 
# добавить вычисление длины окружности и площадь круга с радиусом, равным расстоянию между двумя точками.
# добавить вычисление площади и периметра описанной равнобедренной трапеции с указанимем большего и малого основания
import math
print('Введите х и у первой точки')
xa = float(input('Введите x : '))
ya = float(input('Введите y : '))
print('Введите х и у второй точки')
xb = float(input('Введите x : '))
yb = float(input('Введите y : '))
ras = math.sqrt((xb - xa)**2 + (yb - ya)**2)
h = 2*ras
a = float(input('Введите длину большего основания: '))
b = float(input('Введите длину малого основания: '))
print('Расстояние между двумя точками : ', ras)
print(f'Длина окружности с радиусом {ras} равна: {2 * math.pi * ras}', f'\nплощадь круга с радиусом {ras} равна: {math.pi*(ras**2)}')
print(f'Площадь описанной равнобедренной трапеции с указанимем большего - {a} и малого основания - {b}. S  = {((a+b)/2)*h}')
print(f'Периметр описанной равнобедренной трапеции с указанимем большего - {a} и малого основания - {b}. P  = {(a+b+2)*math.sqrt((h**2)+((a-b)**2)/4)}')

