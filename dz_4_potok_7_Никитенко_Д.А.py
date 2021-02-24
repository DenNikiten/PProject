#1
from sys import argv

def salary(time, stavka, premia):
    try:
        return time * stavka + premia
    except ValueError as err:
       print("Error: ", err)

print(f"Salary - {salary(*map(int, argv[1:]))}")
# По вашему разбору dz разбираюсь.

#2
from random import randint

nums = [randint(30, 100) for i in range(12)]
print(nums)
new_nums = [el for i, el in enumerate(nums) if nums[i] > nums[i - 1]]
print(new_nums)

#3
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

#4
nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 25, 66, 33, 66]
print(nums)
new_nums = [el for el in nums if nums.count(el) == 1]
print(new_nums)

#5
from functools import reduce

def my_func(a, b):
    return a * b

a = [el for el in range(100, 1001) if el % 2 == 0]
print(a)

res = reduce(my_func, a)
print(f"Результат вычисления произведения всех элементов списка a равен: {res}")

#6
from itertools import cycle, count
from time import sleep

for el in count(3):
    sleep(.5)
    if el > 10:
        break
    else:
        print(el)

a = [0, 1, 2, 3]
c = 1
for el in cycle(a):
    if c > 8:
        break
    sleep(.5)
    print(el)
    c += 1

#7

def generator(num):
    f_gen = 1
    for i in range(1, num + 1):
        f_gen *= i
        yield f_gen

for el in generator(9):
    print(el)





