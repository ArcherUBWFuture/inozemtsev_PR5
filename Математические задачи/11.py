#Дана сторона квадрата.
#Вычислить его периметр, площадь и длину диагонали.

#правки
#добавить возможность выбора типа окружности (описанная или вписанная)
#добавить вывод площади и длины вписанной или описанной окружности
#найти площадь  равностороннего треугольника, вписанного в выбранную окружность
import math
a = float(input('Введите длину стороны квадрата: '))
P = 4*a
S = a**2
d = a*math.sqrt(2)
print('Периметр квадрата: ', P, '\nПлощадь квадрата: ', S, '\nДлина диагонали квадрата: ', d)
OorV = int(input('Выберите тип окружности (описанная или вписанная)\nЕсли описанная окружность, нажмите цифру 1  \nЕсли вписанная окружность, нажмите цифру 2\nВаш выбор: '))
r_op = (((math.sqrt(2))/2)*a)
r_vp = (a/2)
if OorV == 1:
    print(f'Длина описанной окружности = {2*math.pi*(((math.sqrt(2))/2)*a)}',f'\nПлощадь описанной окружности = {math.pi*(0.5*(a**2))}')
    print(f'Площадь  равностороннего треугольника, вписанного в описанную окружность = {(r_op**2)*((3*(math.sqrt(3)))/4)}')
elif OorV == 2:
    print(f'Длина вписанной окружности = {2*math.pi*(a/2)}',f'\nПлощадь вписанной окружности = {(math.pi*(a**2))/4}')
    print(f'Площадь  равностороннего треугольника, вписанного в вписанную окружность = {(r_vp**2)*((3*(math.sqrt(3)))/4)}')

    