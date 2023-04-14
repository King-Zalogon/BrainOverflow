# print(round(4.650))
# def fun_x(x):
#     x=x+'2'
#     x=x*2
#     return x
# print(fun_x('python'))
# list1 =[1,1,2,2,3,2,1,2,4,4,5,5,5,5,5,5,1,2]
#
# print(sorted(list(set(list1)),reverse=True))
#
# print(list(set(list1)).sort())
# print(sorted(list(set(list1)), reverse=False))

# i = 1
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 1

# import pytest
#
# @pytest.fixture
# def number():
#     num = 5
#     return num
#
# @pytest.fixture
# def multiplication(number):
#     num = 5 * number
#     return num
#
# def test_multiplication_with_fixtures(multiplication):
#     assert multiplication == 25

# nums = [10, 20, 30]
# temp = nums
# nums.append(temp)
# print(nums)

# s = "1234"
# print(list(s))

# def func(x):
#     x[0] = 'def'
#     x[1] = 'abc'
#     return id(x)
#
#
# q = ['abc', 'def']
# print(id(q) == func(q))

# a_set = set()
#
# print(a_set)
# print(type(a_set))


# list1= {22, 35, 51}
# list1.add((5,1))
# list2 = {4,51,5,1}
# list2.intersection_update(list1)
# print(list2)

# fruits = ['apple', 'banana', 'cherry']
# print(len(fruits))

# def multiplier(y):
#     return lambda x: x * y
# f = multiplier(2)
# print(f(False))
# print(f(True))
# print(f(3))

# st = 'wxy'
# print('z'.join(st))

# x = [10, 20, 30]
# print(x.append(40))

# a = "aaa" > "b"
# b = isinstance(int, type)
# c = bool(0)
# d = bool([])
#
# result = f"{str(a)},{str(b)},{str(c)},{str(d)}"
#
# print(result)


# LIST=[1, 2, 3, 4]
# print(list(map(lambda x:x*2, LIST)))

# list1=[12,47,87,41]
# list2=["1","2","3","4"]
#
# data ={key:value for key,value in zip(list1,list2) if 12<int(key)<50}
#
# print(sum(data.keys()))


# for i in range(10):
#
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")

# x = [1, 2, 3, 4]
# print(x.pop(3))


# n = 3
# for i in range(1, n+1):
#     print((10**i // 9) * i)

# x = "x"
#
# print(ord(x))

# numbers = [str((x+1)*2) for x in range(0,10,2) if x > 5]
#
# print("".join(numbers))

# list = [1,1,2,3,5,8,13]
# print(list[list[4]])

# for i in range(10):
#     if not i % 2 == 0:
#         print(i+1)

# list = [1,2,3]
# for var in list:
#     print(var)

# x = [6, 4, 2, 9]
# x = x[::-1]
# print(x[0]+x[2])

# N = int(input())
# total = 0
# for i in range(1,N+1):
#     total += i
# print(total)

# def f(*args):
#     return sum(args)
# print(f(1, 2, 3, 4, 5))


# tpl = (1,2,3,4,5)
# print(tpl.count(3) + tpl.index(3))

# import numpy as np
# print(np.arange(2,8))

# li = [10, 15, 20, 25]
# li[1:3] = [30]
# print(li)

# list1 = [1, 3, 5]
# set1 = {5, 1, 6, 8}
#
# set1 |= set(list1)
# print(set1)

# tpl = (1,2,3,4,5)
# print(tpl.index(3, 2, 4))

# lst = [1, 2, 3, 4, 5, 2, 3, 4, 5]
# print(len(set(lst)))

# import math
# print(math.fsum([.1 for i in range(20)]))

# li = [10, 20, 30, 20]
# li.remove(20)
# print(li)

st = {'A', 'B', 'C'}
st.clear( )
print(st)

