# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SkillBox.ui'
#
# Created: Wed Jun  4 18:33:32 2014
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
        self.labelTotal = QtGui.QLabel(SkillBox)
        self.labelTotal.setMinimumSize(QtCore.QSize(0, 25))
        self.labelTotal.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
        self.gridLayout.addWidget(self.labelTotal, 5, 0, 1, 1)
        self.labelMax = QtGui.QLabel(SkillBox)
        self.labelMax.setMinimumSize(QtCore.QSize(0, 25))
        self.labelMax.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelMax.setObjectName(_fromUtf8("labelMax"))
        self.gridLayout.addWidget(self.labelMax, 1, 0, 1, 1)
        self.labelSkill = QtGui.QLabel(SkillBox)
        self.labelSkill.setMinimumSize(QtCore.QSize(0, 32))
        self.labelSkill.setMaximumSize(QtCore.QSize(16777215, 32))
        self.labelSkill.setObjectName(_fromUtf8("labelSkill"))
        self.gridLayout.addWidget(self.labelSkill, 0, 0, 1, 1)
        self.labelLevel = QtGui.QLabel(SkillBox)
        self.labelLevel.setMinimumSize(QtCore.QSize(0, 25))
        self.labelLevel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelLevel.setObjectName(_fromUtf8("labelLevel"))
        self.gridLayout.addWidget(self.labelLevel, 2, 0, 1, 1)
        self.labelCost = QtGui.QLabel(SkillBox)
        self.labelCost.setMinimumSize(QtCore.QSize(0, 25))
        self.labelCost.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelCost.setObjectName(_fromUtf8("labelCost"))
        self.gridLayout.addWidget(self.labelCost, 3, 0, 1, 1)
        self.widgetSpacer = QtGui.QWidget(SkillBox)
        self.widgetSpacer.setMinimumSize(QtCore.QSize(0, 3))
        self.widgetSpacer.setMaximumSize(QtCore.QSize(16777215, 3))
        self.widgetSpacer.setObjectName(_fromUtf8("widgetSpacer"))
        self.gridLayout.addWidget(self.widgetSpacer, 4, 0, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)

        self.retranslateUi(SkillBox)
        QtCore.QMetaObject.connectSlotsByName(SkillBox)

    def retranslateUi(self, SkillBox):
        SkillBox.setWindowTitle(QtGui.QApplication.translate("SkillBox", "SkillBox", None, QtGui.QApplication.UnicodeUTF8))
        SkillBox.setTitle(QtGui.QApplication.translate("SkillBox", "SkillBox", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTotal.setText(QtGui.QApplication.translate("SkillBox", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMax.setText(QtGui.QApplication.translate("SkillBox", "Max:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSkill.setText(QtGui.QApplication.translate("SkillBox", "Skill:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLevel.setText(QtGui.QApplication.translate("SkillBox", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCost.setText(QtGui.QApplication.translate("SkillBox", "Cost:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SkillBox = QtGui.QGroupBox()
    ui = Ui_SkillBox()
    ui.setupUi(SkillBox)
    SkillBox.show()
    sys.exit(app.exec_())

