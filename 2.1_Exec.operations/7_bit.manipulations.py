#Манипуляции с битами
#   LSB - Least Significant Bit (наименее значимый бит)
#   MSB - Most Significant Bit (наиболее значимый бит)
#   № бита  8msb    7   6   5   4   3   2   1lsb
#Десятичное  128    64  32  16   8   4   2   1
#Двоичное    0       0   0   1   0   0   1   0
#
#   Опреатор    Название      Опереция с двоичными числами
#       |       ИЛИ             Возвращает 1 в каждый бит, где один из сравниваемых битов имел значение 1. Пример: 1010 | 0101 = 1111
#       &       И               Возвращает 1 в каждый бит, где оба сравниваемых бита имели значение 1. Пример: 1010 & 1100 = 1000
#       ~       НЕ              Возвращает 1 в каждый бит, где ни один из двух сравниваемых битов не имел значение 1. Пример: 1010 ~ 0011 = 1000
#       ^       Исключающее     Возвращает 1 в каждый бит, где только один из двух сравниваемых битов имел значение 1. Пример: 1010 ^ 0100 = 1110
#                ИЛИ
#       <<      Сдвиг влево     Сдвигет влево биты на указанное колличество позиций. Пример: 0010 << 2 = 1000
#       >>      Сдвиг вправо    Сдвигет вправо биты на указанное колличество позиций. Пример: 1000 >> 2 = 0010

a = 10
b = 5

print('a =', a, '\tb = ', b)
#Изменение значения a 1010 ^ 0101 = 1111 (десятичное 15)
a = a ^ b
#Изменение значения b 1111 ^ 0101 = 1010 (десятичное 10)
b = a ^ b
#Изменение значения a 1111 ^ 1010 = 0101 (десятичное 5)
a = a ^ b
print('a = ', a, '\tb = ', b)


