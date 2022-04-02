"""в этом файле прописана логика программы, в остальных .py файлах прописан только интерфейс"""
import os.path
import sqlite3
from datetime import datetime
from sys import exit, argv

from PyQt5 import QtMultimedia

from des import *
from pomidor import *
from settings import *
from task_wid import *
from timer_stand import *

if not os.path.isfile("Tasks.sqlite"):
    conn = sqlite3.connect("Tasks.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE Tasks(TaskID INTEGER PRIMARY KEY, TaskName VARCHAR(20) NOT NULL, Description VARCHAR(20) NOT NULL, Time TIME, Date DATE)")
    conn.close()

conn = sqlite3.connect("Tasks.sqlite")
cursor = conn.cursor()
"""чтение БД задач из файла"""

print(datetime.today().date())
print(datetime.today().time())


class MyWin(QtWidgets.QMainWindow):
    """класс с запуском и управлением главным окном"""

    def __init__(self, parent=None):
        """инициализация и запуск интерфейса"""
        super(MyWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """инструкции для определенных событий"""
        self.ui.stand_time.triggered.connect(self.timer_stand)
        self.ui.pomidor.triggered.connect(self.timer_pomidor)
        self.ui.create_task.triggered.connect(self.create_task)
        self.ui.refresh.triggered.connect(self.read_tasks)

        self.read_tasks()

        # self.test()

        self.ui.pushButton_delete.setEnabled(False)
        self.ui.pushButton_redact.setEnabled(False)

        self.ui.listWidget.itemClicked.connect(self.select_task)

        self.ui.pushButton_delete.clicked.connect(self.delete_task)
        self.ui.pushButton_redact.clicked.connect(self.redact_task)

        self.ui.refresh.setShortcut("f5")
        self.ui.pushButton_delete.setShortcut("delete")

    def select_task(self):
        """разблокировка кнопок редактирования и удаления, если выделен элемент с задачей"""
        self.ui.pushButton_delete.setEnabled(True)
        self.ui.pushButton_redact.setEnabled(True)
        # print(self.ui.listWidget.currentRow())
        cursor.execute(
            f"SELECT * FROM Tasks WHERE TaskID = {self.ui.listWidget.currentRow() + 1}")
        data = cursor.fetchone()
        self.ui.textBrowser.setText(data[0][2])
        print(data)
        print(data[0][2])
        # print(result[self.ui.listWidget.currentRow()])
        # self.ui.textBrowser.setText(data["tasks"][self.ui.listWidget.currentRow()]["description"])

    def timer_stand(self):
        """запуск стандартного таймера"""
        self.w2 = Timer_stand()
        self.w2.show()

    def timer_pomidor(self):
        """запуска помидорного таймера"""
        self.w3 = Pomidor()
        self.w3.show()

    def create_task(self):
        """запуск окна с созданием задачи"""
        self.w4 = Create_task(self)
        self.w4.show()

    def read_tasks(self):
        """функция чтения и вывода задач из массива"""
        self.ui.listWidget.clear()
        cursor.execute("SELECT TaskName FROM Tasks ")
        result = cursor.fetchall()
        # print(result)
        for i in result:
            print(i)
            self.ui.listWidget.addItem(i[0])
        print("\n")

    def redact_task(self):
        self.w5 = Redact_task(self)
        self.w5.show()

    def delete_task(self):
        """удаление выбранной задачи"""
        try:
            # self.ui.listWidget.removeItemWidget(self.ui.listWidget.takeItem(row))
            deletedid = self.ui.listWidget.currentRow() + 1
            cursor.execute(f"DELETE FROM Tasks WHERE TaskID = {deletedid}")
            conn.commit()
            cursor.execute(
                f"UPDATE Tasks SET TaskID = TaskID - 1 WHERE TaskID > {deletedid}")
            conn.commit()
            # print(data)
            self.ui.listWidget.clear()

            self.ui.refresh.trigger()
        except Exception:
            pass


"""остальные классы имеют аналогичное строение"""


class Timer_stand(QtWidgets.QWidget):
    def __init__(self):
        super(Timer_stand, self).__init__()
        self.ui = Ui_Form_timer()
        self.ui.setupUi(self)
        self.ui.lcdNumber.hide()
        self.ui.stop_button.hide()

        self.ui.start_button.clicked.connect(self.start)
        self.ui.stop_button.clicked.connect(self.stop)

        self.url = QtCore.QUrl.fromLocalFile(
            "./notifications_sounds/notification.wav")
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)

    def start(self):
        self.ui.label.hide()
        self.ui.spinBox_min.hide()
        self.ui.spinBox_sec.hide()
        self.ui.spinBox_hour.hide()
        self.ui.label_sec.hide()
        self.ui.label_min.hide()
        self.ui.label_hour.hide()
        self.ui.start_button.hide()
        self.ui.stop_button.show()

        self.timer_value = self.ui.spinBox_hour.value(
        ) * 60 * 60 + self.ui.spinBox_min.value() * 60 + self.ui.spinBox_sec.value()

        self.ui.lcdNumber.show()
        self.ui.lcdNumber.display(
            f"{self.timer_value // 3600}:{(self.timer_value // 60) % 60}:{self.timer_value % 60}")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.timer_proc())
        self.timer.start(1000)

    def timer_proc(self):
        if self.timer_value > 0:
            self.timer_value -= 1
            self.ui.lcdNumber.display(
                f"{self.timer_value // 3600}:{(self.timer_value // 60) % 60}:{self.timer_value % 60}")
        else:
            self.ui.stop_button.click()

    def stop(self):
        self.timer.stop()

        self.player.play()

        self.ui.label.show()
        self.ui.spinBox_min.show()
        self.ui.spinBox_sec.show()
        self.ui.spinBox_hour.show()
        self.ui.label_sec.show()
        self.ui.label_min.show()
        self.ui.label_hour.show()
        self.ui.start_button.show()
        self.ui.stop_button.hide()
        self.ui.lcdNumber.hide()


