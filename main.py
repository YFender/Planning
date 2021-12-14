import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from des import *
from timer_stand import *
from pomidor import *
from task_wid import *
from dialog_del import *
from datetime import datetime
import json


try:
    data = {}
    data['tasks'] = []
    with open('tasks.json') as json_file:
        data = json.load(json_file)
        #print(data["tasks"])
        #for p in data['tasks']:
        #print(p)
        #    self.ui.listWidget.addItem(p["task"])
except Exception:
    pass


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stand_time.triggered.connect(self.timer_stand)
        self.ui.pomidor.triggered.connect(self.timer_pomidor)
        self.ui.create_task.triggered.connect(self.create_task)
        self.ui.refresh.triggered.connect(self.read_tasks)

        self.read_tasks()

        self.ui.pushButton_delete.setEnabled(False)
        self.ui.pushButton_redact.setEnabled(False)

        self.ui.listWidget.itemClicked.connect(self.select_task)

        self.ui.pushButton_delete.clicked.connect(self.delete_task)

        self.ui.refresh.setShortcut("f5")
        self.ui.pushButton_delete.setShortcut("delete")

    def select_task(self):
        self.ui.pushButton_delete.setEnabled(True)
        self.ui.pushButton_redact.setEnabled(True)
        print(self.ui.listWidget.currentRow())

    def timer_stand(self):
        self.w2 = Timer_stand()
        self.w2.show()

    def timer_pomidor(self):
        self.w3 = Pomidor()
        self.w3.show()

    def create_task(self):
        self.w4 = Create_task()
        self.w4.show()

    def isac(self):
        if self.w4.isEnabled:
            print("a")
        #self.read_tasks()

    def read_tasks(self):
        self.ui.listWidget.clear()
        for p in data['tasks']:
            print(p["task"])
            self.ui.listWidget.addItem(p["task"])
        print("\n")

    def dialog_del(self):
        self.w2 = Dialog_del()
        self.w2.show()

        Ui_Form_dialog_del().dialogButtonBox.accepted.connect(
            self.delete_task)

    def delete_task(self):
        try:
            print(data)
            #self.ui.listWidget.removeItemWidget(self.ui.listWidget.takeItem(row))
            data["tasks"].pop(self.ui.listWidget.currentRow())
            #print(data)
            self.ui.listWidget.clear()
            with open("tasks.json", "w") as fin:
                json.dump(data, fin)
            self.read_tasks()
        except Exception:
            pass


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
        )*60*60+self.ui.spinBox_min.value()*60+self.ui.spinBox_sec.value()

        self.ui.lcdNumber.show()
        self.ui.lcdNumber.display(
            f"{self.timer_value//3600}:{(self.timer_value//60)%60}:{self.timer_value%60}")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.timer_proc())
        self.timer.start(1000)

    def timer_proc(self):
        if self.timer_value > 0:
            self.timer_value -= 1
            self.ui.lcdNumber.display(
                f"{self.timer_value//3600}:{(self.timer_value//60)%60}:{self.timer_value%60}")
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
        self.timer_value_rab = 25*60
        self.timer_value_otdih = 5*60
        self.podhod_value = self.ui.spinBox.value()
        self.ui.label_podhod.show()
        self.ui.label_podhod.setText(f'"Помидор" №{self.podhod_count}')
        print(self.podhod_value)
        self.ui.start_button.hide()
        self.ui.stop_button.show()
        #print(self.podhod)
        self.ui.lcdrabota.display(
            f"{self.timer_value_rab//60}:{self.timer_value_rab%60}")
        self.ui.lcdrabota.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_proc_rab)
        self.timer.start(1000)
        #self.timer_proc(timer_value)
        #self.ui

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
                f"{self.timer_value_rab//60}:{self.timer_value_rab%60}")
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
                f"{self.timer_value_otdih//60}:{self.timer_value_otdih%60}")
        else:
            print("stop otdih")
            self.timer_otdih.stop()
            print(self.timer_otdih.isActive())
            if self.podhod_value > 1:
                self.ui.spinBox.setValue(self.ui.spinBox.value()-1)
                #self.timer_proc_rab()
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
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_task()
        self.ui.setupUi(self)

        self.ui.pushButton_create.clicked.connect(self.create_task)

        self.ui.dateEdit.setDate(datetime.today().date())
        self.ui.timeEdit.setTime(datetime.today().time())

        self.ui.checkBox_date.stateChanged.connect(self.hide_date)
        self.ui.checkBox_time.stateChanged.connect(self.hide_time)

    def create_task(self):
        #data = {}
        #data["tasks"] = []
        if self.ui.lineEdit_task.text() != "":
            data["tasks"].append({
                "task": f"{self.ui.lineEdit_task.text()}",
                "time": f"{self.ui.timeEdit.time().hour()}:{self.ui.timeEdit.time().minute()}",
                "date": f"{self.ui.timeEdit.date().currentDate().day()}.{self.ui.timeEdit.date().currentDate().month()}.{self.ui.timeEdit.date().currentDate().year()}",
            })
            with open("tasks.json", "w") as fin:
                json.dump(data, fin)
                #print(data)

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


class Dialog_del(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_dialog_del()
        self.ui.setupUi(self)

        #self.ui.dialogButtonBox.accepted.connect(self.delete_task)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
