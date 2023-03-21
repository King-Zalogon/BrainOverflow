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


list1= {22, 35, 51}
list1.add((5,1))
list2 = {4,51,5,1}
list2.intersection_update(list1)
print(list2)

