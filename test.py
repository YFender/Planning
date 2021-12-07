import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window1')
        self.setMinimumWidth(200)
        self.setMinimumHeight(50)
        self.button = QPushButton(self)
        self.button.setText('Ok')
        self.button.show()
        self.init_handlers()

    def init_handlers(self):  # обработка нажатия для октрытия 2 окна
        self.button.clicked.connect(self.show_window_2)

    def show_window_2(self):  # открытие 2  окна
        self.w2 = Window2()
        self.w2.show()


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window1()
    w.show()  # открытие 1 окна
    sys.exit(app.exec_())
