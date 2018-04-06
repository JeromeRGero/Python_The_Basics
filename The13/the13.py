import random
import sys
import os

print("################################")

def one255():
    x = 1
    while x < 256:
        print(x)
        x = x + 1

one255()

print("################################")

def printodds():
    for i in range(1, 255):
        if i % 2 != 0:
            print(i)

printodds()

print("################################")

total = 0

def psum():
    global total
    for i in range(1, 255):
        total += i
    print(total)

psum()

print("################################")

total = 0

arr = [1, 4, 10, 5]

def parr(arr):
    for i in range(0, len(arr)):
        print(arr[i])

parr(arr)

print("################################")

def find_max(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if max < arr[i]:
            max = arr[i]
    print ("The max is ", max)

find_max(arr)

print("################################")

def print_avg(arr):
    global total
    for i in arr:
        total += i
    avg = total / len(arr)
    print(avg)

print_avg(arr)

print("################################")

def odd_arr():
    narr = []
    for i in range(1, 255):
        if i%2 != 0:
            narr.append(i)
    print(narr)

odd_arr()

print ("################################")

def square_vals(arr):
    for item in enumerate(arr):
        index = item[0]
        arr[index] *= arr[index]
    print(arr)

square_vals(arr)

print ("################################")

def shift_over(arr):
    for i in range(0, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[len(arr) - 1] = 0
    print(arr)

shift_over(arr)

print ("################################")

