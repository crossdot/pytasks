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
print(process4(lst1))

# process5
print(*map(lambda l: [max(l), min(l)], [[1,2,3,4,5]]))