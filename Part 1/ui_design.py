# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/abdulroqeeb/Documents/Larlem/Replicating Macbook Calc App/macbook-calculator-pyqt/design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 307)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 240, 311))
        self.frame.setStyleSheet("background-color: rgb(37, 38, 56);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 60, 241, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 240, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.frame_4.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.reset = QtWidgets.QPushButton(self.frame_4)
        self.reset.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.reset.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.reset.setObjectName("reset")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(60, 0, 60, 50))
        self.frame_5.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.sign = QtWidgets.QPushButton(self.frame_5)
        self.sign.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.sign.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.sign.setObjectName("sign")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(120, 0, 60, 50))
        self.frame_6.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.percent = QtWidgets.QPushButton(self.frame_6)
        self.percent.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.percent.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.percent.setObjectName("percent")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(180, 0, 60, 50))
        self.frame_7.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.divide = QtWidgets.QPushButton(self.frame_7)
        self.divide.setGeometry(QtCore.QRect(0, 0, 60, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.divide.setFont(font)
        self.divide.setStyleSheet("font: 25pt \".AppleSystemUIFont\";\n"
"background-color: rgb(245, 137, 13);\n"
"color: rgb(255, 238, 216);")
        self.divide.setObjectName("divide")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setGeometry(QtCore.QRect(0, 50, 240, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.frame_9.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.seven = QtWidgets.QPushButton(self.frame_9)
        self.seven.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.seven.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.seven.setObjectName("seven")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setGeometry(QtCore.QRect(60, 0, 60, 50))
        self.frame_10.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.eight = QtWidgets.QPushButton(self.frame_10)
        self.eight.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.eight.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.eight.setObjectName("eight")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setGeometry(QtCore.QRect(120, 0, 60, 50))
        self.frame_11.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.nine = QtWidgets.QPushButton(self.frame_11)
        self.nine.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.nine.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.nine.setObjectName("nine")
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setGeometry(QtCore.QRect(180, 0, 60, 50))
        self.frame_12.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.multiply = QtWidgets.QPushButton(self.frame_12)
        self.multiply.setGeometry(QtCore.QRect(0, 0, 60, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("font: 25pt \".AppleSystemUIFont\";\n"
"background-color: rgb(245, 137, 13);\n"
"color: rgb(255, 238, 216);")
        self.multiply.setObjectName("multiply")
        self.frame_13 = QtWidgets.QFrame(self.frame_2)
        self.frame_13.setGeometry(QtCore.QRect(0, 100, 240, 50))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.frame_14.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.four = QtWidgets.QPushButton(self.frame_14)
        self.four.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.four.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.four.setObjectName("four")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setGeometry(QtCore.QRect(60, 0, 60, 50))
        self.frame_15.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.five = QtWidgets.QPushButton(self.frame_15)
        self.five.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.five.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.five.setObjectName("five")
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        self.frame_16.setGeometry(QtCore.QRect(120, 0, 60, 50))
        self.frame_16.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.six = QtWidgets.QPushButton(self.frame_16)
        self.six.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.six.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.six.setObjectName("six")
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        self.frame_17.setGeometry(QtCore.QRect(180, 0, 60, 50))
        self.frame_17.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.subtract = QtWidgets.QPushButton(self.frame_17)
        self.subtract.setGeometry(QtCore.QRect(0, 0, 60, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.subtract.setFont(font)
        self.subtract.setStyleSheet("font: 25pt \".AppleSystemUIFont\";\n"
"background-color: rgb(245, 137, 13);\n"
"color: rgb(255, 238, 216);")
        self.subtract.setObjectName("subtract")
        self.frame_18 = QtWidgets.QFrame(self.frame_2)
        self.frame_18.setGeometry(QtCore.QRect(0, 150, 240, 50))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.frame_19.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.one = QtWidgets.QPushButton(self.frame_19)
        self.one.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.one.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.one.setObjectName("one")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setGeometry(QtCore.QRect(60, 0, 60, 50))
        self.frame_20.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.two = QtWidgets.QPushButton(self.frame_20)
        self.two.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.two.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.two.setObjectName("two")
        self.frame_21 = QtWidgets.QFrame(self.frame_18)
        self.frame_21.setGeometry(QtCore.QRect(120, 0, 60, 50))
        self.frame_21.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.three = QtWidgets.QPushButton(self.frame_21)
        self.three.setGeometry(QtCore.QRect(-1, 0, 61, 50))
        self.three.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.three.setObjectName("three")
        self.frame_22 = QtWidgets.QFrame(self.frame_18)
        self.frame_22.setGeometry(QtCore.QRect(180, 0, 60, 50))
        self.frame_22.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.add = QtWidgets.QPushButton(self.frame_22)
        self.add.setGeometry(QtCore.QRect(0, 0, 60, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.add.setFont(font)
        self.add.setStyleSheet("font: 25pt \".AppleSystemUIFont\";\n"
"background-color: rgb(245, 137, 13);\n"
"color: rgb(255, 238, 216);")
        self.add.setObjectName("add")
        self.frame_23 = QtWidgets.QFrame(self.frame_2)
        self.frame_23.setGeometry(QtCore.QRect(0, 200, 240, 50))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        self.frame_24.setGeometry(QtCore.QRect(0, 0, 121, 50))
        self.frame_24.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.zero = QtWidgets.QPushButton(self.frame_24)
        self.zero.setGeometry(QtCore.QRect(0, 0, 121, 50))
        self.zero.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.zero.setObjectName("zero")
        self.frame_26 = QtWidgets.QFrame(self.frame_23)
        self.frame_26.setGeometry(QtCore.QRect(120, 0, 60, 50))
        self.frame_26.setStyleSheet("background-color: rgb(82, 82, 98);")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.dot = QtWidgets.QPushButton(self.frame_26)
        self.dot.setGeometry(QtCore.QRect(0, 0, 60, 50))
        self.dot.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(221, 220, 225);")
        self.dot.setObjectName("dot")
        self.frame_27 = QtWidgets.QFrame(self.frame_23)
        self.frame_27.setGeometry(QtCore.QRect(180, 0, 60, 50))
        self.frame_27.setStyleSheet("background-color: rgb(54, 55, 72);")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.equal = QtWidgets.QPushButton(self.frame_27)
        self.equal.setGeometry(QtCore.QRect(0, 0, 60, 50))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.equal.setFont(font)
        self.equal.setStyleSheet("font: 25pt \".AppleSystemUIFont\";\n"
"background-color: rgb(245, 137, 13);\n"
"color: rgb(255, 238, 216);")
        self.equal.setObjectName("equal")
        self.display = QtWidgets.QLabel(self.frame)
        self.display.setGeometry(QtCore.QRect(0, 0, 240, 60))
        self.display.setStyleSheet("font: 40pt \".AppleSystemUIFont\";\n"
"color: rgb(248, 238, 216);")
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.reset.setText(_translate("Form", "AC"))
        self.sign.setText(_translate("Form", "+/-"))
        self.percent.setText(_translate("Form", "%"))
        self.divide.setText(_translate("Form", "÷"))
        self.seven.setText(_translate("Form", "7"))
        self.eight.setText(_translate("Form", "8"))
        self.nine.setText(_translate("Form", "9"))
        self.multiply.setText(_translate("Form", "x"))
        self.four.setText(_translate("Form", "4"))
        self.five.setText(_translate("Form", "5"))
        self.six.setText(_translate("Form", "6"))
        self.subtract.setText(_translate("Form", "-"))
        self.one.setText(_translate("Form", "1"))
        self.two.setText(_translate("Form", "2"))
        self.three.setText(_translate("Form", "3"))
        self.add.setText(_translate("Form", "+"))
        self.zero.setText(_translate("Form", "0"))
        self.dot.setText(_translate("Form", "."))
        self.equal.setText(_translate("Form", "="))
        self.display.setText(_translate("Form", "0"))
