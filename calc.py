# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(370, 470)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Calculator.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 10, 330, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.outputLabel.setFont(font)
        self.outputLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.outputLabel.setMouseTracking(False)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setOpenExternalLinks(False)
        self.outputLabel.setObjectName("outputLabel")
        self.button_back = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.remove())
        self.button_back.setGeometry(QtCore.QRect(188, 100, 78, 61))
        self.button_back.setObjectName("button_back")
        self.button_division = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("/"))
        self.button_division.setGeometry(QtCore.QRect(272, 100, 78, 61))
        self.button_division.setObjectName("button_division")
        self.button_percent = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("%"))
        self.button_percent.setGeometry(QtCore.QRect(104, 100, 78, 61))
        self.button_percent.setObjectName("button_percent")
        self.button_clear = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("Clear"))
        self.button_clear.setGeometry(QtCore.QRect(20, 100, 78, 61))
        self.button_clear.setObjectName("button_clear")
        self.button_five = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("5"))
        self.button_five.setGeometry(QtCore.QRect(104, 240, 78, 61))
        self.button_five.setObjectName("button_five")
        self.button_four = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("4"))
        self.button_four.setGeometry(QtCore.QRect(20, 240, 78, 61))
        self.button_four.setObjectName("button_four")
        self.button_six = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("6"))
        self.button_six.setGeometry(QtCore.QRect(188, 240, 78, 61))
        self.button_six.setObjectName("button_six")
        self.button_minus = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("-"))
        self.button_minus.setGeometry(QtCore.QRect(272, 240, 78, 61))
        self.button_minus.setObjectName("button_minus")
        self.button_zero = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("0"))
        self.button_zero.setGeometry(QtCore.QRect(20, 380, 78, 61))
        self.button_zero.setObjectName("button_zero")
        self.button_dot = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.dot())
        self.button_dot.setGeometry(QtCore.QRect(188, 380, 78, 61))
        self.button_dot.setObjectName("button_dot")
        self.button_equal = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.equal())
        self.button_equal.setGeometry(QtCore.QRect(272, 380, 78, 61))
        self.button_equal.setObjectName("button_equal")
        self.button_nine = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("9"))
        self.button_nine.setGeometry(QtCore.QRect(188, 170, 78, 61))
        self.button_nine.setObjectName("button_nine")
        self.button_seven = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("7"))
        self.button_seven.setGeometry(QtCore.QRect(20, 170, 78, 61))
        self.button_seven.setObjectName("button_seven")
        self.button_eight = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("8"))
        self.button_eight.setGeometry(QtCore.QRect(104, 170, 78, 61))
        self.button_eight.setObjectName("button_eight")
        self.button_duplicate = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("*"))
        self.button_duplicate.setGeometry(QtCore.QRect(272, 170, 78, 61))
        self.button_duplicate.setObjectName("button_duplicate")
        self.button_three = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("3"))
        self.button_three.setGeometry(QtCore.QRect(188, 310, 78, 61))
        self.button_three.setObjectName("button_three")
        self.button_two = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("2"))
        self.button_two.setGeometry(QtCore.QRect(104, 310, 78, 61))
        self.button_two.setObjectName("button_two")
        self.button_minusplus = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.PlusAndMinus())
        self.button_minusplus.setGeometry(QtCore.QRect(104, 380, 78, 61))
        self.button_minusplus.setObjectName("button_minusplus")
        self.button_one = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("1"))
        self.button_one.setGeometry(QtCore.QRect(20, 310, 78, 61))
        self.button_one.setObjectName("button_one")
        self.button_plus = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.click_btn("+"))
        self.button_plus.setGeometry(QtCore.QRect(272, 310, 78, 61))
        self.button_plus.setObjectName("button_plus")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate(
            "Calculator", "Calculator by Peter"))
        self.button_back.setText(_translate("Calculator", "<<"))
        self.button_division.setText(_translate("Calculator", "/"))
        self.button_percent.setText(_translate("Calculator", "%"))
        self.button_clear.setText(_translate("Calculator", "C"))
        self.button_five.setText(_translate("Calculator", "5"))
        self.button_four.setText(_translate("Calculator", "4"))
        self.button_six.setText(_translate("Calculator", "6"))
        self.button_minus.setText(_translate("Calculator", "-"))
        self.button_zero.setText(_translate("Calculator", "0"))
        self.button_dot.setText(_translate("Calculator", "."))
        self.button_equal.setText(_translate("Calculator", "="))
        self.button_nine.setText(_translate("Calculator", "9"))
        self.button_seven.setText(_translate("Calculator", "7"))
        self.button_eight.setText(_translate("Calculator", "8"))
        self.button_duplicate.setText(_translate("Calculator", "*"))
        self.button_three.setText(_translate("Calculator", "3"))
        self.button_two.setText(_translate("Calculator", "2"))
        self.button_one.setText(_translate("Calculator", "1"))
        self.button_plus.setText(_translate("Calculator", "+"))
        self.button_minusplus.setText(_translate("Calculator", "+/-"))

    def click_btn(self, pressed):
        if pressed == 'Clear':
            return self.outputLabel.setText('')
        else:
            return self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def dot(self):
        check_dot_in = self.outputLabel.text()
        if check_dot_in[-1] == ".":
            pass
        else:
            return self.outputLabel.setText(f'{check_dot_in}.')

    def remove(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]

        return self.outputLabel.setText(screen)

    def PlusAndMinus(self):
        screen = self.outputLabel.text()

        if screen[-1] == '-':
            return self.outputLabel.setText(f'{screen}')
        elif screen[0] == '-':
            screen = screen[1:]
            return self.outputLabel.setText(f'{screen}')

        else:
            return self.outputLabel.setText(f'-{screen}')

    def equal(self):
        screen = self.outputLabel.text()

        try:
            answer = eval(screen)
            return self.outputLabel.setText(str(answer))

        except:
            return self.outputLabel.setText('Error!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())