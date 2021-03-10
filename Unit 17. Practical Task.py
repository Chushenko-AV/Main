# Напишите программу, которой на вход подается последовательность чисел через пробел, а также
# запрашивается у пользователя любое число.
#=----------------------------------------------------------------------------------------------------------
# В качестве задания повышенного уровня сложности можете выполнить проверку
# соответствия указанному в условии ввода данных.
#=----------------------------------------------------------------------------------------------------------
# Далее программа работает по следующему алгоритму:
#   1. Преобразование введённой последовательности всписок
#   2. Сортировка списка по возрастанию элементов в нем(для реализации сортировки определите функцию)
#   3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий
#      за ним больше или равен этому числу.

# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом
# модуле.Реализуйте его также отдельной функцией.

# Помните, что у вас есть числа, которые могут не соответствовать заданному условию.В этом случае необходимо
# вывести соответствующее сообщение.

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    elements = numbers[0]
    left = list(filter(lambda x: x < elements, numbers))
    center = [i for i in numbers if i == elements]
    right = list(filter(lambda x: x > elements, numbers))

    return quick_sort(left) + center + quick_sort(right)

def search_(spisok, rnd_):
    left = 0  # левая часть (первый элемент)
    right = len(spisok)-1  # правая часть (последний элемент)
    while right > left:
        middle = (right + left) // 2
        if numbers[middle] == rnd_:
            return f"{middle-1} - индекс элемента, который меньше введенного числа '{rnd_}'\n"\
                   f"{middle+1} - индекс элемента, который больше, либо равен введенному числу '{rnd_}'"
        elif spisok[left] == rnd_:
            if spisok[left] == spisok[0]:
                return f"Введенное число '{rnd_}' является наименьшим числом в списке, его индекс равен - {left}\n" \
                       f"{left+1} - индекс следующего элемента, который больше, либо равен введенному числу '{rnd_}'"
        elif spisok[right] == rnd_:
            if spisok[right] == spisok[-1]:
                return f"Введенное число '{rnd_}' является наибольшим числом в списке, его индекс равен - {right}\n" \
                       f"{right-1} - индекс предыдущего элемента, который меньше введенного числа '{rnd_}'"
        elif spisok[middle] > rnd_:
            if right == middle:
                return f"Введенное число '{rnd_}' находится между индексами {left} и {right}"
            right = middle
        else:
            if left == middle:
                return f"{left} - индекс элемента, который меньше введенного числа '{rnd_}'\n" \
                       f"{right} - индекс элемента, который больше, либо равен введенному числу '{rnd_}'"
            left = middle

while True:
    try:
        numbers = list(set(map(int, input("Введите последовательность чисел через пробел: ").split())))
        if len(numbers) <= 1:
            print()
            print("- - - " * 10)
            print('Ошибка !!! Вы не ввели последовательность, повторите ввод -')
            print("- - - " * 10)
            print()
            continue
        else:
            break
    except ValueError:
        print()
        print("- - " * 11)
        print("Вы ошиблись при вводе, попробуйте еще раз -")
        print("- - " * 11)
        print()
        continue

spisok = quick_sort(numbers)
print()

while True:
    try:
        rnd_ = int(input(f"Введите произвольное число в диапазоне от '{spisok[0]} до {spisok[-1]}': "))
        if rnd_ < spisok[0] or rnd_ > spisok[-1]:
            print()
            print("- - - - " * 10)
            print('Ошибка !!! Введенное число находится вне указанного диапазона, повторите ввод -')
            print("- - - - " * 10)
            print()
            continue
        else:
            break
    except ValueError:
        print()
        print("- - - - " * 8)
        print("Вы ошиблись при вводе произвольного числа, попробуйте еще раз -")
        print("- - - - " * 8)
        print()
        continue

print()
print(search_(spisok, rnd_))
print()
print('Выполнение программы завершено')