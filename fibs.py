#!/usr/bin/env python3
"""
Print first N fibonacci numbers
"""
#  -*- coding: utf-8 -*-

N = 130
class Fibs:
    """
    По объектам этого класса можно итерироваться и получать первые N чисел Фибоначчи
    """

    class _Fibs_Iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.fibs_to_rem = [1, 1]

        def __next__(self):
            if self.i < N:
                self.fibs_to_rem[1] = self.fibs_to_rem[0] + self.fibs_to_rem[1]
                self.fibs_to_rem[0] = self.fibs_to_rem[1] - self.fibs_to_rem[0]
                self.i += 1
                return self.fibs_to_rem[1] - self.fibs_to_rem[0]
            raise StopIteration()

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fibs._Fibs_Iter()

f = Fibs()
fi = iter(f)
i = 0

while True:
    i += 1
    try:
        print(i, next(fi))
    except StopIteration:
        print("Done")
        break
