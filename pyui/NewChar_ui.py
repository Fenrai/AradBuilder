# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\NewChar.ui'
#
# Created: Tue May 27 23:59:06 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewCharacter(object):
    def setupUi(self, NewCharacter):
        NewCharacter.setObjectName(_fromUtf8("NewCharacter"))
        NewCharacter.resize(335, 600)
        self.verticalLayout = QtGui.QVBoxLayout(NewCharacter)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelClassName = QtGui.QLabel(NewCharacter)
        self.labelClassName.setMinimumSize(QtCore.QSize(317, 225))
        self.labelClassName.setMaximumSize(QtCore.QSize(317, 225))
        self.labelClassName.setFrameShape(QtGui.QFrame.Panel)
        self.labelClassName.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelClassName.setLineWidth(2)
        self.labelClassName.setText(_fromUtf8(""))
        self.labelClassName.setObjectName(_fromUtf8("labelClassName"))
        self.verticalLayout.addWidget(self.labelClassName)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelName = QtGui.QLabel(NewCharacter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.lineEditName = QtGui.QLineEdit(NewCharacter)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelClassPicture = QtGui.QLabel(NewCharacter)
        self.labelClassPicture.setMinimumSize(QtCore.QSize(81, 58))
        self.labelClassPicture.setMaximumSize(QtCore.QSize(81, 58))
        self.labelClassPicture.setFrameShape(QtGui.QFrame.Panel)
        self.labelClassPicture.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelClassPicture.setText(_fromUtf8(""))
        self.labelClassPicture.setObjectName(_fromUtf8("labelClassPicture"))
        self.gridLayout.addWidget(self.labelClassPicture, 0, 2, 2, 1)
        self.labelClass = QtGui.QLabel(NewCharacter)
        self.labelClass.setObjectName(_fromUtf8("labelClass"))
        self.gridLayout.addWidget(self.labelClass, 1, 0, 1, 1)
        self.comboClass = QtGui.QComboBox(NewCharacter)
        self.comboClass.setObjectName(_fromUtf8("comboClass"))
        self.gridLayout.addWidget(self.comboClass, 1, 1, 1, 1)
        self.labelJob = QtGui.QLabel(NewCharacter)
        self.labelJob.setObjectName(_fromUtf8("labelJob"))
        self.gridLayout.addWidget(self.labelJob, 2, 0, 1, 1)
        self.comboSubClass = QtGui.QComboBox(NewCharacter)
        self.comboSubClass.setObjectName(_fromUtf8("comboSubClass"))
        self.gridLayout.addWidget(self.comboSubClass, 2, 1, 1, 1)
        self.labelCustomPath = QtGui.QLabel(NewCharacter)
        self.labelCustomPath.setObjectName(_fromUtf8("labelCustomPath"))
        self.gridLayout.addWidget(self.labelCustomPath, 3, 0, 1, 1)
        self.lineEditCustompicture = QtGui.QLineEdit(NewCharacter)
        self.lineEditCustompicture.setObjectName(_fromUtf8("lineEditCustompicture"))
        self.gridLayout.addWidget(self.lineEditCustompicture, 3, 1, 1, 1)
        self.toolButtonCustomPath = QtGui.QToolButton(NewCharacter)
        self.toolButtonCustomPath.setObjectName(_fromUtf8("toolButtonCustomPath"))
        self.gridLayout.addWidget(self.toolButtonCustomPath, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.labelCharPicture = QtGui.QLabel(NewCharacter)
        self.labelCharPicture.setMinimumSize(QtCore.QSize(300, 200))
        self.labelCharPicture.setMaximumSize(QtCore.QSize(300, 200))
        self.labelCharPicture.setFrameShape(QtGui.QFrame.StyledPanel)
        self.labelCharPicture.setFrameShadow(QtGui.QFrame.Raised)
        self.labelCharPicture.setLineWidth(2)
        self.labelCharPicture.setText(_fromUtf8(""))
        self.labelCharPicture.setScaledContents(True)
        self.labelCharPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCharPicture.setObjectName(_fromUtf8("labelCharPicture"))
        self.verticalLayout.addWidget(self.labelCharPicture)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonCancel = QtGui.QPushButton(NewCharacter)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.pushButtonCreate = QtGui.QPushButton(NewCharacter)
        self.pushButtonCreate.setObjectName(_fromUtf8("pushButtonCreate"))
        self.horizontalLayout.addWidget(self.pushButtonCreate)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NewCharacter)
        QtCore.QMetaObject.connectSlotsByName(NewCharacter)

    def retranslateUi(self, NewCharacter):
        NewCharacter.setWindowTitle(_translate("NewCharacter", "Create New Character", None))
        self.labelName.setText(_translate("NewCharacter", "Name:", None))
        self.labelClass.setText(_translate("NewCharacter", "Class:", None))
        self.labelJob.setText(_translate("NewCharacter", "Job:", None))
        self.labelCustomPath.setText(_translate("NewCharacter", "Custom Path:", None))
        self.toolButtonCustomPath.setText(_translate("NewCharacter", "...", None))
        self.buttonCancel.setText(_translate("NewCharacter", "Cancel", None))
        self.pushButtonCreate.setText(_translate("NewCharacter", "Create", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewCharacter = QtGui.QDialog()
    ui = Ui_NewCharacter()
    ui.setupUi(NewCharacter)
    NewCharacter.show()
    sys.exit(app.exec_())
