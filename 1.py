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
def save_repr(value):
    f = open( 'dump_repr.txt', 'w' )
    f.write(repr(value))
    f.close()

def load_repr():
    f = open( 'dump_repr.txt', 'r' )
    line = f.readline()
    f.close()
    return eval(line)
    # return list(map(int, line.strip("[]").split(", ")))

# save_repr(newlst)
# print(load_repr())


def save_plain(value):
    f = open( 'dump_plain.txt', 'w' )
    f.write(' '.join(map(str, value)))
    f.close()

def load_plain():
    f = open( 'dump_plain.txt', 'r' )
    line = f.readline()
    f.close()
    return map(int, line.split())

# save_plain(newlst)
# print(*load_plain())


class Example:
    z = 1
    def __init__(self):
        self.a = 0

o1 = Example()
o1.counter = 1
o1.type = 'something going on 1'
o2 = Example()
o2.id = 1
o2.type = 'something going on 2'
o3 = Example()
o3.oid = 1
o3.type = 'something going on 3'
o4 = Example()
o4.pid = 1
o4.type = 'something going on 4'

def print_o_v1(o):
    print("class attributes {0}".format(vars(o.__class__)))
    print("instance attributes {0}".format(vars(o)))
# print_o_v1(o1)


class vendor_material1:
    def __init__(self, id, price, quality, deliveries):
        self.id = id
        self.price = float(price)
        self.quality = float(quality)
        self.deliveries = deliveries
    def __del__(self):
        print("vendor material 1 with id={0} has been deleted".format(self.id))
    def get_quality(self):
        return self.quality
    def reliability(self):
        return 1 - sum(self.deliveries) / float(len(self.deliveries)) * 0.1
    def rating(self, max_price, values):
        return (1-self.price/float(max_price)) * values[0] + self.get_quality() * values[1] + (1-self.reliability()) * values[2]
    def cost(self, size):
        return self.price * size
    
    def __eq__(self, other):
        return self.rating(MAX_PRICE, VALUES) == other.rating(MAX_PRICE, VALUES)
    def __lt__(self, other):
        return self.rating(MAX_PRICE, VALUES) < other.rating(MAX_PRICE, VALUES)
    def __gt__(self, other):
        return self.rating(MAX_PRICE, VALUES) > other.rating(MAX_PRICE, VALUES)
    def __le__(self, other):
        return self.rating(MAX_PRICE, VALUES) <= other.rating(MAX_PRICE, VALUES)
    def __ge__(self, other):
        return self.rating(MAX_PRICE, VALUES) >= other.rating(MAX_PRICE, VALUES)
# vm1 = vendor_material1(1,80,0.1,[1,2,4,6,1,4])
# vm2 = vendor_material1(1,70,0.1,[1,2,4,6,1,4])
MAX_PRICE=100
VALUES=[0.4, 0.3, 0.3]
# print(vm1.reliability())
# print(vm1.rating(200, [0.1, 0.5, 0.4]))
# print(vm1 > vm2)

class vendor_material2(vendor_material1):
    def __init__(self, id, price, qualities, deliveries):
        self.qualities = qualities
        super().__init__(id, price, 0, deliveries)
    def get_quality(self):
        return sum(self.qualities) / float(len(self.qualities))
    def reliability(self):
        return 0.345
    def __str__(self):
        return vars(self)

# vm2_1 = vendor_material2(10, 100, [0.9, 0.7, 0.6, 0.9, 0.8], [1, 2, 0, 1, 1])
# print(vm1 > vm2_1)




def reverse_order(fn):
    def wrapper_function(*l):
        res = fn(*l)
        return res[::-1]
    return wrapper_function

# process 3 1
@reverse_order
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result

# print(transform([1, 2, 3, 4], [5, 6, 7, 8]))


import random
def random_of_list(list, n):
    num = 0
    while num < n:
        yield random.choice(list)
        num += 1
# for i in random_of_list([10, 20, 30, 40, 50, 60, 70, 80, 90], 10):
#     print(i)

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, l, step, limit):
        self.list = l
        self.step = step
        self.limit = limit
        self.counter = 0
        self.current_step = 0

    def __next__(self):
        if self.current_step < self.limit:
            if self.counter >= len(self.list):
                self.counter %= len(self.list)
            val = self.list[self.counter]
            self.counter += self.step
            self.current_step += 1;
            return val
        else:
            raise StopIteration

# for eggs in SimpleIterator([1,2,3], 2, 5):
#     print(eggs)




def get_clue(list1, list2):
    i = 0
    while i < len(list1) and i < len(list2):
        yield (list1[i], list2[i])
        i += 1

for c in get_clue([1, 2, 3], [4, 5, 6]):
    print(c)