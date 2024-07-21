import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QListWidget, QVBoxLayout
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="",
    database="carlot")

class MaincheckupbrokenWindow(QMainWindow):
    def __init__(self):
        super(MaincheckupbrokenWindow, self).__init__()
        self.setWindowTitle("List Lot Error")
        self.setGeometry(500, 500, 1000, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.populate_list()

        self.select_button = QPushButton("Select")
        self.select_button.clicked.connect(self.update_selected_items_status)  # แก้ไขชื่อเมธอดเป็น update_selected_items_status
        self.layout.addWidget(self.select_button)

    def populate_list(self):
        items = ["1=A101", "2=A102", "3=A103", "4=A104", "5=A201", "6=A202", "7=A203", "8=A204", 
            "9=A301", "10=A302", "11=A303", "12=A304", "13=A401", "14=A402", "15=A403", "16=A404", 
            "17=A501", "18=A502", "19=A503", "20=A504", "21=A601", "22=A602", "23=A603", "24=A604", 
            "25=A701", "26=A702", "27=A703", "28=A704", "29=A705", "30=B101", "31=B102", "32=B103", "33=B104", 
            "34=B201", "35=B202", "36=B203", "37=B204", "38=B301", "39=B302", "40=B303", "41=B304", 
            "42=B401", "43=B402", "44=B403", "45=B404", "46=B501", "47=B502", "48=B503", "49=B504", 
            "50=B601", "51=B602", "52=B603", "53=B604", "54=B701", "55=B702", "56=B703", "57=B704", "58=B705", 
            "59=C101", "60=C102", "61=C103", "62=C104", "63=C201", "64=C202", "65=C203", "66=C204", 
            "67=C301", "68=C302", "69=C303", "70=C304", "71=C401", "72=C402", "73=C403", "74=C404", 
            "75=C501", "76=C502", "77=C503", "78=C504", "79=C601", "80=C602", "81=C603", "82=C604", 
            "83=C701", "84=C702", "85=C703", "86=C704", "87=C705", "88=D101", "89=D102", "90=D103", "91=D104", 
            "92=D201", "93=D202", "94=D203", "95=D204", "96=D301", "97=D302", "98=D303", "99=D304", 
            "100=D401", "101=D402", "102=D403", "103=D404", "104=D501", "105=D502", "106=D503", "107=D504", 
            "108=D601", "109=D602", "110=D603", "111=D604", "112=D701", "113=D702", "114=D703", "115=D704", "116=D705", 
            "117=E101", "118=E102", "119=E103", "120=E104", "121=E201", "122=E202", "123=E203", "124=E204", 
            "125=E301", "126=E302", "127=E303", "128=E304", "129=E401", "130=E402", "131=E403", "132=E404", 
            "133=E501", "134=E502", "135=E503", "136=E504", "137=E601", "138=E602", "139=E603", "140=E604", 
            "141=E701", "142=E702", "143=E703", "144=E704", "145=E705", "146=F101", "147=F102", "148=F103", "149=F104", 
            "150=F201", "151=F202", "152=F203", "153=F204", "154=F301", "155=F302", "156=F303", "157=F304", 
            "158=F401", "159=F402", "160=F403", "161=F404", "162=F501", "163=F502", "164=F503", "165=F504", 
            "166=F601", "167=F602", "168=F603", "169=F604", "170=F701", "171=F702", "172=F703", "173=F704", "174=F705", 
            "175=G101", "176=G102", "177=G103", "178=G104", "179=G201", "180=G202", "181=G203", "182=G204", 
            "183=G301", "184=G302", "185=G303", "186=G304", "187=G401", "188=G402", "189=G403", "190=G404", 
            "191=G501", "192=G502", "193=G503", "194=G504", "195=G601", "196=G602", "197=G603", "198=G604", 
            "199=G701", "200=G702", "201=G703", "202=G704", "203=G705", "204=H101", "205=H102", "206=H103", "207=H104", 
            "208=H201", "209=H202", "210=H203", "211=H204", "212=H301", "213=H302", "214=H303", "215=H304", 
            "216=H401", "217=H402", "218=H403", "219=H404", "220=H501", "221=H502", "222=H503", "223=H504", 
            "224=H601", "225=H602", "226=H603", "227=H604", "228=H701", "229=H702", "230=H703", "231=H704", "232=H705"
        ]
        for item in items:
            self.list_widget.addItem(item)

    def update_selected_items_status(self):
        selected_items = self.list_widget.selectedItems()
        if selected_items:
            try:
                with mydb.cursor() as mycursor:
                    for item in selected_items:
                        selected_item = item.text()
                        print("Selected Item:", selected_item)
                        update_reserve_item = '''UPDATE lot SET status_id='6' WHERE lot_id=%s'''
                        mycursor.execute(update_reserve_item, (selected_item,))
                        mydb.commit()
                        print(f"Status for Item {selected_item} Updated Successfully!")
            except mc.Error as err:
                print(f"Error: {err}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaincheckupbrokenWindow()
    window.show()
    sys.exit(app.exec_())
