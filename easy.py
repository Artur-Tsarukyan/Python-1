import random


__author__ = 'Царукян Артур'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
#           постарайтесь решить задачу с применением арифметики и цикла while;
#           при желании решите задачу с применением цикла for.

get_random_number = str(random.randint(0, 1000))
print(get_random_number)
python_number = list(get_random_number)
each_symbol = python_number
for number in each_symbol:
    print(number)
print("Процесс завершен!")



# Задача-2: Иходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
#           постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

first_number = input("Пожалуйста, введите данную №1: ")
second_number = input("Пожалуйста, введите данную №2: ")

hidden_element = second_number
second_number = first_number
first_number = hidden_element

print(first_number)
print(second_number)



# # Задача-3: Запросите у пользователя его возраст.
# # Если ему есть 18 лет, выведите: "Доступ разрешен",
# # иначе "Извините, пользование данным ресурсом только с 18 лет"

user_age = int(input("Пожалуйста, введите год Вашего рождения числами: "))
if 2019 - user_age < 18:
    print("Извините, пользование данным ресурсом только с 18 лет!")
else:
    print("Доступ разрешен!")