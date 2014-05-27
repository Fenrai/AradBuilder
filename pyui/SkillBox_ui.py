# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\SkillBox.ui'
#
# Created: Tue May 27 22:34:54 2014
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

class Ui_SkillBox(object):
    def setupUi(self, SkillBox):
        SkillBox.setObjectName(_fromUtf8("SkillBox"))
        SkillBox.resize(94, 155)
        SkillBox.setTitle(_fromUtf8(""))
        self.mainLayout = QtGui.QHBoxLayout(SkillBox)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 6)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SkillBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SkillBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(SkillBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(SkillBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(SkillBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)

        self.retranslateUi(SkillBox)
        QtCore.QMetaObject.connectSlotsByName(SkillBox)

    def retranslateUi(self, SkillBox):
        SkillBox.setWindowTitle(_translate("SkillBox", "SkillBox", None))
        self.label.setText(_translate("SkillBox", "Skill:", None))
        self.label_2.setText(_translate("SkillBox", "MaxLevel:", None))
        self.label_3.setText(_translate("SkillBox", "Level:", None))
        self.label_4.setText(_translate("SkillBox", "Cost:", None))
        self.label_5.setText(_translate("SkillBox", "Total:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SkillBox = QtGui.QGroupBox()
    ui = Ui_SkillBox()
    ui.setupUi(SkillBox)
    SkillBox.show()
    sys.exit(app.exec_())

