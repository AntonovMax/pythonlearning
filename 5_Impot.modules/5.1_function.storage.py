"""
    Хранение функций

    При определении функции ее можно записать в одном или нескольких файлах, а затем использовать в другиз программах
без дополнительного копирования в каждую из них.
    Такой файл называется модулем, а именем является имя файла без расширения .py.
    Доступ к модулю можно получить через импорт (import имя-модуля).
    Любую импортированную функцию можно вызвать через суффиксную (точечную) запись:
        имя-модуля.имя-функции
    прим.: чтобы вызвать функцию steps из импортированного модуля с именем ineasy достаточно набрать:
        ineasy.steps()

    Если хранязиеся в модуле функции хранят аргументы, полезно назначить аргументам значения по-умолчанию, это сделает
функция более универсальной, так как при вызове ее из какого-либо места программы указание аргументов становится
необязательным.

    При импорте модуля можно создать его псевдоним используя ключевые слова 'import as'.
    Пример:
    import cat is tom позволит использовать все функции модуля cat под именем tom.
"""

# 1. Определить функцию, в которой для вывода используется значение аргумента по умолчанию.
"""
def purr(pet = 'A Cat'):    # purr - мурлыкать
    print(pet, 'Says MEOW!')
"""
# 2. Добавить еще 2 определения функций, в которых также используются значения их аргументов по умолчанию для
# использования при вводе.
"""
def lick(pet = 'A Cat'):    # lick - облизывать, лакать
    print(pet, 'Drinks Milk!')
def nap(pet = 'A Cat'):     # nap - дремать, вдремнуть
    print(pet, 'Sleeps by the fire')
"""
# 3. Сохранить в файл cat.py
# 4. Начать программу в которой необходимо импортировать мудуль cat. (kitty.py)
# 5. Добавить вызовы для трех функций без подстановки аргумента purr(), lick(), nap().
# 6. Добавить еще по одному вызову функций, передав им по одному аргументу.
"""
cat.purr('\nKitty')
cat.lick('Kitty')
cat.nap('Kitty')
"""
# 7. Начать еще программу tiger.py, сделав доступными функции модуля cat еще раз.
"""
import cat
"""
# 8. Зпросить у пользователя ввода имени переменной, которая перезапишет значение аргументов
# функции по умолчани.
"""
pet = input('Enter a pet name: ')
"""
# 9. Вызвать 3 функции еще раз, передав в качестве аргумента значение переменной, определенное
# пользователем.