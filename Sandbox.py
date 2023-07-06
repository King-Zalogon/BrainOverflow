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

# Se requiere de un algoritmo que permita el ingreso de 10 notas numericas de alumnos
# y muestre un array con las calificaciones concpetuales
# 10: LS logros sobresalientes
# 9-8: LSat logros satisfactorios
# 7-6: LB logros basicos
# <5 LNO logros no obtenidos

# mis_notas = []
#
# calificaciones = [
# "LNO logros no obtenidos", "LB logros basicos",
# "LSat logros satisfactorios", "LS logros sobresalientes"
# ]
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

# import asyncio
#
# async def wait_4_it():
#     await asyncio.sleep(0.5)
#     print("It's gonna be LEGEN...")
#     await asyncio.sleep(0.8)
#     print('... wait for it..')
#     await asyncio.sleep(1.2)
#     print('... DARY!!!')
#     await asyncio.sleep(1)
#
# asyncio.run(wait_4_it())

# def draw_random_circles(canvas):
#     # TO DO your code here
#     pass
#
# from tkinter import Canvas
#
# CANVAS_WIDTH = 300
# CANVAS_HEIGHT = 300
# CIRCLE_SIZE = 20
# N_CIRCLES = 20
#
# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     # TO DO your code here
#
#
#
# def random_color():
#     colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
#     return random.choice(colors)
#
# canvas.create_rectangle(0, 0, 40, 40, random_color())

# CONSTANT_LIST = [1, 2, 3]
# CONSTANT_LIST.append(4)
# print(CONSTANT_LIST)

# from graphics import Canvas
# import random
#
# CANVAS_WIDTH = 300
# CANVAS_HEIGHT = 300
# CIRCLE_SIZE = 20
# N_CIRCLES = 20
#
#
# def main():
#     print('Random Circles')
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#
#     for i in range(N_CIRCLES):
#         e = random.randint(1, 10)
#         if e % 2 == 0:
#             draw_random_circles(canvas)
#         else:
#             draw_random_rectangle(canvas)
#
#
# def random_color():
#     """
#     This is a function to use to get a random color for each circle. We have
#     defined this for you and there is no need to edit code in this function,
#     but feel free to read it over if you are interested.
#     """
#     colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen', 'red', 'green', 'yellow', 'orange']
#     return random.choice(colors)
#
#
# def draw_random_circles(canvas):
#     # left_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
#     # top_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
#     # right_x = left_x + CIRCLE_SIZE
#     # bottom_y = top_y + CIRCLE_SIZE
#     random_size = random.randint(15, 40)
#     left_x = random.randint(0, CANVAS_WIDTH - random_size)
#     top_y = random.randint(0, CANVAS_HEIGHT - random_size)
#     right_x = left_x + random_size
#     bottom_y = top_y + random_size
#     random.randint(15, 40)
#
#     canvas.create_oval(left_x, top_y, right_x, bottom_y, random_color())
#
#
# def draw_random_rectangle(canvas):
#     random_size = random.randint(15, 40)
#     left_x = random.randint(0, CANVAS_WIDTH - random_size)
#     top_y = random.randint(0, CANVAS_HEIGHT - random_size)
#     right_x = left_x + random_size
#     bottom_y = top_y + random_size
#     random.randint(15, 40)
#
#     canvas.create_rectangle(left_x, top_y, right_x, bottom_y, random_color())
#
#
# if __name__ == '__main__':
#     main()

# def is_valid(s):
#     stack = []
#     brackets = {'(': ')', '[': ']', '{': '}'}
#
#     for char in s:
#         if char in brackets.keys():
#             stack.append(char)
#         elif char in brackets.values():
#             if len(stack) == 0 or brackets[stack.pop()] != char:
#                 return False
#
#     return len(stack) == 0


