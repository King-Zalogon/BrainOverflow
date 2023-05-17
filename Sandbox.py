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
# print(np.range(2,8))

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

# st = {'A', 'B', 'C'}
# st.clear( )
# print(st)

# print ("py" * 2 * 3)


# import timeit


# def is_palindrome_jr(string):
#     new_string = ""
#     for i in range(len(string)):
#         if string[i] != " ":
#             new_string += string[i]
#     string = new_string
#     for i in range(len(string)):
#         if string[i].lower() != string[len(string)-i-1].lower():
#             return False
#     return True
#
#
# print(is_palindrome_jr('ABC d cb a' * 1000))
#
#
# def is_palindrome_semisr(string):
#     string = string.replace(" ", "").lower()
#     return string == string[::-1]


# print(is_palindrome_semisr('ABC d cb a' * 1000))


# s = """Gur Mra bs Clguba, ol Gvz Crgref
# Ornhgvshy vf orggre guna htyl.
# Rkcyvpvg vf orggre guna vzcyvpvg.
# Fvzcyr vf orggre guna pbzcyrk.
# Pbzcyrk vf orggre guna pbzcyvpngrq.
# Syng vf orggre guna arfgrq.
# Fcnefr vf orggre guna qrafr.
# Ernqnovyvgl pbhagf.
# Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
# Nygubhtu cenpgvpnyvgl orngf chevgl.
# Reebef fubhyq arire cnff fvyragyl.
# Hayrff rkcyvpvgyl fvyraprq.
# Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
# Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
# Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
# Abj vf orggre guna arire.
# Nygubhtu arire vf bsgra orggre guna *evtug* abj.
# Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
# Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
# Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
#
# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)
#
# print("".join([d.get(c, c) for c in s]))


# def is_palindrome_semisr(str):
#     str = str.replace(" ", "").lower()
#     return str == str[::-1]
#
#
# print(is_palindrome_semisr('ABC d cb a' * 1000))
#
# def is_palindrome_sr(text: str) -> bool:
#     text = text.replace(" ", "").lower()
#     return text == text[::-1]
#
# print(is_palindrome_sr('ABC d cb a' * 1000))

# s = "name"
# print(s.zfill(6))


# def isPalindrome(s):
#
#     def toChars(s):
#         s = s.lower()
#         ans = ""
#         for c in s:
#             if c in "abcdefghijklmnñopqrstuvwxyz":
#                 ans = ans + c
#             return ans
#
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#     return isPal(toChars(s))
#
#
# print(isPalindrome("ABC d cb a"*1000))

# d = {2: 30, 1: 10, 3: 30, 1: 40}
# print(d)

# new_list = [1, "John", 4]
# print(new_list[3:])

# s = "stalwart"
# print(s.partition("a"))


# lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# temp = [num for sublist in lst for num in sublist]
# print(temp)
#
# print(12 - (2 < 12) * 7)

# a = 00
# print(list(str(a)))

# import math
#
# print(math.trunc(3.1))

# some_var = "1"
# print(bool(some_var))
#
# target_num = int(input("Ingresa un número del 1 al 50: "))
# my_list = []
#
# for i in range(1, target_num+1):
#     my_list.append(i)
#
# print(f'Mi lista va del {my_list[0]} al {my_list[-1]}.')
# result = 0
# for i in my_list:
#     result += i
#
# print(f'Y sumar cada uno de los elementos de mi lista me da {result} como resultado')

#Se requiere de un algoritmo que permita el ingreso de 10 notas numericas de alumnos
# y muestre un array con las calificaciones concpetuales
#10: LS logros sobresalientes
#9-8: LSat logros satisfactorios
#7-6: LB logros basicos
#<5 LNO logros no obtenidos

# mis_notas = []
#
# calificaciones = ["LNO logros no obtenidos", "LB logros basicos", "LSat logros satisfactorios", "LS logros sobresalientes"]
#
# for i in range(10):
#
#     nota = int(input("Ingrese un numero entre 1 y 10: "))
#
#     while nota < 1 or nota > 10:
#         print("El numero ingresado debe estar entre 1 y 10.")
#         nota = int(input("Ingrese un numero entre 1 y 10: "))
#
#     mis_notas.append(nota)
#
# print(mis_notas)
#
# mis_calificaciones = []
#
# for i in mis_notas:
#     num = (i // 2)-1
#     if num > 0:
#         mis_calificaciones.append(calificaciones[num-1])
#     else:
#         mis_calificaciones.append(calificaciones[0])
#
# print(mis_calificaciones)




