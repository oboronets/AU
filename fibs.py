#!/usr/bin/env python3
"""
Print first N fibonacci numbers
"""
#  -*- coding: utf-8 -*-
import itertools
N = 20
class Fibs:
    """
    По объектам этого класса можно итерироваться и получать 10 чисел Фибоначчи,
    начиная с N-ного
    """

    class _Fibs_Iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.first = 1
            self.second = 1

        def __next__(self):
            self.second = self.first + self.second
            self.first = self.second - self.first
            self.i += 1
            return self.second - self.first

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fibs._Fibs_Iter()

f = Fibs()
fi = iter(f)

for i, f in zip(
    itertools.count(1),
    itertools.islice(f, 0, N)
):
    print(i, f)
