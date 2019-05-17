"""
    Чтение и запись файлов

    open()  - открыть файл
    close() - закрыть
    read()  - возвращает содержимое файла
    write() - добавляет содержимое в файл
"""

# Задания:
# 1. Проинициализировать переменную, содержащую объединенные строки, а также символы
#    новой строки.

poem = 'I never saw a man who looked\n'
    # Я никогда не видел человека, который смотрел
poem += 'With such a wistful eye\n'
    # С таким задумчивым глазом
poem += 'Upon that little tent of blue\n'
    # На этой маленькой палатке синего цвета
poem += 'Whitch prisoners call the sky'
    # Которые заключенные называют небом

# 2. Создать файловый объект для нового текстового файла с именем poem.txt и записать в него
#    содержимое.

file = open('poem.txt', 'w')

# 3. Записать строку, содержащуюся в переменной, в текстовый файл и закрыть файл.

file.write(poem)
file.close()

# 4. Создать файловый объект для существующего текстового файла для чтения из него.

file = open('poem.txt', 'r')

# 5. Вывести содержимое файла и закрыть.

for line in file :
    print(line, end = '')
file.close()

# 6. Добавить подпись

file = open('poem.txt', 'a')
file.write('\n(Oscar Wilde)')
file.close()

file = open('poem.txt', 'r')
print('\n')
for line in file :
    print(line, end='')
file.close()