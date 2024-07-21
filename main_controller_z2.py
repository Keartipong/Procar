import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
import mysql.connector as mc
from PyQt5.QtCore import QTimer
import random

from controller_z2 import *

user_data_new=[]
bay_order=[]
zone_order=['1','2']

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

#nz = normal zone
nz={"A":a,"F":f,"C":c,"B":b,"G":g,"D":d,"H":h,"E":e}

# oz = over heigh zone
oz={"A":oha,"F":ohf,"C":ohc,"B":ohb,"G":ohg,"D":ohd,"H":ohh,"E":ohe}

z1={"A":zone_order[0],"B":zone_order[0]}
z2={"C":zone_order[1],"D":zone_order[1],"E":zone_order[1],"F":zone_order[1],"G":zone_order[1],"H":zone_order[1]}



class MainComtrollerz2Window(QMainWindow):
    def __init__(self):
        super(MainComtrollerz2Window, self).__init__()

        self.ui = Ui_MainControllerZ2Window()
        self.ui.setupUi(self)
        # self.call_lot()

        self.timer = QTimer()
        self.timer.start(2000)
        self.timer.timeout.connect(self.call_lot)
        
        

    def call_lot(self):
        user_data_old=[]
        
        card_id = self.ui.lineEdit.text()
        try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="carlot")
                mycursor = mydb.cursor()
                
                mycursor.execute('''
                    SELECT card.card_id, card.user_height, card.user_license_plate, lot.parked_zone, bay.bay_name, lot.number, lot.lot_id
                    FROM lot
                    INNER JOIN card ON lot.lot_id = card.lot_id                  
                    INNER JOIN bay ON lot.bay_id = bay.bay_id
                    WHERE card_id=%s
                    ''', (card_id,))
                result = mycursor.fetchone()

                for all_data in result:
                    user_data_old.append(all_data)
                

                mycursor.execute("SELECT bay_name FROM bay")
                result = mycursor.fetchall()
                for row in result:
                    bay_order.append(row[0])
                
                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='1' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_a in result:
                    oha.append(lot_a[0])
                # print(oha)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='1' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_a in result:
                    a.append(lot_a[0])
                # print(a)
                    
                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='2' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_b in result:
                    ohb.append(lot_b[0])
                # print(ohb)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='2' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_b in result:
                    b.append(lot_b[0])
                # print(b)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='3' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_c in result:
                    ohc.append(lot_c[0])
                # print(ohc)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='3' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_c in result:
                    c.append(lot_c[0])
                # print(c)
                    
                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='4' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_d in result:
                    ohd.append(lot_d[0])
                # print(ohd)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='4' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_d in result:
                    d.append(lot_d[0])
                # print(d)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='5' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_e in result:
                    ohe.append(lot_e[0])
                # print(ohe)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='5' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_e in result:
                    e.append(lot_e[0])
                # print(e)
                    
                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='6' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_f in result:
                    ohf.append(lot_f[0])
                # print(ohf)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='6' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_f in result:
                    f.append(lot_f[0])
                # print(f)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='7' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_g in result:
                    ohg.append(lot_g[0])
                # print(ohg)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='7' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_g in result:
                    g.append(lot_g[0])
                # print(g)
                    
                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='8' AND parking_type_id='1' ''')
                result = mycursor.fetchall()
                for lot_h in result:
                    ohh.append(lot_h[0])
                # print(ohh)

                mycursor.execute('''
                                    SELECT number FROM lot 
                                    WHERE status_id='1' AND bay_id='8' AND parking_type_id='0' ''')
                result = mycursor.fetchall()
                for lot_h in result:
                    h.append(lot_h[0])
                # print(h)


                old_zone_user = user_data_old[3]

                if old_zone_user==2:
                    self.ui.label_8.setText(str(user_data_old[0]))
                    self.ui.label_9.setText(str(user_data_old[2]))
                    self.ui.label_10.setText(str(user_data_old[1]))

                    self.ui.label_17.setText(str(user_data_old[3]))
                    self.ui.label_18.setText(str(user_data_old[4]))
                    self.ui.label_19.setText(str(user_data_old[5]))

                    #fetch lot_id by lot_number and replace new id in user_data_new
                    new_lot_id_to_update = user_data_old[5]
                    mycursor = mydb.cursor()
                    mycursor.execute('''SELECT lot_id FROM lot WHERE number=%s ''',(new_lot_id_to_update,))
                    data_id3 = mycursor.fetchone()
                    
                    #update lot_status in lot
                    value4 = (data_id3)
                    updatedb4 =('''UPDATE lot SET status_id="7" WHERE lot_id=%s ''')
                    mycursor.execute(updatedb4, value4)
                    mydb.commit()

                    #update card_id in card
                    id_to_up = user_data_old[0]
                    
                    mycursor = mydb.cursor()
                    mycursor.execute('''SELECT card_id FROM card WHERE card_id=%s ''',(id_to_up,))
                    data_id4 = mycursor.fetchone()

                    value5 = (data_id4)
                    updatedb5 =('''UPDATE card SET status_id="7" WHERE card_id=%s ''')
                    mycursor.execute(updatedb5, value5)
                    mydb.commit()
                    
                    # print("check3",user_data_old)
                    # print("check4",user_data_new)
                    
                    self.ui.status_label.setText("*กำลังเรียกช่องจอด")

                elif old_zone_user==1:
                    
                    if user_data_old[1] <= "190" and user_data_old[4] in z1:
                        random_bay = random.choice([bay for bay in bay_order if bay not in z1])
                        new_zone = z2[random_bay]
                        
                        random_lot = random.choice(nz[random_bay])
                        nz[random_bay].remove(random_lot)
                    elif user_data_old[1] > "190" and user_data_old[4] in z1:
                        random_bay = random.choice([bay for bay in bay_order if bay not in z1])
                        new_zone = z2[random_bay]

                        random_lot = random.choice(oz[random_bay])
                        oz[random_bay].remove(random_lot)

                    #append old zone in list user_data_new=[]
                    user_data_new.append(user_data_old[5])

                    #replace new data in user_data_old=[]
                    user_data_old[3] = int(new_zone)
                    user_data_old[4] = random_bay
                    user_data_old[5] = random_lot
                    
                    #fetch lot_id by lot_number and replace new id in user_data_old
                    old_lot_number = user_data_old[5]
                    mycursor2 = mydb.cursor()
                    mycursor2.execute('''SELECT lot_id FROM lot WHERE number=%s''',(old_lot_number,))
                    data_id = mycursor2.fetchone()

                    for row in data_id:
                        user_data_old[6] = data_id[0]
                    
                    #update new lot_id in card
                    user_id = user_data_old[0]
                    new_lot_id = user_data_old[6]
                
                    value = (new_lot_id, user_id)
                    updatedb =('''UPDATE card SET lot_id=%s WHERE card_id=%s ''')
                    mycursor.execute(updatedb, value)
                    mydb.commit()
                    #----------------------------------------------------------------
                    # update new_lot_status in lot
                    value1 = (data_id)
                    updatedb1 =('''UPDATE lot SET status_id="6" WHERE lot_id=%s ''')
                    mycursor.execute(updatedb1, value1)
                    mydb.commit()
                    #----------------------------------------------------------------
                    #update old lot to status 1:empty
                    update_old_lot_number = user_data_new[0]
                    mycursor2 = mydb.cursor()
                    mycursor2.execute('''SELECT lot_id FROM lot WHERE number=%s''',(update_old_lot_number,))
                    data_id2 = mycursor2.fetchone()

                    value2 = (data_id2)
                    updatedb2 =('''UPDATE lot SET status_id="1" WHERE lot_id=%s ''')
                    mycursor.execute(updatedb2, value2)
                    mydb.commit()
                    
                    # print("check1",user_data_old)
                    # print("check2",user_data_new)
                    #-----------------------------------------------------------------
            
                    self.ui.old_lot_label.setText(str(user_data_new[0]))
                    self.ui.status_label.setText("*กำลังหาช่องจอดใหม่")
                else:
                    self.ui.status_label.setText("*การหาช่องจอดใหม่มีปัญหา")
        except:
             self.ui.label_8.clear()
             self.ui.label_9.clear()
             self.ui.label_10.clear()
             self.ui.label_17.clear()
             self.ui.label_18.clear()
             self.ui.label_19.clear()
             self.ui.old_lot_label.clear()
             user_data_old.clear()
             user_data_new.clear()
             self.ui.status_label.setText("*ไม่มีการเรียกช่องจอด")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    controllerz1window = MainComtrollerz2Window()
    controllerz1window.show()
    
    sys.exit(app.exec())