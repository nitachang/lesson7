# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:39:48 2021

@author: nitac
"""

def func():
    print('hello world')
func()

print('-------------------')

def func1(age):
    print('I am',age,'years old.')
func1(7)

print('-------------------')

def add(a,b):
    x=a*b
    return x
y=add(19,38)
print (y)

print('-------------------')

max=0
def subtract(a,b):
    if b<a:
        max=a
        u=max-b
    else:
        max=b
        u=max-a
    return u
s=subtract(50,500)
print(s)

print('-------------------')



    

    
    









