#   Выход из цикла.
#   break - ключевое слово используется для принудительного выхода из цикла, когда
# выполняется какое-то улсловие. Располагается внутри инструкции цикла после проверяемого
# выражения. При получении True, цикл заканчивается, программа передает управление
# следующей инструкции. Прим.: если break стоит во вложенном цикле, управление передасться
# наружному циклу.

# Задание:
# 1. Описать инструкцию, создающую цикл, выполняющийся 3 раза.

for i in range(1, 4) :

# 2. Добавить инструкцию, создающую вложенный цикл.

    for j in range(1, 4) :

# 3. Добавить вывод значений счетчиков (как внутреннего цикла, так и наружного)
# для каждого прохода внутри цикла.
        print('Running i =', i, 'j =', j)