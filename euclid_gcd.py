#!/usr/bin/env python3
"""
Euclidean method
"""
# -*- coding: utf-8 -*-

a = int(input())
b = int(input())

while (a != 0) & (b != 0):
    if a > b:
        a = a % b
    else:
        b = b % a
if b == 0:
    print(a)
if a == 0:
    print(b)
    
