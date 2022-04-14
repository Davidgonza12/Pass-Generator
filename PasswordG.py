#Author : Eliel Gonzalez

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(667, 497)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(-10, 10, 611, 501))
        self.widget_2.setObjectName("widget_2")
        self.label_fondo = QtWidgets.QLabel(self.widget_2)
        self.label_fondo.setGeometry(QtCore.QRect(70, 20, 480, 365))
        self.label_fondo.setStyleSheet("border-image: url(:/images/image.jpg);\n"
"border-radius:10px;")
        self.label_fondo.setText("")
        self.label_fondo.setObjectName("label_fondo")
        self.label_gradiente = QtWidgets.QLabel(self.widget_2)
        self.label_gradiente.setGeometry(QtCore.QRect(70, 20, 480, 365))
        self.label_gradiente.setStyleSheet("background-color: rgb(0, 0, 0,30);\n"
"border-radius:10px;")
        self.label_gradiente.setText("")
        self.label_gradiente.setObjectName("label_gradiente")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(70, 20, 480, 365))
        self.widget.setObjectName("widget")
        self.cb_mayus = QtWidgets.QCheckBox(self.widget)
        self.cb_mayus.setGeometry(QtCore.QRect(10, 70, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cb_mayus.setFont(font)
        self.cb_mayus.setAutoFillBackground(False)
        self.cb_mayus.setStyleSheet("\n"
"QCheckBox::indicator:unchecked{\n"
"background-color: rgb(255, 255, 255);\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ),stop:1  rgb(40, 67, 98,200));\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.cb_mayus.setAutoRepeat(False)
        self.cb_mayus.setAutoExclusive(False)
        self.cb_mayus.setObjectName("cb_mayus")
        self.cb_minus = QtWidgets.QCheckBox(self.widget)
        self.cb_minus.setGeometry(QtCore.QRect(10, 120, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb_minus.setFont(font)
        self.cb_minus.setStyleSheet("\n"
"QCheckBox::indicator:unchecked{\n"
"background-color: rgb(255, 255, 255);\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ),stop:1  rgb(40, 67, 98,200));\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}")
        self.cb_minus.setObjectName("cb_minus")
        self.cb_numeros = QtWidgets.QCheckBox(self.widget)
        self.cb_numeros.setGeometry(QtCore.QRect(10, 170, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb_numeros.setFont(font)
        self.cb_numeros.setStyleSheet("\n"
"QCheckBox::indicator:unchecked{\n"
"background-color: rgb(255, 255, 255);\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ),stop:1  rgb(40, 67, 98,200));\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}")
        self.cb_numeros.setObjectName("cb_numeros")
        self.cb_simbolos = QtWidgets.QCheckBox(self.widget)
        self.cb_simbolos.setGeometry(QtCore.QRect(10, 220, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cb_simbolos.setFont(font)
        self.cb_simbolos.setStyleSheet("\n"
"QCheckBox::indicator:unchecked{\n"
"background-color: rgb(255, 255, 255);\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ),stop:1  rgb(40, 67, 98,200));\n"
"    width : 18px;\n"
"    height : 18px;\n"
"    border-radius : 8px;\n"
"    border : 1px solid black;\n"
"}")
        self.cb_simbolos.setObjectName("cb_simbolos")
        self.slider_long = QtWidgets.QSlider(self.widget)
        self.slider_long.setGeometry(QtCore.QRect(300, 110, 131, 31))
        self.slider_long.setStyleSheet("QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: rgb(255, 90, 90);\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    height: 20px;\n"
"    width:20px;\n"
"    margin: -9px 0;\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ),stop:1  rgb(40, 67, 98,200));\n"
"\n"
"}    \n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background:  rgb(210,210, 210);\n"
"    border-radius: 2px;\n"
"    background-color:  rgb(194, 194, 194);\n"
"    \n"
"}")
        self.slider_long.setOrientation(QtCore.Qt.Horizontal)
        self.slider_long.setObjectName("slider_long")
        self.lbl_titulo_long = QtWidgets.QLabel(self.widget)
        self.lbl_titulo_long.setGeometry(QtCore.QRect(300, 70, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo_long.setFont(font)
        self.lbl_titulo_long.setObjectName("lbl_titulo_long")
        self.lbl_titulo_pass = QtWidgets.QLabel(self.widget)
        self.lbl_titulo_pass.setGeometry(QtCore.QRect(10, 320, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo_pass.setFont(font)
        self.lbl_titulo_pass.setObjectName("lbl_titulo_pass")
        self.lbl_vis = QtWidgets.QLabel(self.widget)
        self.lbl_vis.setGeometry(QtCore.QRect(430, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_vis.setFont(font)
        self.lbl_vis.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 90, 90);\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        self.lbl_vis.setObjectName("lbl_vis")
        self.btn_generar = QtWidgets.QPushButton(self.widget)
        self.btn_generar.setGeometry(QtCore.QRect(10, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_generar.setFont(font)
        self.btn_generar.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ,219),stop:1  rgb(255, 90, 90)); \n"
"    color: rgb(255, 255, 255,210);\n"
"    border-radius:5px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ,195),stop:1  rgb(255, 90, 90)); \n"
"    \n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98 ,195),stop:1  rgb(255, 90, 90)); \n"
"    \n"
"    \n"
"}")
        self.btn_generar.setObjectName("btn_generar")
        self.titulo1 = QtWidgets.QLabel(self.widget)
        self.titulo1.setGeometry(QtCore.QRect(170, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo1.setFont(font)
        self.titulo1.setStyleSheet("color: rgb(255, 90, 90);")
        self.titulo1.setObjectName("titulo1")
        self.titulo2 = QtWidgets.QLabel(self.widget)
        self.titulo2.setGeometry(QtCore.QRect(250, 30, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.titulo2.setFont(font)
        self.titulo2.setObjectName("titulo2")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgb(255, 90, 90,95),stop:1  rgb(255, 90, 90,80)); \n"
"    color: rgb(255, 255, 255,210);\n"
"    border-top-right-radius:10px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgb(255, 90, 90,75),stop:1  rgb(255, 90, 90,60)); \n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgb(255, 90, 90,75),stop:1  rgb(255, 90, 90,60)); \n"
"    \n"
"    \n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(420, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgb(40, 67, 98 ,95),stop:1  rgb(40, 67, 98 ,80)); \n"
"border: none;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgb(40, 67, 98 ,80),stop:1  rgb(40, 67, 98 ,65)); \n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  rgb(40, 67, 98 ,80),stop:1  rgb(40, 67, 98 ,65)); \n"
"    \n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.ln_pass = QtWidgets.QLineEdit(self.widget)
        self.ln_pass.setGeometry(QtCore.QRect(120, 290, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ln_pass.setFont(font)
        self.ln_pass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(255, 90, 90);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"padding-bottom:4px;")
        self.ln_pass.setText("")
        self.ln_pass.setObjectName("ln_pass")

        self.retranslateUi(Form)
        self.pushButton_12.clicked.connect(Form.close)
        self.pushButton.clicked.connect(Form.hide)
        self.slider_long.valueChanged['int'].connect(self.lbl_vis.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cb_mayus.setText(_translate("Form", "M A Y Ú S C U L A S"))
        self.cb_minus.setText(_translate("Form", "M I N Ú S C U L A S"))
        self.cb_numeros.setText(_translate("Form", "N Ú M E R O S"))
        self.cb_simbolos.setText(_translate("Form", "S Í M B O L O S "))
        self.lbl_titulo_long.setText(_translate("Form", "LONGITUD DE LA CONTRASEÑA"))
        self.lbl_titulo_pass.setText(_translate("Form", "CONTRASEÑA:"))
        self.lbl_vis.setText(_translate("Form", " 0"))
        self.btn_generar.setText(_translate("Form", "G E N E R A R"))
        self.titulo1.setText(_translate("Form", "P A S S"))
        self.titulo2.setText(_translate("Form", "G E N E R A T O R"))
        self.pushButton_12.setText(_translate("Form", "X"))
        self.pushButton.setText(_translate("Form", "-"))
        self.ln_pass.setPlaceholderText(_translate("Form", "             CONTRASEÑA        "))
