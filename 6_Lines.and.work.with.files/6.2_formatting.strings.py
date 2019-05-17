"""
    Форматирование строк, стр. 102 МакГрат.

    функция dir() используется для получения имен всех функций и переменных, определенных в модуле,
при этом имя нужного модуля указывается ей в скобках в качестве параметра. Для этих целей можно вос-
пользоваться интерактивным режимом, импортировать требуемы модуль и вызвать функцию dir().
    Ниже пример, в котором проверяется модуль dog, созданный в пред. главе.
    >>> for i in dir(dog) :
            print(i)

    __builties__
    __cached__
    __doc__
    __file__
    __initializing__
    __loader__
    __name__
    __package__
    bark
    lick
    nap
    >>>
!!! После вызова функции dir() среди других имен появляется также атрибут __dcc__, рассмотренный в
предыдущем примере.

    Имена, которые начинаются и заканчиваются символом двойного подчеркивания, являются зарезерви-
рованными объектами языка python, а все остальные - определенными программистом. При помощи dir()
можно также получать список имен функций и переменных, определенных по умолчанию в модуле __builtins__
таких как, например, функция print() и объект str.
    Объект str определяет несколько полезных методов для формирования строк, включая метод format(),
который производит подстановки. Строка, которую необходимо отформатирвоать методом format(), может
содержать текстовые поля и поля для замены, куда будет подставляться текст из списка элементов, разде-
ленных зяпятой. Каждое поле замены обозначается парой фигурных скобок {}. Внутри фигруных скобок может
стоять порядковый номер заменяемого элемента, в соответствии с которыми будут происходить подстановки
из списка.
    Строки можно так же форматировать с помощью оператора замены %s, как в языке С. Данный оператор
будет помечать места в строке, куда будет вставляться текст из упорядоченного списка значений.

!!! Не путайте объект str, описанный здесь, с функцией str(), которая преобразует переменные к строко-
вому типу.

!!! Вокруг индексов в полях замены недопустимы симвовлы пробела.

!!! Для другиз типов данных при форматировании используются^
    %d - для целых чисел;
    %c - для символов;
    %f - для чисел с плавающей точкой.
"""

# Задачи:
# 1. Проинициализировать переменную форматирвоанной строкой.

snack = '{} and {}'.format('Burger', 'Fries')

# 2. Вывести значение переменной, чтобы увидеть текст, подставленный в нее у казанном порядке.

print('\nReplaced:', snack)

# 3. Присвоить этой же переменной значение строки, отформатированной по другому (с использованием индексов)

snack = '{1} and {0}'.format('Burger', 'Fries')

# 4. Вывести значение переменной заново, чтобы увидеть, что теперь строки представляются в соответствии с
#    указанным порядком индексов.

print('Replaced:', snack)

# 5. Присвоить переменной еще одно значение строки.

snack = '%s and %s' % ('Milk', 'Cookies')

# 6. Вывести значение переменных еще раз, чтобы увидеть, строки подставились в нужном порядке.

print('\nSubstituded:', snack)