# def is_valid(s):
#     stack = []
#     brackets_map = {')': '(', ']': '[', '}': '{'}
#
#     for char in s:
#         if char in ['(', '[', '{']:
#             stack.append(char)
#         elif char in [')', ']', '}']:
#             if not stack or brackets_map[char] != stack.pop():
#                 return False
#
#     return len(stack) == 0
#
# # Test cases
# print(is_valid("()"))  # Output: True
# print(is_valid("()[]{}"))  # Output: True
# print(is_valid("(]"))  # Output: False
# print(is_valid("([)]"))  # Output: False
# print(is_valid("{[]}"))  # Output: True
# print(is_valid("()[]{}"))

# def solution(k: list[int]) -> int:
#     max_diff = float('-inf')
#
#     for i in range(len(k)):
#         for j in range(i + 1, len(k)):
#             for m in range(len(k)):
#                 for n in range(m + 1, len(k)):
#                     diff = (k[i] * k[j]) - (k[m] * k[n])
#                     max_diff = max(max_diff, diff)
#
#     return max_diff
#
#
# k = [3,2,1,4,5,6]
#
# print(solution(k))


# from typing import List
#
# def solution(s: str, k: List[int]) -> str:
#     sorted_string = [''] * len(s)  # Create a list to store the characters in their sorted positions
#
#     for i in range(len(s)):
#         sorted_string[k[i]] = s[i]  # Move the character to its sorted position
#
#     return ''.join(sorted_string)  # Convert the list back to a string
#
#
# s = "talentcloudturing"
# k = [6,7,8,9,10,11,12,13,14,15,16,0,1,2,3,4,5]


# R E A D M E
# DO NOT CHANGE the code below, we use it to grade your submission.
# If changed your submission will be failed automatically.
# if __name__ == '__main__':
#     s = input()
#     line = input()
#     k = line.strip().split()
#     k = [int(x) for x in k]
#     output = solution(s, k)
#     print(output)

# output = solution(s, k)
# print(output)
#
# import random
#
#
# def main():
#     print("Khansole Academy")
#
#     # TO DO: your code here
#     def my_ints():
#         a = random.randint(10, 100)
#         b = random.randint(10, 100)
#         return (a, b)
#
#     my_sum = my_ints()
#     correct = my_sum[0] + my_sum[1]
#
#     print(f'What is {my_sum[0]} + {my_sum[1]}?')
#
#     answer = int(input('Your answer: '))
#
#     if answer == correct:
#         print('Correct!')
#     else:
#         print('Incorrect.')
#         print(f'The expected answer is {correct}')

#
# def presentar(nombre, edad, team_invierno):
#     saludo = 'Hola, mi nombre es ' + nombre
#     dias_vida = edad * 365
#
#     if team_invierno:
#         team = 'frío!'
#     else:
#         team = 'calor!'
#     clima = 'Amo cagarme de ' + team
#
#     print(saludo, '\nLlevo con vida más de', dias_vida, ' días\nY', clima)
#
#
# presentar("Gonzalo", 40, False)
#
# presentar(team_invierno=True, nombre='Loana', edad=24)


# for i in range(20, 0, -1):
#     print(i)

# try:
#     with open('test_file.txt', 'w') as f:
#         f.write('Create a new text file!')
# except FileNotFoundError:
#     print("The directory does not exist")


# numbers = [1, 2, 3, 4]


# def double_numbers(list):
#     for i in range(len(list)):
#         list[i] = list[i] * 2
#
#
# double_numbers(numbers)
#
# print(numbers)

# def add_many_numbers(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
#
#
# numbers = [1, 2, 3, 4, 5]
# sum_of_numbers = add_many_numbers(numbers)
# print(sum_of_numbers)

# my_dict = {
#     1 : 'Tom',
#     2 : 32,
#     3 : True
# }
#
# for item in my_dict.items():
#     print(type(item[1]))

