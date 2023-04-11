"""
Plane (Body extension)
"""
from .some_body import *
from .some_body.body import Body

class Plane(Body):
    """
    Plane physics
    """
    def __init__(self, x, y):
        """
        Создать самолет.
        """
        super().__init__(x, y, 75, 1) # Вызовем конструктор предка — тела, он актуален

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.v_y -= MODEL_G /4 * MODEL_DT  # медленно снижается
        super().advance()