class Pomidor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_pomidor()
        self.ui.setupUi(self)
        self.ui.label_podhod.hide()
        self.ui.lcdrabota.hide()
        self.ui.stop_button.hide()
        self.ui.lcdotdih.hide()
        self.ui.label_rabota.hide()
        self.ui.label_otdih.hide()

        self.ui.start_button.clicked.connect(self.start)
        self.ui.stop_button.clicked.connect(self.stop)

        self.podhod_count = 1

        self.url = QtCore.QUrl.fromLocalFile(
            "./notifications_sounds/notification.wav")
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)

    def start(self):
        self.ui.spinBox.hide()
        self.ui.label.hide()
        self.timer_value_rab = 25 * 60
        self.timer_value_otdih = 5 * 60
        self.podhod_value = self.ui.spinBox.value()
        self.ui.label_podhod.show()
        if config["Settings"]["Language"] == "Russian_Russia":
            self.ui.label_podhod.setText(f'"Помидор" №{self.podhod_count}')
        else:
            self.ui.label_podhod.setText(f'"Pomodoro" №{self.podhod_count}')
        print(self.podhod_value)
        self.ui.start_button.hide()
        self.ui.stop_button.show()
        # print(self.podhod)
        self.ui.lcdrabota.display(
            f"{self.timer_value_rab // 60}:{self.timer_value_rab % 60}")
        self.ui.lcdrabota.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_proc_rab)
        self.timer.start(1000)
        # self.timer_proc(timer_value)
        # self.ui

    def stop(self):
        self.player.play()
        self.timer.stop()
        try:
            self.timer_otdih.stop()
        except Exception:
            pass
        self.ui.start_button.show()
        self.ui.stop_button.hide()
        self.ui.label_rabota.hide()
        self.ui.label_otdih.hide()
        self.ui.label_podhod.hide()
        self.ui.label.show()
        self.ui.spinBox.show()
        self.ui.lcdrabota.hide()
        self.ui.lcdotdih.hide()

    def timer_proc_rab(self):
        self.ui.label_otdih.hide()
        self.ui.label_rabota.show()
        if self.timer_value_rab > 0:
            self.timer_value_rab -= 1
            self.ui.lcdrabota.show()
            self.ui.lcdrabota.display(
                f"{self.timer_value_rab // 60}:{self.timer_value_rab % 60}")
        else:
            print("stop rabota")
            self.timer.stop()
            self.player.play()
            if self.timer_value_otdih > 0:
                self.timer_otdih = QtCore.QTimer(self)
                self.timer_otdih.timeout.connect(
                    lambda: self.timer_proc_otdih())
                self.timer_otdih.start(1000)

    def timer_proc_otdih(self):
        self.ui.label_rabota.hide()
        self.ui.label_otdih.show()
        if self.timer_value_otdih > 0:
            self.timer_value_otdih -= 1
            self.ui.lcdrabota.hide()
            self.ui.lcdotdih.show()
            self.ui.lcdotdih.display(
                f"{self.timer_value_otdih // 60}:{self.timer_value_otdih % 60}")
        else:
            print("stop otdih")
            self.timer_otdih.stop()
            print(self.timer_otdih.isActive())
            if self.podhod_value > 1:
                self.ui.spinBox.setValue(self.ui.spinBox.value() - 1)
                # self.timer_proc_rab()
                self.ui.lcdotdih.hide()
                self.podhod_count += 1
                self.ui.start_button.click()

            else:
                self.player.play()
                self.ui.lcdotdih.hide()
                self.ui.label_rabota.hide()
                self.ui.label_otdih.hide()
                self.ui.label_podhod.hide()
                self.ui.label.show()
                self.ui.spinBox.show()
                self.ui.stop_button.hide()
                self.ui.start_button.show()


