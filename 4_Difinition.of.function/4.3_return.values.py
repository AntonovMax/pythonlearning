""""
    Возвращение значений

    Пользовательская функция может возвращать значение тому оператору, который ее вызвал.
Это выполняется с помощью ключевого слова return с указанием после него возвращаемого значения.

    Пример:
    Чтобы вернуть значение суммы двух складываемых аргументов:
    def sum(a, b) :
        return a + b

возвращаемый результат можно присвоить переменной с помощью инструкции вызова функции и
впоследствии использовать в программе:
    total = sum(8, 4)
    print('8 + 4 = ', total)
    
либо может быть использован непосредственно "на лету":
    print('8 + 4 = ', sum(8, 4))
    
    !!! Можно указать значение аргументов по умолчанию в определении функции.
как правило, инструкция return появляется в самом конце блока функции и возвращает окончательный
результат всех вычислений, производимых инструкциями в теле функции. Однако return может
находиться и в начале блока инструкций, прерывая исполнение всех последующих инструкций этого блока.
Тогда исполнение программы в вызывающем функцию операторе немедленно останавливается.
    При указании значения инструкции return она вернет его оператору, в ином случае вернет None,
такой подход используется, когда нужно пропустить выполнение инструкций, когда определенное
проверочное условие не выполнилось.

    Пример (значение принмаемого аргумента меньше указанного числа):
    def sum(a, b) :
        if a < 5 :
            return
            return a + b
в данном случае, если переданный аргумент меньше 5, функция будет возвращать значение None, а 
последняя инструкция не станет исполняться.

    При выполнении в функции арифметических действий полезно проверять введенные пользоватлем
значения на предмет чисел с помощью встроенной функции isdigit().
"""""

# Задания:
# 1. Инициализировать переменную с помощью пользовательского ввода:

num = input('Enter an integer:')

# 2. Добавить определение функции, которая примет единственный аргумент:

def square(num) :

# 3. Добавить в блок функции инструкцию для проверки переданного значения на предмет того,
# является ли оно числом, и для прерывания дальнейшего исполнения по результатам проверки:

    if not num.isdigit() :
        return 'error: invalid entry'

# 4. Добавить инструкции для приведения типов с помощью функции int, а так же возвращения
# результата возведения значения результата в квадрат.

    num = int(num)
    return num * num

# 5. Добавить инструкции для вывода строки и возвращенного с помощью вызова функции значения:

print(num, 'Square is: ', square(num))

#
#