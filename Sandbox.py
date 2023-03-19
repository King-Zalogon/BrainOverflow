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

nums = [10, 20, 30]
temp = nums
nums.append(temp)
print(nums)
