#!/usr/bin/env python3
"""
Для множества  из числовых множеств определим
симметричсекую разность (+) и пересечение (*).
Множество с такими операциями образует кольцо.
"""
# -*- coding: utf-8 -*-

from numbers import Number
import numpy

class SetTypeError(TypeError):
    pass

class SetDomainError(ValueError):
    pass

class NumSet:
    """
    Класс числового множества
    Так как сим. разность подразумевает сравнение, операции будем опредлять
    для множества, состоящего из чего-то похожего
    """

    def __init__(self, arg = []):  # arg = [], так как пустое множество хорошо подходит на роль нуля
        """
        elements - элементы множества
        """
        if arg == []:
            self.elements = []
        elif isinstance(arg, Number):
            self.elements = [arg]
        elif isinstance(arg, list):
            for el in arg:
                if not isinstance(el, Number):
                    raise SetTypeError("You are trying to add " + repr(arg) + " to numeric set")
            self.elements = arg.copy()
        elif isinstance(arg, NumSet):
            self.elements = arg.elements.copy()
        else:
            raise SetTypeError("You are trying to create numeric set from " + repr(arg))

    def __str__(self):
        """Переделывает self в красивую строку"""
        return ("{" + ", ".join([str(c) for c in self.elements]) + "}") if len(self.elements) else []

    def __eq__(self, other):
        """Сравнить self и other"""
        if isinstance(other, Number):
            other = NumSet(other)

        if isinstance(other, NumSet):
            return self.elements == other.elements
        else:
            raise SetDomainError("Can't say if set is equal to " + str(type(other)))

    def __lshift__(self, deg):
        """Добавляет deg нулевых элементов"""
        return NumSet(([0] * deg) + self.elements)

    def __sub__(self, other):
        """"
        Вычитание \
        Оставляем элементы, которые пренадлежат self и отличны от всех из other
        """
        if isinstance(other, Number):
            other = NumSet(other)
        c = []
        for self_el in self.elements:
            to_add = True
            for other_el in other.elements:
                if other_el == self_el:
                    to_add = False
                    break
            if to_add:
                c.append(self_el)

        return NumSet(c)

    def __rsub__(self, other):
        """"
        \ не коммутативно
        """
        if isinstance(other, Number):
            other = NumSet(other)
        c = []
        for other_el in other.elements:
            to_add = True
            for self_el in self.elements:
                if other_el == self_el:
                    to_add = False
                    break
            if to_add:
                c.append(other_el)

        return NumSet(c)

    def __mul__(self, other):
        """
        Пересечение
        Оставляем только элементы, которые содержатся и в self, и в other
        """
        if isinstance(other, Number):
            other = NumSet(other)

        c = []
        for self_el in self.elements:
            to_add = False
            for other_el in other.elements:
                if other_el == self_el:
                    to_add = True
                    break
            if to_add:
                c.append(self_el)

        return NumSet(c)

    def __rmul__(self, other):
        """ * коммутативно """
        return self.__mul__(other)

    def __add__(self, other):
        """
        Симметрическая разность
        Оставляем все элементы (self или other) которые не принадлежат self*other
        """
        if isinstance(other, Number):
            other = NumSet(other)

        res = NumSet(self.elements.copy() + other.elements.copy())
        res = res.__sub__(self.__mul__(other))
        return res

    def __radd__(self, other):
        """ + коммутативно """
        return self.__add__(other)

    def __neg__(self):
        """
        Пусть минус преобразует элемент в обратный по + (self + other = 0)
        Но пресечение self и other = self, если и только если
        other = self
        """
        return self

    def __int__(self) -> int:
        if len(self.elements) == 1:
            return int(self.elements[0])
        else:
            raise SetDomainError("Can't consider this set as an integer")

    def __float__(self):
        if len(self.elements) == 1:
            return float(self.elements[0])
        else:
            raise SetDomainError("Can't consider this set as a number")

    def __complex__(self):
        if len(self.elements) == 1:
            return complex(self.elements[0])
        else:
            raise SetDomainError("Can't consider this set as a number")

a = list(numpy.arange(0, 6, 1))
b = list(numpy.arange(5, 10, 1))

set_A = NumSet(a)
set_B = NumSet(b)

print(set_B)
print(-set_A, '\n')

print(set_A - set_B)
print(set_B - set_A, '\n')

print(set_A * set_B)
print(set_B * set_A, '\n')

print(set_A + set_B)
print(set_B + set_A, '\n')

set_C = set_A * set_B
print(int(set_C))
print(float(set_C))
print(complex(set_C), '\n')

print("А дистрибутивность? (частный случай)")
if ( (set_A + set_B) * set_C ) == ( set_A * set_C + set_B *  set_C):
    print(True)
else: print(False)

print('\n', "Сейчас будет ошибка:")
print(int(set_A))
