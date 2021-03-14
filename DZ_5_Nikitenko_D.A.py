#1
out_f = open("1_out_file.txt", "w")
while True:
    str_list = f"{input('Введите слова: ')}\n"
    if str_list == "\n":
        break
    out_f.writelines(str_list)
out_f.close()

#2
my_file = open("2_out_file.txt", "r")
line = my_file.readlines()
print(f'Количество строк в файле - {len(line)}')
for el in range(len(line)):
    print(f'Количество слов {el + 1} - ой строки - {len(line[el])}')
my_file.close()

#3
from statistics import mean

salaries = []
with open('3_out_file.txt', 'r') as my_f:
    line = my_f.readlines()
    for el in line:
        surname, salary = line.split(" ")
        salary = int(salary)
        salaries.append(salary)
        if salary < 20000:
            print(surname)
    print(mean(salaries))

#4
dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open('4_1_out_file.txt', 'r') as my_f:
        line = my_f.readlines()
        print(line)
with open('4_2_out_file.txt', 'w') as new_my_f:
    for el in line:
        num_list = el.split(' — ')
        new_my_f.write(f'{dict[num_list[0]]} - {num_list[1]}')

#5
with open('5_out_file.txt', 'w') as my_f:
    str_list = input('Введите числа через пробел: ')
    my_f.write(str_list)
with open('5_out_file.txt', 'r') as my_f:
    line = my_f.readline()
    my_numb = line.split()
    print(sum(map(int, my_numb)))

#6
my_dict = {}
with open('6_out_file.txt', 'r') as my_f:
    for el in my_f:
        obj, lessons = el.split(':')
        sum_obj = sum(map(int, ''.join([i for i in lessons if i == ' ' or i.isdigit()]).split()))
        my_dict[obj] = sum_obj
print(my_dict)

#7
Разбираюсь с задачей. Сложно еще для понимания(


