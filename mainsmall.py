import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer

from Smallmonitor import *

class MainSmallWindow(QMainWindow):
    def __init__(self):
        super(MainSmallWindow, self).__init__()

        self.ui = Ui_Smallmonitor()
        self.ui.setupUi(self)
        self.connectdb()
        self.timer = QTimer()
        self.timer.start(6000)
        self.timer.timeout.connect(self.connectdb)
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    

    def connectdb(self):
        mydb = mc.connect(
            host="localhost",
                user="root",
                password="",
                database="carlot"
        )
        mycursor = mydb.cursor()
        mycursor.execute('''
            SELECT card.user_license_plate, lot.parked_zone ,lot.number
            FROM lot
            INNER JOIN card ON lot.lot_id  = card.lot_id
            WHERE card.status_id="3"
            ''')
        result = mycursor.fetchone()
        if result:
            self.ui.np_right_label.setText(str(result[0]))
            self.ui.zone_right_label.setText(str(result[1]))
            self.ui.bay_right_label.setText(str(result[2]))
        else:
            self.ui.np_right_label.clear()
            self.ui.zone_right_label.clear()
            self.ui.bay_right_label.clear()

if __name__ =="__main__":
    app = QApplication(sys.argv)

    # style_file = QFile("smallscreenstyle.qss")
    # style_file.open(QFile.ReadOnly | QFile.Text)
    # style_stream = QTextStream(style_file)
    # app.setStyleSheet(style_stream.readAll())

    window = MainSmallWindow()
    window.show()

    sys.exit(app.exec())