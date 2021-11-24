# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functools import reduce
from itertools import count, cycle
from sys import argv
#№1
# script, output_in_hours, rate_per_hour, bonus = argv
#
# print("функция расчета заработной платы сотрудника ", script)
# print("выработка в часах ", output_in_hours)
# print("ставка в час ", rate_per_hour)
# print("Премия ", bonus)
# wage = (int(output_in_hours) * int(rate_per_hour)) + int(bonus)
# print("Ваша заработная плата ", wage)


#2
list_num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_num = [x for x, x1 in zip(list_num[1:], list_num[:-1]) if x > x1]
print(result_num)

#3
num_gen = [x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0]
print(num_gen)

#4
list_num1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_num1_result = [x for x in list_num1 if list_num1.count(x) < 2]
print(list_num1_result)


my_set = (el for el in range(5, 10))
print(*my_set)


dic_num = {x: x * 2 for x in range(50)}
print(dic_num)

#5

def sum(a, b):
    return a + b
list_num2 = [x for x in range(100, 1000)]
print(reduce(sum, list_num2))

#6
for i in count(3):
    if i == 11:
        break
    else:
        print(i)

for i in cycle([1, 2, 5, "ABC", 20]):
    if i == 20:
        break
    else:
        print(i)
#5
def fact(n):
    count = 1
    total = 1
    for i in range(n):
        total = total * count
        yield total
        count += 1

for i in fact(4):
    print(i)