class Create_task(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Create_task, self).__init__()
        self.ui = Ui_Form_task()
        self.ui.setupUi(self)

        self.parent = parent

        self.ui.pushButton_create.clicked.connect(self.create_task)

        self.ui.dateEdit.setDate(datetime.today().date())
        self.ui.timeEdit.setTime(datetime.today().time())

        self.ui.checkBox_date.stateChanged.connect(self.hide_date)
        self.ui.checkBox_time.stateChanged.connect(self.hide_time)
        # self.show()

    def create_task(self):

        # data["tasks"] = []
        if not self.ui.checkBox_date.isChecked():
            self.date = self.ui.timeEdit.date()
        #    self.date = f"{self.ui.dateEdit.date().day()}.{self.ui.dateEdit.date().month()}.{self.ui.dateEdit.date().year()}"
        else:
            self.date = "Null"

        if not self.ui.checkBox_time.isChecked():
            self.time = self.ui.dateEdit.date()
            self.time = f"{self.ui.timeEdit.time().hour()}:{self.ui.timeEdit.time().minute()}:0.0"
        else:
            self.time = "Null"

        if self.ui.lineEdit_task.text() != "":
            cursor.execute(
                f"INSERT INTO Tasks VALUES (Null, '{self.ui.lineEdit_task.text()}', '{self.ui.plainTextEdit.toPlainText()}', '{self.time}', '{self.date}' )")
            conn.commit()
            # print(data)
            self.parent.ui.refresh.trigger()
            self.close()

    def hide_date(self):
        if self.ui.checkBox_date.checkState():
            self.ui.dateEdit.hide()
            self.ui.label_date.hide()
            self.ui.dateEdit.clear()
        else:
            self.ui.dateEdit.show()
            self.ui.label_date.show()
            self.ui.dateEdit.setDate(datetime.now().date())

    def hide_time(self):
        if self.ui.checkBox_time.checkState():
            self.ui.timeEdit.hide()
            self.ui.label_time.hide()
            self.ui.timeEdit.clear()
        else:
            self.ui.timeEdit.show()
            self.ui.timeEdit.setTime(datetime.today().time())
            self.ui.label_time.show()


class Redact_task(QtWidgets.QWidget):
    try:
        def __init__(self, parent=None):
            super(Redact_task, self).__init__()
            self.ui = Ui_Form_task()
            self.ui.setupUi(self)

            self.ui.pushButton_create.setText("Редактировать задачу")
            self.ui.pushButton_create.clicked.connect(self.redact_task)

            self.parent = parent

            print(self.parent.ui.listWidget.currentRow() + 1)
            cursor.execute(
                f"SELECT * FROM Tasks WHERE TaskID = {self.parent.ui.listWidget.currentRow() + 1}")
            data = cursor.fetchone()
            print(data)

            self.ui.plainTextEdit.setPlainText(data[0][2])
            self.ui.lineEdit_task.setText(data[0][1])

            if not data[0][3] == "Null":
                pass
                # self.ui.timeEdit.setTime(data[0][3])
                # self.ui.timeEdit.setTime(f"{int(data[0][3].replace(':',''))/100}:{int(data[0][3].replace(':',''))%100}")
            else:
                self.ui.checkBox_time.setEnabled(True)
            if not data[0][4] == "Null":
                pass
                # self.ui.dateEdit.setDate(data[0][4])
            else:
                self.ui.checkBox_date.setEnabled(True)

        def redact_task(self):
            pass

    except Exception as ex:
        print(ex)


class Settings(QtWidgets.QWidget):
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = MyWin()
    myapp.show()
    exit(app.exec_())
