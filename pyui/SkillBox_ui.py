# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SkillBox.ui'
#
# Created: Tue Jun  3 14:19:43 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SkillBox(object):
    def setupUi(self, SkillBox):
        SkillBox.setObjectName(_fromUtf8("SkillBox"))
        SkillBox.resize(94, 198)
        self.mainLayout = QtGui.QHBoxLayout(SkillBox)
        self.mainLayout.setSpacing(3)
        self.mainLayout.setContentsMargins(0, 6, 0, 0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(2, -1, 2, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(SkillBox)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SkillBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(SkillBox)
        self.label.setMinimumSize(QtCore.QSize(0, 32))
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(SkillBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(SkillBox)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.widget = QtGui.QWidget(SkillBox)
        self.widget.setMinimumSize(QtCore.QSize(0, 3))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 3))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)

        self.retranslateUi(SkillBox)
        QtCore.QMetaObject.connectSlotsByName(SkillBox)

    def retranslateUi(self, SkillBox):
        SkillBox.setWindowTitle(QtGui.QApplication.translate("SkillBox", "SkillBox", None, QtGui.QApplication.UnicodeUTF8))
        SkillBox.setTitle(QtGui.QApplication.translate("SkillBox", "SkillBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SkillBox", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SkillBox", "Max:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SkillBox", "Skill:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SkillBox", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SkillBox", "Cost:", None, QtGui.QApplication.UnicodeUTF8))

