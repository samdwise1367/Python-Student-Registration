from PyQt5 import QtCore, QtGui, QtWidgets
from database import Db #importing database.py
from home import Ui_MainWindow
from signup import Ui_Dialog


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(597, 356)
        Dialog.setStyleSheet("QDialog{background-color:\n"
"\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))}\n"
"\n"
"QLineEdit{\n"
"background-color:rgb(170, 255, 127)\n"
"\n"
"}\n"
"\n"
"QLabel#label_Heading{\n"
"font: 75 25pt \"Century Schoolbook L\";\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"font: 75 italic 14pt \"Century Schoolbook L\";\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 160, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 151, 21))
        self.label_2.setObjectName("label_2")
        self.txtUsername = QtWidgets.QLineEdit(Dialog)
        self.txtUsername.setGeometry(QtCore.QRect(300, 160, 191, 27))
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        ################## make the password invisible ############
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword.setGeometry(QtCore.QRect(300, 190, 191, 27))
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(210, 250, 71, 41))
        self.btnLogin.setObjectName("btnLogin")
        #################### Login Button funtion #######################
        self.btnLogin.clicked.connect(self.loginCheck)
        #################################################################
        self.btnSignup = QtWidgets.QPushButton(Dialog)
        self.btnSignup.setGeometry(QtCore.QRect(290, 250, 81, 41))
        self.btnSignup.setObjectName("btnSignup")
        #################### SignUp Button #############################
        self.btnSignup.clicked.connect(self.signupButton)
        ################################################################
        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(150, 90, 381, 51))
        self.label_Heading.setObjectName("label_Heading")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "UserName:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.btnLogin.setText(_translate("Dialog", "Login"))
        self.btnSignup.setText(_translate("Dialog", "SignUp"))
        self.label_Heading.setText(_translate("Dialog", "Student Login Form"))
        
    def welcomePage(self):
        self.homWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.homWindow)
        self.homWindow.show()
        
    def loginCheck(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        getDb = Db()        
        result = getDb.loginCheck(username,password)
        if(result):
            self.welcomePage()
            self.clearField()
            print(result)
        else:
            print("password wrong")
            self.showMessage("Warning","Invalid Username and Password")
            
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def signupButton(self):   
        self.signDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.signDialog)
        self.signDialog.show()
                
    def clearField(self):
        self.txtUsername.setText(None)
        self.txtPassword.setText(None)
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

