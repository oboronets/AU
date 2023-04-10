#!/usr/bin/env python3
"""
Extended euclidean method
"""
# -*- coding: utf-8 -*-

def extended_gcd(a, b):
    """
    Extended euclidean method
    """
    if a == 0:
        A = [0, 0, 0]
        A[0] = b
        A[1] = 0
        A[2] = 1
        return A
    B = extended_gcd(b % a, a)
    return [B[0], B[2] - (b // a) * B[1], B[1]]

first_num = int(input())
second_num = int(input())

res = extended_gcd(first_num, second_num)
print(first_num, "*", res[1], " + ", second_num, "*", res[2], " = ", res[0])
