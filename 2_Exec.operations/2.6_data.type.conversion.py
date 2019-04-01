#Конвертирование данных в Phyton
#   Функция     Описание
#   int(x)      преобразует [x] в целое число
#   float(x)    преобразует [x] в целое число с плавающей точкой
#   str(x)      преобразует [x] в строковое представление
#   chr(x)      преобразует целое [x] в символ
#   unichr(x)   преобразует целое [x] в символ юникода (Unicode)
#   ord(x)      преобразует [x] в целое число
#   hex(x)      преобразует [x] в шестнадцатиричную строку
#   oct(x)      преобразует [x] в восьмиричную строку

a = input('Enter A Number: ')
b = input('Now Enter Another Number: ')

sum = a + b
print('\nDate type sum:', sum, type(sum))

sum = int(a) + int(b)
print('Date type sum:', sum, type(sum))

sum = float(sum)
print('Date type sum:', sum, type(sum))

#Для получения значения назначить a=60, b=5 (пример получим 65, в ASCII это A)
sum = chr(int(sum))
print('Date type sum:', sum, type(sum))
