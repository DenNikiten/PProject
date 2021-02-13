

my_str = ["word", 1, True, 40.5, None, b'text', ZeroDivisionError]
for el in my_str:
    print(f"Для элемента {el} тип {type(el)}")


my_list = list(input("Введите элементы в список: "))
print(my_list)
el = 0
for i in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print("Измененный список имеет вид ", my_list)


seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
seasons_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите месяц в виде числа: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Вы ввели не верное число!")

words = input("Введите слова: ")
new_line = words.split()
num = 1
for i in new_line:
    print(f"Для {num} слова: {i[:10]}")
    num += 1


my_list = [7, 5, 5, 5, 4, 3, 3, 2]
elem = int(input("Введите натуральное число: "))
num = 0
for i in my_list:
    if elem <= i:
        num += 1
my_list.insert(num, elem)
print(my_list)



task = ("Задание 6-ть со * не успел сделать(")
print(task)
answer = input("Введите причину: ")
if answer == ("У меня 12.02.2021 года был день рождение"):
    print("Это уважительная причина!")
    print("Мои позравления!)")
else:
    print("Это не уважительная причина!")
