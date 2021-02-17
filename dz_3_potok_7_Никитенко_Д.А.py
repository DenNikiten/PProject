
# 1
def my_func(a, b):
    if b == 0:
        print("На ноль делить нельзя!")
    return a // b
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(my_func(a, b))

# 2
def my_func(var_1, var_2, var_3, var_4, var_5, var_6):
    print(f"Имя - {var_1}, Фамилия - {var_2}, {var_3} года рождения, Проживаю в - {var_4}, E-mail - {var_5}, Телефон - {var_6}")
name = input("Введите ваше имя: ")
soname = input("Введите вашу фамилию: ")
year_of_birth = input("Введите ваш год рождения: ")
city_of_res = input("Введите ваш город проживания: ")
e_mail = input("Введите ваш e-mail: ")
tel = input("Введите ваш телефон: ")
my_func(var_1=name, var_2=soname, var_3=year_of_birth, var_4=city_of_res, var_5=e_mail, var_6=tel)

# 3
def my_func(a, b, c):
    k = [a, b, c]
    k.remove(min(k))
    print(sum(k))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
my_func(a, b, c)

# 4
def my_func(x, y):
    return 1 / (x ** y)
x = float(input("Введите число x: "))
y = int(input("Введите число y: "))
print(my_func(x, y))

def my_func(x, y):
    z = 1
    for i in range(y):
        z *= x
    return 1 / z
x = float(input("Введите число x: "))
y = int(input("Введите число y: "))
print(my_func(x, y))

# 5
# Не разобрался с заданием. Постараюсь понять задание в вашем разборе на Youtube.com.

# 6
def int_func(*args):
    return args
words = input("Введите слова:")
print(words.title())

