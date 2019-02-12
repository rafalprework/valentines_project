import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QFrame, QRadioButton, QComboBox, QPushButton


#ctrl+d duplicate

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.lblInfo = QLabel('Imię', self)
        self.lblInfo.move(20,20)
        self.txtName = QLineEdit(self)
        self.txtPhone = QLineEdit(self)
        self.txtName.setPlaceholderText("Imię")
        self.txtPhone.setPlaceholderText("Numer telefonu")
        self.txtName.move(20,50)
        self.txtPhone.move(20,80)
        self.setGeometry(300, 300, 300, 300)

        gender= QFrame(self)
        self.rbMale = QRadioButton("Male", gender)
        self.rbMale.move(20, 110)

        self.rbFemale = QRadioButton("Female", gender)
        self.rbFemale.setChecked(True)
        self.rbFemale.move(100, 110)

        self.cbActivity = QComboBox(self)
        self.cbActivity.addItem("Kino")
        self.cbActivity.addItem("Kolacja")
        self.cbActivity.addItem("Programowanie")
        self.cbActivity.move(20, 140)


        btnSubmit = QPushButton("Wyślij", self)
        btnSubmit.setToolTip('Wyslij formularz')
        btnSubmit.move(20,170)

        btnSubmit.clicked.connect(self.sendAction)

        self.setWindowTitle('Walentynki')
        self.show()


    def sendAction(self):
        if (self.txtName.text() and self.txtPhone.text()):
            gender = "Female"
            if (self.rbMale.isChecked()):
                gender = "Male"
            print("%15s   | %10s   | %10s   | %20s" %
                  (self.txtName.text(), self.txtPhone.text(), gender, self.cbActivity.currentText()))
            self.lblInfo.setText("dzieki za zapisanie sie")
        else:
            self.lblInfo.setText("Uzupelnij brakujące pola")


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
