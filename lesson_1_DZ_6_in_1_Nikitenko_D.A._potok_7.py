# answer1 = int(input("Введите первое число: "))
# answer2 = int(input("Введите второе число: "))
# print("Первое число ", answer1)
# print("Второе число ", answer2)


# s = int(input("Введите время в секундах: "))
# sec = f"Время в формате чч:мм:сс - {int(s / 3600)}:{int((s / 60) % 60)}:{int(s % 60)}"
# print(sec)


# n = int(input("Ведите число: "))
# num = str(n)
# n2 = num + num
# n3 = num + num + num
# sum = n + int(n2) + int(n3)
# print(sum)


# num = int(input("Введите целое положительное число: "))
# max = num % 10
# num = num // 10
# while num > 0:
#     if num % 10 > max:
#         max = num % 10
#     num //= 10
# print("Самая большая цифра в числе равна", max)


# rev = int(input("Введите выручку фирмы: "))
# cost = int(input("Введите издержки фирмы: "))
# if rev > cost:
#     a = rev - cost
#     print("Прибыль фирмы равна", a)
#     prof = (a / rev) * 100
#     print("Рентабельность равна", int(prof), "%")
#     q = int(input("Введите численность сотрудников фирмы "))
#     print("Прибыль фирмы в расчете на одного сотрудника равна", int(a / q))
# else:
#     print("Фирма в убытке!")


# a = int(input("Введите количество километров, которые спортсмен пробежал в первый день: "))
# b = int(input("Введите общее количество километров, которые пробежал спортсмен за все время: "))
# day = 1
# result = a
# while result < b:
#         a = a + 0.1 * a
#         result += a
#         day += 1
# print("На", day, "день спортсмен пробежит", b, "километров")
