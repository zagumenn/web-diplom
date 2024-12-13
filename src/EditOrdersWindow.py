# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditOrdersWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 715)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEditOrderWindow = QtWidgets.QLabel(self.centralwidget)
        self.labelEditOrderWindow.setGeometry(QtCore.QRect(300, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelEditOrderWindow.setFont(font)
        self.labelEditOrderWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.labelEditOrderWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEditOrderWindow.setObjectName("labelEditOrderWindow")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(590, 550, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(70, 490, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("background-color: rgb(255, 172, 0);")
        self.AddButton.setObjectName("AddButton")
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(420, 290, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditButton.setFont(font)
        self.EditButton.setStyleSheet("background-color: rgb(255, 172, 0);")
        self.EditButton.setObjectName("EditButton")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(760, 240, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("background-color: rgb(255, 172, 0);")
        self.DeleteButton.setObjectName("DeleteButton")
        self.textAddDriverId = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddDriverId.setGeometry(QtCore.QRect(70, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddDriverId.setFont(font)
        self.textAddDriverId.setObjectName("textAddDriverId")
        self.textAddPrice = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddPrice.setGeometry(QtCore.QRect(70, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddPrice.setFont(font)
        self.textAddPrice.setObjectName("textAddPrice")
        self.textAddDataId = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddDataId.setGeometry(QtCore.QRect(70, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddDataId.setFont(font)
        self.textAddDataId.setObjectName("textAddDataId")
        self.textAddUserId = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddUserId.setGeometry(QtCore.QRect(70, 240, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddUserId.setFont(font)
        self.textAddUserId.setObjectName("textAddUserId")
        self.textAddCarId = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddCarId.setGeometry(QtCore.QRect(70, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddCarId.setFont(font)
        self.textAddCarId.setObjectName("textAddCarId")
        self.textDeleteId = QtWidgets.QTextEdit(self.centralwidget)
        self.textDeleteId.setGeometry(QtCore.QRect(760, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textDeleteId.setFont(font)
        self.textDeleteId.setObjectName("textDeleteId")
        self.textEditOrderId = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditOrderId.setGeometry(QtCore.QRect(420, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditOrderId.setFont(font)
        self.textEditOrderId.setObjectName("textEditOrderId")
        self.textEditStatusId = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditStatusId.setGeometry(QtCore.QRect(420, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditStatusId.setFont(font)
        self.textEditStatusId.setObjectName("textEditStatusId")
        self.labelOrderAdd = QtWidgets.QLabel(self.centralwidget)
        self.labelOrderAdd.setGeometry(QtCore.QRect(30, 130, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelOrderAdd.setFont(font)
        self.labelOrderAdd.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.labelOrderAdd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOrderAdd.setObjectName("labelOrderAdd")
        self.labelOrderEdit = QtWidgets.QLabel(self.centralwidget)
        self.labelOrderEdit.setGeometry(QtCore.QRect(360, 130, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelOrderEdit.setFont(font)
        self.labelOrderEdit.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.labelOrderEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOrderEdit.setObjectName("labelOrderEdit")
        self.labelOrderDelete = QtWidgets.QLabel(self.centralwidget)
        self.labelOrderDelete.setGeometry(QtCore.QRect(700, 130, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelOrderDelete.setFont(font)
        self.labelOrderDelete.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.labelOrderDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOrderDelete.setObjectName("labelOrderDelete")
        self.textAddStartPlace = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddStartPlace.setGeometry(QtCore.QRect(70, 440, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddStartPlace.setFont(font)
        self.textAddStartPlace.setObjectName("textAddStartPlace")
        self.textAddEndPLace = QtWidgets.QTextEdit(self.centralwidget)
        self.textAddEndPLace.setGeometry(QtCore.QRect(290, 440, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textAddEndPLace.setFont(font)
        self.textAddEndPLace.setObjectName("textAddEndPLace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Окно изменения заказов"))
        self.labelEditOrderWindow.setText(_translate("MainWindow", "Окно изменения заказов"))
        self.ExitButton.setText(_translate("MainWindow", "Выйти"))
        self.AddButton.setText(_translate("MainWindow", "Добавить"))
        self.EditButton.setText(_translate("MainWindow", "Изменить"))
        self.DeleteButton.setText(_translate("MainWindow", "Удалить"))
        self.textAddDriverId.setPlaceholderText(_translate("MainWindow", "Введите driver_id"))
        self.textAddPrice.setPlaceholderText(_translate("MainWindow", "Введите цену"))
        self.textAddDataId.setPlaceholderText(_translate("MainWindow", "Введите дату"))
        self.textAddUserId.setPlaceholderText(_translate("MainWindow", "Введите user_id"))
        self.textAddCarId.setPlaceholderText(_translate("MainWindow", "Введите car_id"))
        self.textDeleteId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditOrderId.setPlaceholderText(_translate("MainWindow", "Введите id"))
        self.textEditStatusId.setPlaceholderText(_translate("MainWindow", "Введите id статуса"))
        self.labelOrderAdd.setText(_translate("MainWindow", "Добавить Заказ"))
        self.labelOrderEdit.setText(_translate("MainWindow", "Изменить статус заказа"))
        self.labelOrderDelete.setText(_translate("MainWindow", "Удалить заказ"))
        self.textAddStartPlace.setPlaceholderText(_translate("MainWindow", "Введите starting_place"))
        self.textAddEndPLace.setPlaceholderText(_translate("MainWindow", "Введите end_place"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
