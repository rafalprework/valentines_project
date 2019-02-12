import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QFrame, QRadioButton, QComboBox, QPushButton, \
    QCheckBox, QPlainTextEdit, QMessageBox


#ctrl+d duplicate

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        self.lblName = QLabel('Imię*', self)
        self.lblName.move(20,20)
        self.txtName = QLineEdit(self)
        self.txtName.setPlaceholderText("Imię")
        self.txtName.move(20,50)

        self.lblSurname = QLabel('Nazwisko*', self)
        self.lblSurname.move(20,80)
        self.txtSurname = QLineEdit(self)
        self.txtSurname.setPlaceholderText("Nazwisko")
        self.txtSurname.move(20, 110)

        self.lblJobTitle = QLabel('Stanowisko*', self)
        self.lblJobTitle.move(20, 140)
        self.txtJobTitle = QLineEdit(self)
        self.txtJobTitle.setPlaceholderText("Stanowisko")
        self.txtJobTitle.move(20, 170)

        self.lblMail = QLabel('e-mail*', self)
        self.lblMail.move(20, 210)
        self.txtMail = QLineEdit(self)
        self.txtMail.setPlaceholderText("Adres e-mail")
        self.txtMail.move(20, 240)


        self.lblGender = QLabel('Wybierz płeć', self)
        self.lblGender.move(20, 270)

        gender = QFrame(self)
        self.rbMale = QRadioButton("Mężczyzna", gender)
        self.rbMale.move(20, 300)
        self.rbFemale = QRadioButton("Kobieta", gender)
        self.rbFemale.setChecked(True)
        self.rbFemale.move(20, 330)



        self.lblLang = QLabel('Jakie znasz języki programowania?', self)
        self.lblLang.move(220, 20)

        self.checkBoxJava = QCheckBox("Java", self)
        self.checkBoxJava.move(220, 50)

        self.checkBoxPython = QCheckBox("Python", self)
        self.checkBoxPython.move(220, 80)

        self.checkBoxOther = QCheckBox("inne", self)
        self.checkBoxOther.move(220, 110)

        self.lblEngSkill = QLabel('Wybierz poziom języka angielskiego', self)
        self.lblEngSkill.move(220, 140)

        self.cbEng = QComboBox(self)
        self.cbEng.addItem("Podstawowy")
        self.cbEng.addItem("Średnio-zaawansowany")
        self.cbEng.addItem("Zaawansowany")
        self.cbEng.move(220, 170)

        self.lblChooseCourse = QLabel('Wybierz kurs programowania?', self)
        self.lblChooseCourse.move(220, 200)

        self.cbCourse = QComboBox(self)
        self.cbCourse.addItem("Frontend developer")
        self.cbCourse.addItem("Backend developer")
        self.cbCourse.addItem("Android developer")
        self.cbCourse.addItem("Analityk danych")
        self.cbCourse.move(220, 230)

        self.cmntBox = QPlainTextEdit(self)
        self.cmntBox.move(500, 20)


        btnSubmit = QPushButton("Wypisz", self)
        btnSubmit.setToolTip('Wyslij formularz')
        btnSubmit.move(20, 360)
        btnSubmit.clicked.connect(self.sendAction)


        btnExit = QPushButton("Wyjdz", self)
        btnExit.setToolTip('Zamknij aplikcję')
        btnExit.move(150, 360)
        btnExit.clicked.connect(self.close)

        self.lblInfo = QLabel('* Pola obowiązkowe', self)
        self.lblInfo.move(20, 390)


        self.setGeometry(300, 300, 800, 430)
        self.setWindowTitle('Rejestracja na kurs')
        self.show()


    def sendAction(self):
        language = ""
        if self.checkBoxJava.isChecked():
            language = language + ' java'
        else:
            ""
        if self.checkBoxPython.isChecked():
            language = language + ' python'
        else:
            ""
        if self.checkBoxOther.isChecked():
            language = language + " inne"
        else:
            ""
        if (self.txtName.text() and self.txtSurname.text()) and (self.txtJobTitle and self.txtMail.text()):
            gender = "Kobieta"
            if (self.rbMale.isChecked()):
                gender = "Mężczyzna"

            self.cmntBox.appendPlainText("%s | %s | %s | %s | %s | %s | %s | %s\n" %
                  (self.txtName.text(), self.txtSurname.text(), self.txtJobTitle.text(), self.txtMail.text(),  gender, language ,self.cbEng.currentText(), self.cbCourse.currentText()))
        else:
            QMessageBox.about(self, "Uwaga", "Uzupełnij obowiązkowe pola")


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
