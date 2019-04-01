# \t - т.н. управляющая последовательность, добавляющая символ табуляции
a = 8
b = 2
print('Addition:\t', a, '+', b, '=', a + b)
print('Subscription:\t', a, '-', b, '=', a - b)
print('Multiplication:\t', a, 'x', b, '=', a * b)
print('Division:\t', a, '/', b, '=', a / b)
print('Floor division:\t', a, '÷', b, '=', a // b)
print('Modules:\t', a, '%', b, '=', a % b)
print('Exponent:\t', a, '² = ', a ** b,  sep = '')

b = input('Input b = ')
c = input('Input c = ')
d = input('Input d = ')
e = input('Input e = ')
f = input('Input f = ')
print(a, '=', b, '*', c, '-', d, '%', e, '/', f, '=', int(b) * int(c) - int(d) % int(e) / int(f))
#Вывести: a = (b * c) - ((d % e) / f)

# Присваивание значений (сокращенные формы)
#Оператор   Пример      Аналог
#   =       a = b       a = b       Присвоить значение
#   +=      a += b      a = (a + b) Добавить и присвоить
#   -=      a -= b      a = (a - b) Вычесть и присвоить
#   *=      a *= b      a = (a * b) Умножить и присвоить
#   /=      a /= b      a = (a / b) Разделить и присвоить
#   %=      a %= b      a = (a % b) Взять по модулю
#   //=     a //= b     a = (a // b)
#   **=     a **= b     a = (a ** b)

a, b = 8, 2
#Выведем присвоенные значения a и b
print('Assign Values:\t\t', 'a =', a, '\t, b =', b)
a += b
print('Add & Assign:\t\t', 'a =', a, '\t (8 + 4)')
a -= b
print('Subtract & Assign:\t', 'a =', a, '\t (12 - 4)')
a *= b
print('Multiply & Assign:\t', 'a =', a, '\t (8 x 4)')
a /= b
print('Divide & Assign:\t', 'a =', a, '\t (32 / 4)')
a %= b
print('Multiply & Assign:\t', 'a =', a, '\t (8 % 4)')
