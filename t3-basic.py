# datatype: int, float, list,

price = 100
print(price)

tax = 0.25
print(tax)

# The string is enclosed in double quotes if the string contains a single quote and no double quotes,
# otherwise it is enclosed in single quotes.

name1 = "terry1"
print(name1)

name2 = 'terry2'
print(name2)

x1 = [1, 2, 3, 4, 5]
print(x1)
print("first line", x1[0], "last one", x1[-1], x1[len(x1) -1])


# control flow

# i1 = int(input("Pls input a number"))
i1 = 100
if i1 < 0:
    print("negative")
elif i1 == 0:
    print("zero")
else:
    print("positive")


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for i in range(10):
    if (i % 2 == 1):
        print(i)
    else:
        continue

print("Fibonacci")
a, b = 0, 1
while b < 20:
    print(a, end = ',')
    a, b = b, a + b
print()

# function

def fib(n):
    print("calling fib()")
    a, b = 0, 1
    while b < n:
        print(a, end = ',')
        a, b = b, a + b
    print()

fib(20)

def concat(sep, *args):
    return sep.join(args)

print(concat("/", "abc", "def"))
print(concat("\\", "abc", "def", "ghi"))

# input, Output
# x1 = input("Pls input your name: ")
# i1 = int(input("Pls input your phone number: "))
# print(x1, i1)

# DATA STRUCTURES
# - List, String: sequence
# - Tuple: sequence
# {
# Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples
# are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing)
# Lists are mutable, and their elements
# are usually homogeneous and are accessed by iterating over the list.
# }
t = (12345, 54321, 'hello!')
print(t)
# - Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# - Dictionary
tel = {'sss': 666, 'jack': 4098, 'sape': 4139}
print(tel)
print(sorted(tel.keys()))
print(tel['jack'])

# File
f1 = open('workfile1', 'w')
f1.write('This is line1\n')
f1.write('This is line2\n')
f1.close()

f2 = open('workfile1', 'r')
data = f2.read()
print(data)
f2.close()

f2 = open('workfile1', 'r')
data = f2.readline()
while (data != ''):
    print(data, end='')
    data = f2.readline()
f2.close()

f2 = open('workfile1', 'r')
data = f2.readlines()
print(data)
f2.close()

f2 = open('workfile1', 'r')
data = list(f2)
print(data)
f2.close()

# exception

# class

# library
import os
import sys
import shutil
import glob
import re
import math
import random
import statistics
import urllib
import smtplib
import datetime
import zlib
import timeit
import reprlib
import pprint
import textwrap
import locale
from string import Template
import struct
import threading
import logging
import weakref, gc
from decimal import *

print(sys.argv)

data = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(data)
data = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(data)
data = 'tea for too'.replace('too', 'two')
print(data)

# format string
print('I have spotted %d camels.' % 10)
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
