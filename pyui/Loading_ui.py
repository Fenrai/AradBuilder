# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\Loading.ui'
#
# Created: Thu Jun 19 16:09:55 2014
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

class Ui_Load(object):
    def setupUi(self, Load):
        Load.setObjectName(_fromUtf8("Load"))
        Load.resize(318, 264)
        self.verticalLayout = QtGui.QVBoxLayout(Load)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelPicture = QtGui.QLabel(Load)
        self.labelPicture.setMinimumSize(QtCore.QSize(300, 200))
        self.labelPicture.setMaximumSize(QtCore.QSize(300, 200))
        self.labelPicture.setText(_fromUtf8(""))
        self.labelPicture.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelPicture.setObjectName(_fromUtf8("labelPicture"))
        self.verticalLayout.addWidget(self.labelPicture)
        self.labelText = QtGui.QLabel(Load)
        self.labelText.setObjectName(_fromUtf8("labelText"))
        self.verticalLayout.addWidget(self.labelText)
        self.progressBar = QtGui.QProgressBar(Load)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Load)
        QtCore.QMetaObject.connectSlotsByName(Load)

    def retranslateUi(self, Load):
        Load.setWindowTitle(_translate("Load", "Loading Builds", None))
        self.labelText.setText(_translate("Load", "Loading Saved Builds...", None))