# """
# This program counts the number of times each number appears in a list of numbers.
# """
#
#
# def get_user_numbers():
#     """
#     Create an empty list.
#     Ask the user to input numbers and store them in a list.
#     Once they enter a blank line, break out of the loop and return the list.
#     """
#     user_numbers = []
#     while True:
#         user_input = input("Enter a number: ")
#
#         # If the user enters a blank line, break out of the loop and stop asking for input
#         if user_input == "":
#             break
#
#         # convert the user input to an integer and add it to the list
#         num = int(user_input)
#         user_numbers.append(num)
#
#     return user_numbers
#
#
# def count_nums(num_lst):
#     """
#     Create an empty dictionary.
#     Loop over the list of numbers.
#     If the number is not in the dictionary, add it as a key with a value of 1.
#     If the number is in the dictionary, increment its value by 1.
#     """
#     num_dict = {}
#     for num in num_lst:
#         if num not in num_dict:
#             num_dict[num] = 1
#         else:
#             num_dict[num] += 1
#
#     return num_dict
#
#
# def print_counts(num_dict):
#     """
#     Loop over the dictionary and print out each key and its value.
#     """
#     for num in num_dict:
#         print(str(num) + " appears " + str(num_dict[num]) + " times.")
#
#
# def main():
#     """
#     Ask the user to input numbers and store them in a list. Once they enter a blank line,
#     print out the number of times each number appeared in the list.
#     """
#     user_numbers = get_user_numbers()
#     num_dict = count_nums(user_numbers)
#     print_counts(num_dict)


# """
# Program to show an example of using dictionaries to maintain
# a phonebook.
# """
#
#
# def read_phone_numbers():
#     """
#     Ask the user for names/numbers to story in a phonebook (dictionary).
#     Returns the phonebook.
#     """
#     phonebook = {}                   # Create empty phonebook
#
#     while True:
#         name = input("Name: ")
#         if name == "":
#             break
#         number = input("Number: ")
#         phonebook[name] = number
#
#     return phonebook
#
#
# def print_phonebook(phonebook):
#     """
#     Prints out all the names/numbers in the phonebook.
#     """
#     for name in phonebook:
#         print(str(name) + " -> " + str(phonebook[name]))
#
#
# def lookup_numbers(phonebook):
#     """
#     Allow the user to lookup phone numbers in the phonebook
#     by looking up the number associated with a name.
#     """
#     while True:
#         name = input("Enter name to lookup: ")
#         if name == "":
#             break
#         if name not in phonebook:
#             print(name + " is not in the phonebook")
#         else:
#             print(phonebook[name])
#
#
# def main():
#     phonebook = read_phone_numbers()
#     print_phonebook(phonebook)
#     lookup_numbers(phonebook)

# import random
#
# # Name of the file to read in!
# FILE_NAME = 'cswords.txt'
#
# def get_words_from_file():
#     """
#     This function has been implemented for you. It opens a file,
#     and stores all of the lines into a list of strings.
#     It returns a list of all lines in the file.
#     """
#     f = open(FILE_NAME, mode='r')
#     lines = []
#     for line in f:
#         # removes whitespace characters (\n) from the start and end of the line
#         line = line.strip()
#         # if the line was only whitespace characters, skip it
#         if line != "":
#             lines.append(line)
#     return lines
#
#
# def main():
#
#     words_list = get_words_from_file()
#     while True:
#         print(random.choice(words_list))
#         if input() != '':
#             break

