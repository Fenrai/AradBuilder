# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\Skill.ui'
#
# Created: Tue Jun 10 00:09:47 2014
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
        Skill.resize(94, 165)
        self.gridLayout = QtGui.QGridLayout(Skill)
        self.gridLayout.setContentsMargins(2, 0, 2, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spinBoxMax = QtGui.QSpinBox(Skill)
        self.spinBoxMax.setEnabled(True)
        self.spinBoxMax.setMinimumSize(QtCore.QSize(40, 25))
        self.spinBoxMax.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBoxMax.setAutoFillBackground(False)
        self.spinBoxMax.setStyleSheet(_fromUtf8("QSpinBox{color: rgb(255, 0, 0)};"))
        self.spinBoxMax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBoxMax.setFrame(True)
        self.spinBoxMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxMax.setReadOnly(True)
        self.spinBoxMax.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxMax.setObjectName(_fromUtf8("spinBoxMax"))
        self.gridLayout.addWidget(self.spinBoxMax, 1, 0, 1, 1)
        self.spinBoxLevel = QtGui.QSpinBox(Skill)
        self.spinBoxLevel.setMinimumSize(QtCore.QSize(40, 25))
        self.spinBoxLevel.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBoxLevel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinBoxLevel.setAutoFillBackground(False)
        self.spinBoxLevel.setStyleSheet(_fromUtf8("QSpinBox{color: rgb(0, 0, 0); font-weight:bold;};"))
        self.spinBoxLevel.setWrapping(False)
        self.spinBoxLevel.setFrame(True)
        self.spinBoxLevel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxLevel.setReadOnly(False)
        self.spinBoxLevel.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.spinBoxLevel.setProperty("value", 0)
        self.spinBoxLevel.setObjectName(_fromUtf8("spinBoxLevel"))
        self.gridLayout.addWidget(self.spinBoxLevel, 2, 0, 1, 1)
        self.labelPic = QtGui.QLabel(Skill)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPic.sizePolicy().hasHeightForWidth())
        self.labelPic.setSizePolicy(sizePolicy)
        self.labelPic.setMinimumSize(QtCore.QSize(32, 32))
        self.labelPic.setMaximumSize(QtCore.QSize(32, 32))
        self.labelPic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelPic.setFrameShape(QtGui.QFrame.Box)
        self.labelPic.setFrameShadow(QtGui.QFrame.Raised)
        self.labelPic.setLineWidth(2)
        self.labelPic.setText(_fromUtf8(""))
        self.labelPic.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPic.setObjectName(_fromUtf8("labelPic"))
        self.gridLayout.addWidget(self.labelPic, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBoxCost = QtGui.QSpinBox(Skill)
        self.spinBoxCost.setEnabled(True)
        self.spinBoxCost.setMinimumSize(QtCore.QSize(40, 25))
        self.spinBoxCost.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBoxCost.setStyleSheet(_fromUtf8("QSpinBox{color: rgb(0, 0,255)};"))
        self.spinBoxCost.setFrame(True)
        self.spinBoxCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxCost.setReadOnly(True)
        self.spinBoxCost.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxCost.setObjectName(_fromUtf8("spinBoxCost"))
        self.gridLayout.addWidget(self.spinBoxCost, 3, 0, 1, 1)
        self.spinBoxTotal = QtGui.QSpinBox(Skill)
        self.spinBoxTotal.setEnabled(True)
        self.spinBoxTotal.setMinimumSize(QtCore.QSize(40, 25))
        self.spinBoxTotal.setMaximumSize(QtCore.QSize(40, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.spinBoxTotal.setPalette(palette)
        self.spinBoxTotal.setStyleSheet(_fromUtf8("QSpinBox{color: rgb(0, 170, 0)};"))
        self.spinBoxTotal.setFrame(True)
        self.spinBoxTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBoxTotal.setReadOnly(True)
        self.spinBoxTotal.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxTotal.setMaximum(9999)
        self.spinBoxTotal.setProperty("value", 0)
        self.spinBoxTotal.setObjectName(_fromUtf8("spinBoxTotal"))
        self.gridLayout.addWidget(self.spinBoxTotal, 5, 0, 1, 1)
        self.line = QtGui.QFrame(Skill)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)

        self.retranslateUi(Skill)
        QtCore.QMetaObject.connectSlotsByName(Skill)

    def retranslateUi(self, Skill):
        Skill.setWindowTitle(_translate("Skill", "Skill", None))
        self.spinBoxMax.setToolTip(_translate("Skill", "The higherst level for the current char level.", None))
        self.spinBoxLevel.setToolTip(_translate("Skill", "The currently set level.", None))
        self.spinBoxCost.setStatusTip(_translate("Skill", "The cost for the next level up.", None))
        self.spinBoxTotal.setToolTip(_translate("Skill", "The total amount of SP used for this Skill", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Skill = QtGui.QWidget()
    ui = Ui_Skill()
    ui.setupUi(Skill)
    Skill.show()
    sys.exit(app.exec_())

