"""
Plane (Body extension)
"""
from .some_physics.body import Body
MODEL_G = 9.81
MODEL_DT = 0.001

class Plane(Body):
    """
    Plane physics
    """
    def __init__(self, v_x = 75, v_y = 1, x = 0, y = 1500):
        """
        Создать самолет.
        """
        super().__init__(x, y, v_x, v_y) # Вызовем конструктор предка — тела, он актуален
    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.v_y -= MODEL_G /4 * MODEL_DT  # медленно снижается
        super().advance()