# with open('test_file.txt', 'r', encoding='utf8') as f:
#     lines = []
#     for line in f:
#         lines.append(line.strip())
#
#
# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'a') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')
#
# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'a') as f:
#     f.writelines(lines)
#
# more_lines = ['', 'Append text files', 'The End']
#
# with open('readme.txt', 'a') as f:
#     f.write('\n'.join(more_lines))
#
# f.close()
#
#
# def solution(queries):
#     container = []
#     answers = []
#
#     for query in queries:
#         operation = query[0]
#         value = query[1]
#
#         if operation == "ADD":
#             container.append(value)
#             answers.append("")
#         elif operation == "EXISTS":
#             count = container.count(value)
#             if count > 0:
#                 for i in range(0, count):
#                     answers.append("true")
#             else:
#                 answers.append("false")
#         elif operation == "REMOVE":
#             if value in container:
#                 container.remove(value)
#
#     return answers
#
#
# def solution(queries):
#     accounts = {}
#     results = []
#
#     for query in queries:
#         operation = query[0]
#         timestamp = query[1]
#         account_id = query[2]
#
#         if operation == "CREATE_ACCOUNT":
#             if account_id not in accounts:
#                 accounts[account_id] = [0, []]
#                 results.append("true")
#             else:
#                 results.append("false")
#
#         elif operation == "DEPOSIT":
#             if account_id in accounts:
#                 amount = int(query[3])
#                 accounts[account_id][0] += amount
#                 results.append(str(accounts[account_id][0]))
#             else:
#                 results.append("")
#
#         elif operation == "PAY":
#             if account_id in accounts:
#                 amount = int(query[3])
#                 if accounts[account_id][0] >= amount:
#                     accounts[account_id][0] -= amount
#                     results.append(str(accounts[account_id][0]))
#                 else:
#                     results.append("")
#             else:
#                 results.append("")
#
#     return results
#
#
# def solution(queries):
#     accounts = {}
#     transaction_values = []
#     results = []
#
#     for query in queries:
#         operation = query[0]
#         timestamp = query[1]
#         account_id = query[2]
#
#         if operation == "CREATE_ACCOUNT":
#             if account_id not in accounts:
#                 accounts[account_id] = [0, []]
#                 transaction_values.append((0, account_id))
#                 results.append("true")
#             else:
#                 results.append("false")
#
#         elif operation == "DEPOSIT":
#             if account_id in accounts:
#                 amount = int(query[3])
#                 accounts[account_id][0] += amount
#                 results.append(str(accounts[account_id][0]))
#                 # Update the total transaction value for the account
#                 index = transaction_values.index((accounts[account_id][0] - amount, account_id))
#                 transaction_values[index] = (accounts[account_id][0], account_id)
#             else:
#                 results.append("")
#
#         elif operation == "PAY":
#             if account_id in accounts:
#                 amount = int(query[3])
#                 if accounts[account_id][0] >= amount:
#                     accounts[account_id][0] -= amount
#                     results.append(str(accounts[account_id][0]))
#                     # Update the total transaction value for the account
#                     index = transaction_values.index((accounts[account_id][0] + amount, account_id))
#                     transaction_values[index] = (accounts[account_id][0], account_id)
#                 else:
#                     results.append("")
#             else:
#                 results.append("")
#
#         elif operation == "TOP_ACTIVITY":
#             n = int(query[2])
#             top_accounts = []
#             for i in range(min(n, len(transaction_values))):
#                 account = transaction_values[i]
#                 top_accounts.append(f"{account[1]}({account[0]})")
#             results.append(", ".join(top_accounts))
#
#     return results
# import  datetime
# print(type(datetime.date(2012, 1, 1) - datetime.date(2011, 1, 1)))
# print(datetime.date(2023, 1, 1) - datetime.date(2000, 1, 1))

# def test(i,j):
#   if i == 0:
#     return j
#   else:
#     return test(i-1,i+j)
#
# print(test(4,7))

# print({x for x in range(100) if x%3 == 0})

# number_list = [x for x in range(100) if x%3 if x%5]
# print(number_list)

# print '{0:-2%}'.format(1.0 / 3)

# i = 0
# while i < 3:
#   print(i)
#   i += 1
#   print(i+1)

# def print_alpha_nums(abc_list, num_list):
#     for char in abc_list:
#         for num in num_list:
#             print(char, num)
#     return
#
# print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])


# if bool(1):
#     print("Foo")

# a, b, c, d = {"foo": 4}, {"que": {"bar": 6}, "make": 6}, "all", "5"
# print(c)

nota1 = float(input("Ingrese nota del primer parcial: "))
nota2 = float(input("Ingrese nota del segundo parcial: "))
recu = input("Rendiste recuperatorio de alguno de los parciales? Y/N: ").lower()

promedio = (nota1 + nota2) / 2
tema_final = 0
temas = ["una pregunta fácil para simular que te tomó final", "un examen principalmente apuntado al parcial que no hayas aprobado"]

if nota1 < 7 or nota2 < 7 or recu == 'y':
    tema_final = 1
    if promedio > 7:
        promedio = 6

resultado = f"Como te sacaste {nota1} y {nota2} el día del final tenés que ir y te va a tomar {temas[tema_final]} porque tu promedio da {promedio}"
print(resultado)