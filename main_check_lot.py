import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer

from check_lot import *



class MainChecklotWindow(QMainWindow):
    def __init__(self):
        super(MainChecklotWindow, self).__init__()

        self.ui = Ui_check_lot()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.bayA_btn.setChecked(True)
        
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.connectdb)
        # self.ui.bayA_btn.clicked.connect
        

    def on_bayA_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_bayB_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_bayC_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_bayD_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_bayE_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    def on_bayF_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    def on_bayG_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    def on_bayH_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def connectdb(self):
        mydb = mc.connect(
            host="localhost",
                user="root",
                password="",
                database="carlot"
        )
        mycursor = mydb.cursor()

        while True:
            list=[]
            mycursor.execute("SELECT number,status_id FROM lot  ")
            lot_db = mycursor.fetchall()

            for row in lot_db:
                list.append(row[1])
            
            labels = [self.ui.a101, self.ui.a102, self.ui.a103, self.ui.a104,
                      self.ui.a201, self.ui.a202, self.ui.a203, self.ui.a204,
                      self.ui.a301, self.ui.a302, self.ui.a303, self.ui.a304,
                      self.ui.a401, self.ui.a402, self.ui.a403, self.ui.a404,
                      self.ui.a501, self.ui.a502, self.ui.a503, self.ui.a504,
                      self.ui.a601, self.ui.a602, self.ui.a603, self.ui.a604,
                      self.ui.a701, self.ui.a702, self.ui.a703, self.ui.a704, self.ui.a705,

                      self.ui.b101, self.ui.b102, self.ui.b103, self.ui.b104,
                      self.ui.b201, self.ui.b202, self.ui.b203, self.ui.b204,
                      self.ui.b301, self.ui.b302, self.ui.b303, self.ui.b304,
                      self.ui.b401, self.ui.b402, self.ui.b403, self.ui.b404,
                      self.ui.b501, self.ui.b502, self.ui.b503, self.ui.b504,
                      self.ui.b601, self.ui.b602, self.ui.b603, self.ui.b604,
                      self.ui.b701, self.ui.b702, self.ui.b703, self.ui.b704, self.ui.b705,

                      self.ui.c101, self.ui.c102, self.ui.c103, self.ui.c104,
                      self.ui.c201, self.ui.c202, self.ui.c203, self.ui.c204,
                      self.ui.c301, self.ui.c302, self.ui.c303, self.ui.c304,
                      self.ui.c401, self.ui.c402, self.ui.c403, self.ui.c404,
                      self.ui.c501, self.ui.c502, self.ui.c503, self.ui.c504,
                      self.ui.c601, self.ui.c602, self.ui.c603, self.ui.c604,
                      self.ui.c701, self.ui.c702, self.ui.c703, self.ui.c704, self.ui.c705,

                      self.ui.d101, self.ui.d102, self.ui.d103, self.ui.d104,
                      self.ui.d201, self.ui.d202, self.ui.d203, self.ui.d204,
                      self.ui.d301, self.ui.d302, self.ui.d303, self.ui.d304,
                      self.ui.d401, self.ui.d402, self.ui.d403, self.ui.d404,
                      self.ui.d501, self.ui.d502, self.ui.d503, self.ui.d504,
                      self.ui.d601, self.ui.d602, self.ui.d603, self.ui.d604,
                      self.ui.d701, self.ui.d702, self.ui.d703, self.ui.d704, self.ui.d705,

                      self.ui.e101, self.ui.e102, self.ui.e103, self.ui.e104,
                      self.ui.e201, self.ui.e202, self.ui.e203, self.ui.e204,
                      self.ui.e301, self.ui.e302, self.ui.e303, self.ui.e304,
                      self.ui.e401, self.ui.e402, self.ui.e403, self.ui.e404,
                      self.ui.e501, self.ui.e502, self.ui.e503, self.ui.e504,
                      self.ui.e601, self.ui.e602, self.ui.e603, self.ui.e604,
                      self.ui.e701, self.ui.e702, self.ui.e703, self.ui.e704, self.ui.e705,

                      self.ui.f101, self.ui.f102, self.ui.f103, self.ui.f104,
                      self.ui.f201, self.ui.f202, self.ui.f203, self.ui.f204,
                      self.ui.f301, self.ui.f302, self.ui.f303, self.ui.f304,
                      self.ui.f401, self.ui.f402, self.ui.f403, self.ui.f404,
                      self.ui.f501, self.ui.f502, self.ui.f503, self.ui.f504,
                      self.ui.f601, self.ui.f602, self.ui.f603, self.ui.f604,
                      self.ui.f701, self.ui.f702, self.ui.f703, self.ui.f704, self.ui.f705,

                      self.ui.g101, self.ui.g102, self.ui.g103, self.ui.g104,
                      self.ui.g201, self.ui.g202, self.ui.g203, self.ui.g204,
                      self.ui.g301, self.ui.g302, self.ui.g303, self.ui.g304,
                      self.ui.g401, self.ui.g402, self.ui.g403, self.ui.g404,
                      self.ui.g501, self.ui.g502, self.ui.g503, self.ui.g504,
                      self.ui.g601, self.ui.g602, self.ui.g603, self.ui.g604,
                      self.ui.g701, self.ui.g702, self.ui.g703, self.ui.g704, self.ui.g705,

                      self.ui.h101, self.ui.h102, self.ui.h103, self.ui.h104,
                      self.ui.h201, self.ui.h202, self.ui.h203, self.ui.h204,
                      self.ui.h301, self.ui.h302, self.ui.h303, self.ui.h304,
                      self.ui.h401, self.ui.h402, self.ui.h403, self.ui.h404,
                      self.ui.h501, self.ui.h502, self.ui.h503, self.ui.h504,
                      self.ui.h601, self.ui.h602, self.ui.h603, self.ui.h604,
                      self.ui.h701, self.ui.h702, self.ui.h703, self.ui.h704, self.ui.h705
                      ]
            
            for item, label in zip(list,labels):
                if item == 7:
                    label.setStyleSheet("background-color: #580EF6;border-radius: 10px;color: #fff;")
                elif item == 6:
                    label.setStyleSheet("background-color: #F8DE22;border-radius: 10px;color: #000000;")
                elif item == 1:
                    label.setStyleSheet("background-color: #16FF00;border-radius: 10px;color: #000000;")
                else:
                    label.setStyleSheet("background-color: #16FF00;border-radius: 10px;color: #000000;")
            break

        # print(list)
    

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainChecklotWindow()
    window.show()
    sys.exit(app.exec())