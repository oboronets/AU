#!/usr/bin/env python3
"""
Check if number is prime
"""
# -*- coding: utf-8 -*-

def prime_check(num):
    """
    Check if number is prime
    """
    smaller_num = 2
    while smaller_num < num:
        if (num % smaller_num) == 0:
            return False
        smaller_num += 1
    return True

print(prime_check(int(input())))
