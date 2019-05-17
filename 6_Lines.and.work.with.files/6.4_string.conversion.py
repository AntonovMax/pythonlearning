"""
    Преобразование строк. стр. 106 МакГрат


"""

# Задания:
# 1. Проинициализирвоать переменную, содержащую не-ASCII символы, а затем вывести ее значение, типа данных, длину.

s = 'Röd'
print('Red string:',s,'Type:', type(s), '\tLenght:', len(s))
    # Результат: Red string: Rod Type: <class 'str'> 	Lenght: 3

# 2. Преобразовать строку с помощью encode, затем вывести значение, тип данных, длину.

s = s.encode('utf-8')
print('Encoded String:',s,'Type:', type(s), '\tLenght:', len(s))
    # Результат: Encoded String: b'Rod' Type: <class 'bytes'> 	Lenght: 3

# 3. Произвести обратное преобразование с помощью decode, затем еще раз вывести значения, чтобы отобразить
#    шестнадцатиричный код не-ASCII-символа.

s = s.decode('utf-8')
print('Encoded String:',s,'Type:', type(s), '\tLenght:', len(s))
    # Результат: Encoded String: Rod Type: <class 'str'> 	Lenght: 3

# 4. Добавить инструкции с импортом модуля unicodedata и получить Unicode-имя для каждого символа в строке,
#    создав цикл.

import unicodedata
for i in range(len(s)) :
    print(s[i], unicodedata.name(s[i]), sep=': ')
    #Результат:
    # R: LATIN CAPITAL LETTER R
    # ö: LATIN SMALL LETTER O WITH DIAERESIS
    # d: LATIN SMALL LETTER D

# 5. Добавить инструкции, присваивающие переменной новое значение, которое включает шестнадцатиричный код
#    не-ASCII, затем вывести преобразованную строку.

s = b'Gr\xc3\xb6n'
print('Green String:', s.decode('utf-8'))
    # Результат: Green String: Grön

# 6. Добавить инструкцию с присваиванием переменной нового значения, которое включает Unicode-имя для
#    не-ASCII-символа, затем вывести строку.

s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print('Green string:', s)
    # Результат: Green String: Grön
