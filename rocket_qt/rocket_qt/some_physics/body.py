"""
Common Body
"""

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:
    """
    Basics of bodies' physics
    """
    def __init__(self, x, y, v_x, v_y):
        """
        Создать тело.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        self.x += self.v_x * MODEL_DT
        self.y += self.v_y * MODEL_DT
