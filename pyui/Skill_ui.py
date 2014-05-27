# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\Skill.ui'
#
# Created: Tue May 27 22:34:40 2014
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

class Ui_Skill(object):
    def setupUi(self, Skill):
        Skill.setObjectName(_fromUtf8("Skill"))
        Skill.resize(94, 180)
        self.gridLayout = QtGui.QGridLayout(Skill)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Skill)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(32, 32))
        self.label.setMaximumSize(QtCore.QSize(32, 32))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBoxLevel = QtGui.QSpinBox(Skill)
        self.spinBoxLevel.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxLevel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxLevel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxLevel.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spinBoxLevel.setProperty("value", 0)
        self.spinBoxLevel.setObjectName(_fromUtf8("spinBoxLevel"))
        self.gridLayout.addWidget(self.spinBoxLevel, 2, 0, 1, 1)
        self.spinBoxCost = QtGui.QSpinBox(Skill)
        self.spinBoxCost.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxCost.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxCost.setReadOnly(True)
        self.spinBoxCost.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxCost.setObjectName(_fromUtf8("spinBoxCost"))
        self.gridLayout.addWidget(self.spinBoxCost, 3, 0, 1, 1)
        self.spinBoxMax = QtGui.QSpinBox(Skill)
        self.spinBoxMax.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxMax.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxMax.setReadOnly(True)
        self.spinBoxMax.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxMax.setObjectName(_fromUtf8("spinBoxMax"))
        self.gridLayout.addWidget(self.spinBoxMax, 1, 0, 1, 1)
        self.spinBoxTotal = QtGui.QSpinBox(Skill)
        self.spinBoxTotal.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxTotal.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxTotal.setReadOnly(True)
        self.spinBoxTotal.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxTotal.setMaximum(9999)
        self.spinBoxTotal.setProperty("value", 0)
        self.spinBoxTotal.setObjectName(_fromUtf8("spinBoxTotal"))
        self.gridLayout.addWidget(self.spinBoxTotal, 4, 0, 1, 1)

        self.retranslateUi(Skill)
        QtCore.QMetaObject.connectSlotsByName(Skill)

    def retranslateUi(self, Skill):
        Skill.setWindowTitle(_translate("Skill", "Skill", None))
        self.spinBoxLevel.setToolTip(_translate("Skill", "The currently set level.", None))
        self.spinBoxCost.setStatusTip(_translate("Skill", "The cost for the next level up.", None))
        self.spinBoxMax.setToolTip(_translate("Skill", "The higherst level for the current char level.", None))
        self.spinBoxTotal.setToolTip(_translate("Skill", "The total amount of SP used for this Skill", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Skill = QtGui.QWidget()
    ui = Ui_Skill()
    ui.setupUi(Skill)
    Skill.show()
    sys.exit(app.exec_())

