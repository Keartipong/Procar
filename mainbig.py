import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer


from Bigmonitor import *


class MainBigWindow(QMainWindow):
    def __init__(self):
        super(MainBigWindow, self).__init__()

        self.ui = Ui_BigMonitor()
        self.ui.setupUi(self)
        self.connectdb()
        self.timer = QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.connectdb)
        
        # self.showFullScreen()
        
        #flamelesswindow
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        

    def connectdb(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="carlot")
        
        
        mycursor = mydb.cursor()
        mycursor.execute('''
            SELECT card.user_license_plate, lot.parked_zone ,lot.number
            FROM lot
            INNER JOIN card ON lot.lot_id  = card.lot_id
            WHERE card.status_id="6"
            ''')
        result = mycursor.fetchone()
        # print(result)
        
        #left_checking
        if result:
            self.ui.num_plate1_left_label.setText(str(result[0]))
            self.ui.zone1_left_label.setText(str(result[1]))
            self.ui.bay1_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate1_left_label.clear()
            self.ui.zone1_left_label.clear()
            self.ui.bay1_left_label.clear()
            
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate2_left_label.setText(str(result[0]))
            self.ui.zone2_left_label.setText(str(result[1]))
            self.ui.bay2_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate2_left_label.clear()
            self.ui.zone2_left_label.clear()
            self.ui.bay2_left_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate3_left_label.setText(str(result[0]))
            self.ui.zone3_left_label.setText(str(result[1]))
            self.ui.bay3_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate3_left_label.clear()
            self.ui.zone3_left_label.clear()
            self.ui.bay3_left_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate4_left_label.setText(str(result[0]))
            self.ui.zone4_left_label.setText(str(result[1]))
            self.ui.bay4_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate4_left_label.clear()
            self.ui.zone4_left_label.clear()
            self.ui.bay4_left_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate5_left_label.setText(str(result[0]))
            self.ui.zone5_left_label.setText(str(result[1]))
            self.ui.bay5_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate5_left_label.clear()
            self.ui.zone5_left_label.clear()
            self.ui.bay5_left_label.clear()
        
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate6_left_label.setText(str(result[0]))
            self.ui.zone6_left_label.setText(str(result[1]))
            self.ui.bay6_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate6_left_label.clear()
            self.ui.zone6_left_label.clear()
            self.ui.bay6_left_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate7_left_label.setText(str(result[0]))
            self.ui.zone7_left_label.setText(str(result[1]))
            self.ui.bay7_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate7_left_label.clear()
            self.ui.zone7_left_label.clear()
            self.ui.bay7_left_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate8_left_label.setText(str(result[0]))
            self.ui.zone8_left_label.setText(str(result[1]))
            self.ui.bay8_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate8_left_label.clear()
            self.ui.zone8_left_label.clear()
            self.ui.bay8_left_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate9_left_label.setText(str(result[0]))
            self.ui.zone9_left_label.setText(str(result[1]))
            self.ui.bay9_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate9_left_label.clear()
            self.ui.zone9_left_label.clear()
            self.ui.bay9_left_label.clear()
        
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate10_left_label.setText(str(result[0]))
            self.ui.zone10_left_label.setText(str(result[1]))
            self.ui.bay10_left_label.setText(str(result[2]))
        else:
            self.ui.num_plate10_left_label.clear()
            self.ui.zone10_left_label.clear()
            self.ui.bay10_left_label.clear()
       

        #right_checking
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate1_right_label.setText(str(result[0]))
            self.ui.zone1_right_label.setText(str(result[1]))
            self.ui.bay1_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate1_right_label.clear()
            self.ui.zone1_right_label.clear()
            self.ui.bay1_right_label.clear()
    
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate2_right_label.setText(str(result[0]))
            self.ui.zone2_right_label.setText(str(result[1]))
            self.ui.bay2_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate2_right_label.clear()
            self.ui.zone2_right_label.clear()
            self.ui.bay2_right_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate3_right_label.setText(str(result[0]))
            self.ui.zone3_right_label.setText(str(result[1]))
            self.ui.bay3_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate3_right_label.clear()
            self.ui.zone3_right_label.clear()
            self.ui.bay3_right_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate4_right_label.setText(str(result[0]))
            self.ui.zone4_right_label.setText(str(result[1]))
            self.ui.bay4_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate4_right_label.clear()
            self.ui.zone4_right_label.clear()
            self.ui.bay4_right_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate5_right_label.setText(str(result[0]))
            self.ui.zone5_right_label.setText(str(result[1]))
            self.ui.bay5_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate5_right_label.clear()
            self.ui.zone5_right_label.clear()
            self.ui.bay5_right_label.clear()
        
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate6_right_label.setText(str(result[0]))
            self.ui.zone6_right_label.setText(str(result[1]))
            self.ui.bay6_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate6_right_label.clear()
            self.ui.zone6_right_label.clear()
            self.ui.bay6_right_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate7_right_label.setText(str(result[0]))
            self.ui.zone7_right_label.setText(str(result[1]))
            self.ui.bay7_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate7_right_label.clear()
            self.ui.zone7_right_label.clear()
            self.ui.bay7_right_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate8_right_label.setText(str(result[0]))
            self.ui.zone8_right_label.setText(str(result[1]))
            self.ui.bay8_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate8_right_label.clear()
            self.ui.zone8_right_label.clear()
            self.ui.bay8_right_label.clear()

        result = mycursor.fetchone()
        if result:
            self.ui.num_plate9_right_label.setText(str(result[0]))
            self.ui.zone9_right_label.setText(str(result[1]))
            self.ui.bay9_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate9_right_label.clear()
            self.ui.zone9_right_label.clear()
            self.ui.bay9_right_label.clear()
        
        result = mycursor.fetchone()
        if result:
            self.ui.num_plate10_right_label.setText(str(result[0]))
            self.ui.zone10_right_label.setText(str(result[1]))
            self.ui.bay10_right_label.setText(str(result[2]))
        else:
            self.ui.num_plate10_right_label.clear()
            self.ui.zone10_right_label.clear()
            self.ui.bay10_right_label.clear()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    bigwindow = MainBigWindow()
    bigwindow.show()
    
        
    sys.exit(app.exec())

    