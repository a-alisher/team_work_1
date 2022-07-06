
# Задание 1:
    # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
    # 1. У пользователя просят выбрать знак
    # 2. Просят ввести 1-ое число
    # 3. Просят ввести 2-ое число
    # 4. Вывести результат
    # 5. После результата спросить у пользователя хочет он закончить или нет,
    # если нет то калькулятор должен запускатся сначала
    # 6. Учесть то что деление на ноль невозможно
while True:
    first_sign = (input('Please choose sign: +, - , *, / '))
    if first_sign == '0':
        break
    first_number = float(input('Enter first number '))
    second_number = float(input('Enter second number '))
    if first_sign == '+':
        print(first_number + second_number)
    elif first_sign == "-":
        print(first_number - second_number)
    elif first_sign == '*':
        print(first_number * second_number)
    elif first_sign == '/':
        if second_number == 0:
            print('Делить на ноль нельзя!')
        else:
            print(first_number / second_number)
    else:
        print('Неверно')
    answer = input('Хотите продолжить? Да или нет ')
    if answer == 'Да':
        continue
    else:
        break


# Задание 2:
    # Даны три переменные "A", "B" и "C".
    # Изменить значения этих переменных так, /Users/alisheralimkanov/Downloads/Test2.txtчтобы в "A" хранилось значение "A"+"B",
    # в "B" хранилась разность старых значений "C" - "A",
    # а в "C" хранилось сумма старых значений "A" + "B" + "C".
    # Например, A=0, B=2, C=5, тогда новые значения A=2, B=5 и C=7.

A = float(input('Введите число '))
B = float(input('Введите число '))
C = float(input('Введите число '))
for x in range(1):
    A = A + B
    B = C - A
    C = A + B + C
print(A, B, C)


# Задание 3:
    # Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.
side = float(input('Введите сторону квадрата '))
p = 4 * side
s = side**2
print(p, s)

# Задание 4:
    # Вам даны несколько последовательностей чисел:
    # sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
    # sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
    # sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
    # sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

    # Нужно проверить, все ли числа в КАЖДОЙ последовательности уникальны.
    # Если в последовательности были найдены дубликаты ---> Выведите на экран: "Последовательность не уникальна."
    # Если в последовательности дубликатов найдено не было ---> Выведите на экран: "Последовательность уникальна."
    # Если в решении задания не присутствует цикл ---> Задание не защитано.

sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
for x in range(1):
    setarr = set(sequence_0)
    if len(sequence_0) == len(setarr):
        print('Последовательность уникальна')
    else:
        print('Последовательность не уникальна')
    setarr_1 = set(sequence_1)
    if len(sequence_1) == len(setarr_1):
        print('Последовательность уникальна')
    else:
        print('Последовательность не уникальна')
    setarr_2 = set(sequence_2)
    if len(sequence_2) == len(setarr_2):
        print('Последовательность уникальна')
    else:
        print('Последовательность не уникальна')
    setarr_3 = set(sequence_3)
    if len(sequence_3) == len(setarr_3):
        print('Последовательность уникальна')
    else:
        print('Последовательность не уникальна')


# Задание 5:
    # Создайте input и спросите у пользоваетля как работает встроенная функция reversed().
    # В терминале пользователя должен ввести пример функции reversed() и отправить это вашей программе.
    # Ваша программа должна исполнить ту часть кода которую ввёл пользователь и вывести на экран результат.
    # Если пользователь ввёл что-то не по синтаксису Python поймайте это с помощью try: except:
    # Если пользователь всё ввёл верно выполните его программу.
    # Если поймали ошибку ---> Спросите снова как работает встроенная функция reversed().

# user_answer = input('enter  function reversed ')
#
# print(user_answer



# Задание 6:
#     Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию?
#     Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.


number = input("Введите четыреххначное число: ")
# for x in range(1):
number = list(str(4000))
if number[0] > number [1] > number[2] > number[3]:
    print('Да')
else:
    print('Нет')
