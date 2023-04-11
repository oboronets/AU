"""
Rocket (Body extension)
"""
from .some_body import *  # to use globals in __init__
from .some_body.body import Body

class Rocket(Body):
    """
    Rocket physics
    """
    def __init__(self, target):
        """
        Создать ракету.
        Старт с зесли
        Начальная скорость в 5 раз больше скорости цели
        """
        super().__init__(0, 0, 5 * target.v_x, 5 * target.v_y) # Вызовем конструктор предка

    def target_pos(self, target):
        """
        Получаем координаты цели
        """
        (self.target_x, self.target_y) = (target.x, target.y)

    def advance(self, target):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        Скорость меняется по модулю только из-за g
        Направление скорости - к цели
        """
        self.target_pos(target)
        self.v_y -= MODEL_G * MODEL_DT

        dist = math.sqrt( (self.x - self.target_x)**2 + (self.y - self.target_y)**2)
        mod_v = math.sqrt( (self.v_x)**2 + (self.v_y)**2 )  # Модуль скорости и расст. до цели

        self.v_x = mod_v * ( - self.x + self.target_x ) / dist  # Поворот в сторону цели
        self.v_y = mod_v * ( - self.y + self.target_y ) / dist
        super().advance()
