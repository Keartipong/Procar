import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
import mysql.connector as mc
import requests
import datetime

from Mainwindow_final import Ui_MainWindow
from mainbig import *
from mainsmall import *
from main_controller_z1 import *
from main_controller_z2 import *
from main_check_lot import *
from main_check_broken import *
from main_check_upbroken import *

# bay_order=["A","F","C","B","G","D","H","E"]
bay_order=[]
zone_order=["1","2"]
parked_lot_old=[]
parked_lot=[]
empty_index = []

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]

oha=[]
ohb=[]
ohc=[]
ohd=[]
ohe=[]
ohf=[]
ohg=[]
ohh=[]

mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="carlot"
    )

#load bay order 
mycursor = mydb.cursor()
mycursor.execute('''SELECT name FROM bay_order WHERE status='5' ''')
present_order = mycursor.fetchall()
for row in present_order:
    bay_order.append(row[0])
# print("check present",bay_order)

# nz = normal zone
nz={"A":a,"F":f,"C":c,"B":b,"G":g,"D":d,"H":h,"E":e}

# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}

#Parking Zone
z={"A":zone_order[0],"B":zone_order[0],"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.full_accept_btn.setChecked(True)

        self.timer2 = QTimer()
        self.timer2.start(2000)
        self.timer2.timeout.connect(self.lot_status_check)

        self.ui.monitor1_btn.clicked.connect(self.smallscreen)
        self.ui.monitor2_btn.clicked.connect(self.bigscreen)
        # self.ui.reload_btn.clicked.connect(self.load_data_api)
        self.ui.accept_btn.clicked.connect(self.get_lot)
        self.ui.return_btn.clicked.connect(self.return_lot)
        self.ui.controller_z1_btn.clicked.connect(self.controller_z1_screen)
        self.ui.controller_z2_btn.clicked.connect(self.controller_z2_screen)
        self.ui.check_lot_btn.clicked.connect(self.check_lot_screen)
        self.ui.check_broken_btn.clicked.connect(self.check_broken_screen)
        self.ui.check_upbroken_btn.clicked.connect(self.check_upbroken_screen)
        self.ui.after_barier_btn.clicked.connect(self.after_barier_update)
        self.ui.clear_accept_db_btn.clicked.connect(self.clear_accept)
        self.ui.clear_return_db_btn.clicked.connect(self.clear_return)

        #btn update lot status Parked: normal and over height
        self.ui.all_lot_status_7_btn.clicked.connect(self.update_full_normal_lot)
        self.ui.all_oz_lot_status_7_btn.clicked.connect(self.update_full_oz_lot)
        
        #btn update lot status Empty: normal and over height
        self.ui.all_lot_status_1_btn.clicked.connect(self.update_empty_lot)
        self.ui.oz_lot_status_1_btn.clicked.connect(self.update_empty_lot_oz)

        self.ui.all_card_status_null_btn.clicked.connect(self.update_card_null_status_1)


    def on_icon_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_full_accept_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_icon_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_full_edit_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_icon_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_full_monitor_btn_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        

    def smallscreen(self):
        self.mainsmall = MainSmallWindow()    
        self.mainsmall.show()
    
    def bigscreen(self):
        self.mainbig = MainBigWindow()
        self.mainbig.show()

    def controller_z1_screen(self):
        self.mainz1 = MainComtrollerz1Window()
        self.mainz1.show()
    
    def controller_z2_screen(self):
        self.mainz2 = MainComtrollerz2Window()
        self.mainz2.show()

    def check_lot_screen(self):
        self.ui.maincheck = MainChecklotWindow()
        self.ui.maincheck.show()

    def check_broken_screen(self):
        self.ui.maincheck = MaincheckbrokenWindow()
        self.ui.maincheck.show()

    def check_upbroken_screen(self):
        self.ui.maincheck = MaincheckupbrokenWindow()
        self.ui.maincheck.show()
        
    
    #แก้ตรงนี้ไอ่ควาย
    def lot_status_check(self):

        empty_index.clear()

        mycursor = mydb.cursor()
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' ")
        all_empty_index = mycursor.fetchall()

        for empty_i in all_empty_index:
            empty_index.append(empty_i[0])
        # print(empty_index)
        
        try:
            if all(item == '' for item in empty_index):
                self.ui.full_lot_label.setStyleSheet("color: rgb(255, 0, 0);")
                self.ui.full_lot_label.setText("ช่องจอดเต็ม กรุณาจอดแบบลาน !!!!")
                 
            else:
                self.ui.full_lot_label.setStyleSheet("color: #00aa00;")
                self.ui.full_lot_label.setText("ช่องจอดว่าง !!!!")    
        except:
            self.ui.full_lot_label.setText("พบปัญหา แจ้ง Admin")
    

    def get_lot(self):
        #bay_a : bay_id='1'
        mycursor = mydb.cursor()
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='1' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            a.append(row[0])
        # print(a)
            
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='1' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            oha.append(row[0])
        # print(oha)
            
        #bay_b : bay_id='2'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='2' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            b.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='2' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohb.append(row[0])

        #bay_c : bay_id='3'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='3' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            c.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='3' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohc.append(row[0])

        #bay_d : bay_id='4'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='4' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            d.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='4' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohd.append(row[0])

        #bay_e : bay_id='5'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='5' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            e.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='5' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohe.append(row[0])

        #bay_f : bay_id='6'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='6' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            f.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='6' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohf.append(row[0])

        #bay_g : bay_id='7'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='7' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            g.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='7' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohg.append(row[0])

        #bay_h : bay_id='8'
        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='8' AND parking_type_id='0'")
        normal_zone_result=mycursor.fetchall()
        for row in normal_zone_result:
            h.append(row[0])

        mycursor.execute("SELECT number FROM lot WHERE status_id='1' AND bay_id='8' AND parking_type_id='1'")
        over_zone_result = mycursor.fetchall()
        for row in over_zone_result:
            ohh.append(row[0])
            
        data_api = []

        response = requests.get('http://127.0.0.1:8000/cars/1')
        api_noplate = str(response.json()['license_plate'])
        height=(199,180)
        api_height = random.choice(height)

        data_api.append(api_noplate)
        data_api.append(api_height)
        
        self.ui.api_hight_status_label.setText(str(api_height))
        
        
        car_height = int(data_api[1])
        parking_lot = None

        try:
            for _ in range(8):
                if car_height >= 190:
                    removed_element = bay_order.pop(0)
                    bay_order.append(removed_element)
                   
                    # ตรวจสอบ normal zone ถ้าเต็มให้ใช้ over zone แทน
                    # if len(oz[removed_element]) == 0:
                    #     continue
                    if len(oz[removed_element]) == 1:
                        # continue
                        if len(nz[removed_element]) == 0:
                            continue
                        else:
                            parking_lot = nz[removed_element].pop(1)
                    else:
                        parking_lot = oz[removed_element].pop(0)

                    # parking_lot = oz[removed_element].pop(0)
                    parked_lot.append(parking_lot)

                    self.ui.accept_show_zone_label.setText(z[removed_element[0]])
                    self.ui.accept_show_bay_label.setText(removed_element)
                    self.ui.accept_show_lot_label.setText(parking_lot)

                    lot_ready_to_db = parking_lot

                    old_lot_id = []
                    mycursor = mydb.cursor()
                    mycursor.execute('''SELECT lot_id FROM lot WHERE number = %s''', (lot_ready_to_db,))
                    old_data = mycursor.fetchone()
                    for row in old_data:
                        old_lot_id.append(row)

                    value = (old_data)
                    updatedb = '''UPDATE lot SET status_id ="3" WHERE lot_id = %s'''
                    try:
                        mycursor.execute(updatedb, value)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกไม่สำเร็จ")

                    card_id = self.ui.lineEdit.text()
                    id_now = old_data[0]
                    value2 = (id_now, card_id)
                    updatedb2 = '''UPDATE card SET lot_id = %s, status_id ="3" WHERE card_id = %s'''
                    try:
                        mycursor.execute(updatedb2, value2)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดไม่สำเร็จ")

                    license_plate_ready_to_get_lot = data_api[0]
                    height_plate_ready_to_get_lot = data_api[1]

                    value3 = (height_plate_ready_to_get_lot, license_plate_ready_to_get_lot, card_id)
                    updatedb3 = '''UPDATE card SET user_height = %s, user_license_plate = %s WHERE card_id = %s'''
                    mycursor.execute(updatedb3, value3)
                    mydb.commit()

                    data_to_insert_history = []

                    mycursor = mydb.cursor()
                    mycursor.execute('''
                        SELECT card.card_id, card.user_height, card.user_license_plate, lot.lot_id, card.time, lot.number
                        FROM lot
                        INNER JOIN card ON lot.lot_id = card.lot_id
                        WHERE lot.number = %s
                    ''', (lot_ready_to_db,))

                    card_data_to_history = mycursor.fetchall()

                    for row in card_data_to_history:
                        data_to_insert_history.append(row)

                    for data_row in data_to_insert_history:
                        card_id_in_list = data_row[0]
                        height_in_list = data_row[1]
                        lp_in_list = data_row[2]
                        lot_id_in_list = data_row[3]
                        timestamp_in_list = data_row[4]
                        mycursor.execute('''
                            INSERT INTO history
                            (his_id, card_id, height, license_plate, lot_id, time_in, time_out)
                            VALUES (NULL, %s, %s, %s, %s, %s, NULL)
                        ''', (card_id_in_list, height_in_list, lp_in_list, lot_id_in_list, timestamp_in_list))

                    mydb.commit()

                    a.clear()
                    b.clear()
                    c.clear()
                    d.clear()
                    e.clear()
                    f.clear()
                    g.clear()
                    h.clear()
                    oha.clear()
                    ohb.clear()
                    ohc.clear()
                    ohd.clear()
                    ohe.clear()
                    ohf.clear()
                    ohg.clear()
                    ohh.clear()
                    return parked_lot
                    
                else:
                    removed_element = bay_order.pop(0)            
                    bay_order.append(removed_element)

                    # if len(nz[removed_element])==0:
                    #     continue
                    # parking_lot = nz[removed_element].pop(0)
                    if len(nz[removed_element]) == 0:
                        # continue
                        if len(oz[removed_element]) == 0:
                            continue
                        else:
                            parking_lot = oz[removed_element].pop(0)
                    else:
                        parking_lot = nz[removed_element].pop(0)

                    parked_lot.append(parking_lot)
                    
                    self.ui.accept_show_zone_label.setText(z[removed_element[0]])
                    self.ui.accept_show_bay_label.setText(removed_element)
                    self.ui.accept_show_lot_label.setText(parking_lot)

                    #Element to use
                    lot_ready_to_db = parking_lot
                    # print(lot_ready_to_db)

                    old_lot_id = []
                    mycursor = mydb.cursor()
                    mycursor.execute('''
                                        SELECT lot_id FROM lot WHERE number=%s
                                        ''',(lot_ready_to_db,))
                    old_data = mycursor.fetchone()
                    for row in old_data:
                        old_lot_id.append(row)
                    # print('lot id :',old_lot_id)

                    #update lot status_id by lot_id from (old_data = mycursor.fetchone())
                    value = (old_data)
                    updatedb = ('''UPDATE lot SET status_id="3" WHERE lot_id=%s ''')
                    try:
                        mycursor.execute(updatedb, value)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกไม่สำเร็จ")

                     #อัพเดตข้อมูลช่องจอดลงใน card โดยล็อค card id
                    card_id = self.ui.lineEdit.text()
                    id_now = old_data[0]
                    value2 = (id_now, card_id)
                    updatedb2 =('''UPDATE card SET lot_id=%s, status_id="3" WHERE card_id=%s ''')
                    try:
                        mycursor.execute(updatedb2, value2)
                        mydb.commit()
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดสำเร็จ")
                    except:
                        self.ui.accept_status_label.setText("บันทึกลงการ์ดไม่สำเร็จ")
                    
                    licese_plate_ready_to_get_lot = data_api[0]
                    height_plate_ready_to_get_lot = data_api[1]

                    value3 = (height_plate_ready_to_get_lot, licese_plate_ready_to_get_lot,  card_id)
                    updatedb3 =('''UPDATE card SET user_height=%s,user_license_plate=%s WHERE card_id=%s ''')
                    mycursor.execute(updatedb3, value3)
                    mydb.commit()

                    #insert_data to history table
                    data_to_insert_history = []


                    mycursor = mydb.cursor()
                    mycursor.execute('''
                        SELECT card.card_id, card.user_height, card.user_license_plate, lot.lot_id, card.time, lot.number
                        FROM lot
                        INNER JOIN card ON lot.lot_id = card.lot_id 
                        WHERE lot.number = %s
                    ''', (lot_ready_to_db,))

                    card_data_to_history = mycursor.fetchall()

                    for row in card_data_to_history:
                        data_to_insert_history.append(row)

                    # print("data fetch", data_to_insert_history)

                    #insert time in
                    for data_row in data_to_insert_history:
                        card_id_in_list = data_row[0]
                        height_in_list = data_row[1]
                        lp_in_list = data_row[2]
                        lot_id_in_list = data_row[3]
                        timestamp_in_list = data_row[4]
                        mycursor.execute('''
                            INSERT INTO history 
                            (his_id, card_id, height, license_plate, lot_id, time_in, time_out) 
                            VALUES (NULL, %s, %s, %s, %s, %s, NULL)
                        ''', (card_id_in_list, height_in_list, lp_in_list, lot_id_in_list, timestamp_in_list))

                    mydb.commit()

                    a.clear()
                    b.clear()
                    c.clear()
                    d.clear()
                    e.clear()
                    f.clear()
                    g.clear()
                    h.clear()
                    oha.clear()
                    ohb.clear()
                    ohc.clear()
                    ohd.clear()
                    ohe.clear()
                    ohf.clear()
                    ohg.clear()
                    ohh.clear()
                    # print(parked_lot)
                    return parked_lot  
            return parking_lot
        except:
            self.ui.accept_status_label.setText("มีปัญหาในการรับช่องจอด")
        

    def after_barier_update(self):
        after_barier_data = []
        card_id_barier = self.ui.after_barier_edit.text()
        mycursor = mydb.cursor()
        try:
            mycursor.execute('''SELECT card.card_id, card.status_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number, lot.lot_id
            FROM lot
            INNER JOIN card ON lot.lot_id = card.lot_id                  
            INNER JOIN bay ON lot.bay_id = bay.bay_id
            WHERE card_id=%s ''', (card_id_barier,))
            data_to_update = mycursor.fetchone()
            
            if data_to_update:
                after_barier_data = data_to_update
                # print(after_barier_data)

                update_query_card = '''UPDATE card SET status_id='6' WHERE card_id=%s '''
                mycursor.execute(update_query_card, (after_barier_data[0],))
                mydb.commit()
                update_status_lot ='''UPDATE lot SET status_id='6' WHERE number=%s '''
                mycursor.execute(update_status_lot, (after_barier_data[6],))
                mydb.commit()
                self.ui.after_barier_status_label.setText("สำเร็จ")
            else:
                self.ui.after_barier_status_label.setText("ไม่พบข้อมูล")   
        except:
            self.ui.after_barier_status_label.setText("ไม่สำเร็จ")
        self.ui.after_barier_edit.clear()
    
    
    def return_lot(self):
        id_no = self.ui.return_edit.text()

        mycursor = mydb.cursor()
        mycursor.execute('''SELECT number, status_id FROM lot WHERE status_id=7 ''')
        old_return_data = mycursor.fetchall()
        for row in old_return_data:
            parked_lot.append(row[0])

        # print("information to return :",parked_lot)
        
        mycursor = mydb.cursor()
        mycursor.execute('''SELECT card.card_id, card.status_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number, lot.lot_id
            FROM lot
            INNER JOIN card ON lot.lot_id = card.lot_id                  
            INNER JOIN bay ON lot.bay_id = bay.bay_id
            WHERE card_id=%s ''', (id_no,))
        
        old_data = mycursor.fetchone()
        

        if old_data:
            card_id, status_id, user_height, user_license_plate, parked_zone, bay_name, number, lot_id = old_data

            # print("ข้อมูลที่จะคืน ที่ดึงจาก card id :", old_data)

            # Check if the lot number is in the list of parked_lot
            lot_no_list = number
            if lot_no_list in parked_lot:
                parked_lot_old.append(lot_no_list)
                # print("list old pk : ",parked_lot_old)
                # Construct and execute the SQL query to update the row for 'lot' table
                update_query_lot = "UPDATE lot SET status_id = '1' WHERE number = %s"
                mycursor.execute(update_query_lot, (lot_no_list,))
                mydb.commit()

                # Construct and execute the SQL query to update the row for 'card' table
                update_query_card = "UPDATE card SET user_height=%s, user_license_plate=%s, lot_id=%s, status_id='1' WHERE lot_id=%s"
                mycursor.execute(update_query_card, (None, None, None, lot_id))  # Assuming None means no lot assigned
                mydb.commit()

                # Insert time_out into history table
                mycursor.execute('''SELECT time FROM card WHERE card_id=%s''', (id_no,))
                card_time_out = mycursor.fetchone()

                if card_time_out:
                    # ดึงเวลาปัจจุบัน
                    current_time_out = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    # ปรับปรุงข้อมูลเวลาออกในตาราง history
                    mycursor.execute('''UPDATE history 
                                        SET time_out = %s 
                                        WHERE card_id = %s AND time_out IS NULL''', (current_time_out, id_no))
                    mydb.commit()

                parked_lot_old.clear()
                parked_lot.remove(lot_no_list)
                # print("old list after pop",parked_lot)
                # print("ข้อมูล lot หลังดึงข้อมูล:", current_time_out)
                # parked_lot.pop(parked_lot[str(lot_no_list)])
                # print("after return lot",parked_lot)
                self.ui.return_status_label.setText("คืนเรียบร้อย")
            else:
                self.ui.return_status_label.setText("ไม่เจอช่องจอดที่จอดไปแล้ว")
        else:
            self.ui.return_status_label.setText("ไม่มีหมายเลขการ์ดไอดีนี้")

    def update_full_normal_lot(self):
        mycursor = mydb.cursor()
        update_full_normal = "UPDATE lot SET status_id='7' WHERE parking_type_id='0' "
        mycursor.execute(update_full_normal)
        mydb.commit()

    def update_full_oz_lot(self):
        mycursor = mydb.cursor()
        update_full_oz = "UPDATE lot SET status_id='7' WHERE parking_type_id='1' "
        mycursor.execute(update_full_oz)
        mydb.commit()

    def update_empty_lot(self):
        mycursor = mydb.cursor()
        update_empty = "UPDATE lot SET status_id='1' WHERE parking_type_id='0' "
        mycursor.execute(update_empty)
        mydb.commit()

    def update_empty_lot_oz(self):
        mycursor = mydb.cursor()
        update_empty = "UPDATE lot SET status_id='1' WHERE parking_type_id='1' "
        mycursor.execute(update_empty)
        mydb.commit()

    def update_card_null_status_1(self):
        mycursor = mydb.cursor()
        update_card_null = "UPDATE card SET lot_id=NULL, status_id='1' "
        mycursor.execute(update_card_null)
        mydb.commit()

    def clear_accept(self):
        self.ui.lineEdit.clear()
        self.ui.accept_show_zone_label.clear()
        self.ui.accept_show_bay_label.clear()
        self.ui.accept_show_lot_label.clear()
        self.ui.accept_status_label.clear()
        self.ui.api_hight_status_label.clear()

    def clear_return(self):
        self.ui.return_edit.clear()
        self.ui.return_status_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    style_file = QFile("style_final.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    Window = MainWindow()
    Window.show()

    sys.exit(app.exec())