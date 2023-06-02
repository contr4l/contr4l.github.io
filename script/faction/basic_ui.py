# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 392)
        Form.setStyleSheet("background-color: rgb(218, 218, 163);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 14pt \"黑体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.key = QtWidgets.QLineEdit(Form)
        self.key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.key.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("font: 14pt \"黑体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.faction_name = QtWidgets.QComboBox(Form)
        self.faction_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.faction_name.setStyleSheet("font: 14pt \"黑体\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.faction_name.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.faction_name.setIconSize(QtCore.QSize(16, 16))
        self.faction_name.setObjectName("faction_name")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.faction_name.addItem("")
        self.gridLayout.addWidget(self.faction_name, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("font: 14pt \"黑体\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.faction_id_opt = QtWidgets.QLineEdit(Form)
        self.faction_id_opt.setObjectName("faction_id_opt")
        self.gridLayout.addWidget(self.faction_id_opt, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 600 10pt \"黑体\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Torn Spy"))
        self.label.setText(_translate("Form", "Key"))
        self.label_2.setText(_translate("Form", "Faction"))
        self.faction_name.setItemText(0, _translate("Form", "CCRC"))
        self.faction_name.setItemText(1, _translate("Form", "PTA"))
        self.faction_name.setItemText(2, _translate("Form", "PN"))
        self.faction_name.setItemText(3, _translate("Form", "SH"))
        self.faction_name.setItemText(4, _translate("Form", "NOV"))
        self.faction_name.setItemText(5, _translate("Form", "BSU"))
        self.faction_name.setItemText(6, _translate("Form", "Others"))
        self.label_3.setText(_translate("Form", "Faction_ID (Optional)"))
        self.faction_id_opt.setStyleSheet(_translate("Form", "font: 14pt \"黑体\";\n"
                                                     "background-color: rgb(255, 255, 255);"))
        self.pushButton.setText(_translate("Form", "Spy!"))
        self.label_4.setText(_translate("Form", "Faction_ID仅当目标帮派\n"
                                        "为Others时才需要填写"))
