# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MainWindow.ui'
#
# Created: Mon Jun 02 01:08:13 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listBuilds = QtGui.QListWidget(self.centralwidget)
        self.listBuilds.setMinimumSize(QtCore.QSize(150, 0))
        self.listBuilds.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listBuilds.setObjectName(_fromUtf8("listBuilds"))
        self.gridLayout.addWidget(self.listBuilds, 0, 0, 1, 1)
        self.stackedBuilds = QtGui.QStackedWidget(self.centralwidget)
        self.stackedBuilds.setObjectName(_fromUtf8("stackedBuilds"))
        self.gridLayout.addWidget(self.stackedBuilds, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuConfugure = QtGui.QMenu(self.menubar)
        self.menuConfugure.setObjectName(_fromUtf8("menuConfugure"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuEdit.addAction(self.actionAdd)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionDelete)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConfugure.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.listBuilds, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.stackedBuilds.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AradBuilder", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuConfugure.setTitle(_translate("MainWindow", "Confugure", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+Shift+N", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSaveAs.setText(_translate("MainWindow", "SaveAs", None))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.actionAdd.setText(_translate("MainWindow", "Add", None))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Shift+Del", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

