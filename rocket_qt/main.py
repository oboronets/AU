"""
Rocket qt'ed
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import uic, QtGui

from matplotlib import pyplot as pp

from rocket_qt.plane import Plane
from rocket_qt.rocket import Rocket
from rocket_qt.collision import collision

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/main_dialog.ui", self)
        self.ready_to_launch = [True, False]

        self.target_vx = 75
        self.target_vy = 1
        self.time = 60
        self.start_v = 500

        self.ui.failure_label.hide()
        self.ui.success_label.hide()
        self.ui.failure_start_label.hide()
        self.ui.graf_label.hide()
        self.hide_launch()

        self.ui.max_time_lineEdit.setText("60")
        self.ui.vx_lineEdit.setText("75")
        self.ui.vy_lineEdit.setText("1")

        self.ui.save_button.clicked.connect(self.save_changes)
        self.ui.save_start_button.clicked.connect(self.save_start)
        self.ui.traj_radioButton.clicked.connect(self.ui.graf_label.hide)

    def hide_launch(self):
        """
        Всегда вместе
        """
        self.ui.launch_failure_eternal.hide()
        self.ui.launch_failure_rocket.hide()
        self.ui.launch_failure_plane.hide()

    def save_changes(self):
        """
        Действия по кнопке "сохранить" в параметрах самолета
        """
        try:
            get_vx = float( self.ui.vx_lineEdit.text() )
            get_vy = float( self.ui.vy_lineEdit.text() )
            get_time = float( self.ui.max_time_lineEdit.text() )
            self.ui.failure_label.hide()

        except:
            self.ui.failure_label.show()
            self.ready_to_launch[0] = False
            get_vx = 1000
            get_vy = 1000
            get_time = None

        if ( (get_vx**2 > 300**2) + (get_vy**2 > 100**2) ) != 0:
            self.ui.failure_label.show()
        else:
            self.target_vx = get_vx
            self.target_vy = get_vy
            self.time = get_time
            self.ready_to_launch[0] = True
            self.ui.success_label.show()
            self.ui.podlet_lineEdit.setText("")

    def save_start(self):
        """
        Действия по кнопке "сохранить" в парметрах ракеты
        """
        try:
            get_v = float( self.ui.start_v_lineEdit.text() )
            self.ui.failure_start_label.hide()
        except:
            self.ui.failure_start_label.show()
            self.ready_to_launch[1] = False
            get_v = 1000

        if (get_v > 340) + (get_v < 0):
            self.ui.failure_start_label.show()
        else:
            self.start_v = get_v
            self.ready_to_launch[1] = True
            self.ui.podlet_lineEdit.setText("")

    def launch_rocket(self):
        """
        Кнопка "launch": проверяем, что все готово и вызываем collision
        """
        self.hide_launch()
        if sum(self.ready_to_launch) == 2:
            plane = Plane(self.target_vx, self.target_vy)
            rocket = Rocket(plane, self.start_v)
            podlet, bodies = collision(plane, rocket, self.time)
            self.show_graph(bodies)
            self.ui.graf_label.setPixmap(QtGui.QPixmap("graf.jpg"))

            if self.ui.traj_radioButton.isChecked():
                self.ui.readme_browser.hide()
                self.ui.graf_label.show()

            if podlet > 0:
                self.ui.podlet_lineEdit.setText(str(podlet))
                QMessageBox.information(None, "Попал", "Попал!")
            else:
                QMessageBox.critical(None, "Не попал", "Не попал!")

        elif sum(self.ready_to_launch) == 0:
            self.ui.launch_failure_eternal.show()

        elif not self.ready_to_launch[0]:
            self.ui.launch_failure_plane.show()

        else:
            self.ui.launch_failure_rocket.show()

    def show_graph(self, bodies):
        """
        Чтобы график вставить в окошко сразу экспортируем его в файл
        """
        for b in bodies:
            pp.plot(b.trajectory_x, b.trajectory_y)
        pp.savefig("graf.jpg")
        pp.clf()

app = QApplication(sys.argv)

main = MainWindow()
main.show()

app.exec()
