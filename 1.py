# -*- coding: utf-8 -*-

import functools
import operator

def process1(matrix):
    # return map(lambda l: [len(l), len(l), list(max(enumerate(l), key=operator.itemgetter(1)))[::-1]], matrix)
    return map(lambda l: [len(l), len(l), [max(l), l.index(max(l))]], matrix)
# print (*process ([[1,2,3], [4,5,6], [7,8,9]]))

def process2(arg):
    if isinstance(arg, list):
        return tuple(arg)
    if isinstance(arg, tuple):
        return list(arg)
    return "functional is in development"
# print(process2([1,2,3]))
# print(process2((1,2,3)))
# print(process2(123))

from string import ascii_lowercase as asc_lower
def process3(arg):
    if isinstance(arg, str):
        diff = set(asc_lower) - set(arg)
        return len(diff) == 0, len(diff), sorted(diff)
    return "functional is in development"
# print(process3([1,2,3]))
# print(process3((1,2,3)))
# print(process3("The quick brown fox jumps over the lazy dog"))
# print(process3("The quick brown fox jumps over the"))


# process4
lst1 = [1,2,3,4,5,6,7,8,9,10] # входной список
newlst = [] # список-результат
averlst = [] # временный список средних значений
for (i, value) in enumerate(lst1):
    if i == 0:
        first = value # первый элемент списка сохраняем как first
    elif i > 0 and i < len(lst1) - 1:
        averlst.append(lst1[i]) # не первый и не последний элемент списка добавляем в массив averlst
    elif i == len(lst1) - 1:
        last = value # последний элемент списка сохраняем как last
newlst.append(first)
newlst.append(sum(averlst) / len(averlst)) # выводим среднее арифметическое от элементов списка averlst
newlst.append(last)
# print(newlst)

# import statistics
# def process4(l):
#     return l[0], statistics.mean(l[1:-1]), l[-1]
def process4(l):
    return l[0], sum(l[1:-1]) / float(len(l) - 2), l[-1]
# print(process4(lst1))

# process5
min_max = lambda l : [max(l), min(l)]
# print(*map(min_max, [[1,2,3,4,5]]))


# process 1 1
res = map(lambda i : i ** (1/4.0), [16, 81, 256])
# print(*res)

# process 1 2
def get_max(a, b): # зачем функцию писать то?
    # return max(a, b)
    return a if a > b else b
# print(functools.reduce(get_max, [1,5,7,1,3,2]))

# process 1 3
def logic(value):
    encounter = 0 # зачемто завели переменную со значением 0, в которую будет записываться необходимое изменение значения аргумента
    if value == 0: # если значение равно единице
        encounter += 1 # то увеличиваем переменную на единицу
        return value + encounter # а потом увеличиваем и значение аргумента на величину переменной
    elif value > 0: # аналогично предыдущему для чисел больше нуля
        encounter += 2 # увеличиваем переменную на 2
        return value + encounter # увеличиваем аргумент
    else: # аналогично предыдущему для чисел больше нуля
        encounter -= 1 # уменьшаем переменную
        return value + encounter # уменьшаем аргумент (прибавляем отрицательное значение)
lst = [-1, 10, 0, 12, 0, 0, 16, -2, 2, -3, -5, -6]
newlst = [logic(value) for value in lst]
# print(*newlst)
# print(*map(logic, lst))

def logic_fixed(value):
    if value == 0:
        return value + 1
    elif value > 0:
        return value + 2
    else:
        return value - 1
# print(*map(logic_fixed, lst))

def logic_fixed_2(value):
    return value + (value >= 0) + (value > 0) - (value < 0)
# print(*map(logic_fixed_2, lst))

# print(*map(lambda v: v + (v >= 0) + (v > 0) - (v < 0), lst))


# process 1 4
def save(value):
    f = open( 'dump.txt', 'w' )
    f.write(repr(newlst))
    f.close()

def load():
    f = open( 'dump.txt', 'r' )
    line = f.readline()
    f.close()
    return eval(line)

save(newlst)
print(load())
