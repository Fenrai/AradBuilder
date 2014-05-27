#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Device Settings Backup Tool (DSBT)
# Copyright (C) 2013 Stefan Rainow
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

from PyQt4.QtCore import (pyqtSlot)
from PyQt4.QtGui import (QMainWindow, QApplication, QListWidgetItem)

from pyui.MainWindow_ui import Ui_MainWindow as MainWindowUI
import ConfigParser
import newdialog
import build
import os

def launchGui(argv=None):
    if argv is None:
        argv = sys.argv()
    app = QApplication(argv)
    window = MainWindow()

    window.show()

    app.exec_()


class MainWindow(QMainWindow, MainWindowUI):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createDictionaries()
        self.createConnections()

    def createDictionaries(self):
        self.dictSP = self.getPointsDict('SP')
        self.dictTP = self.getPointsDict('TP')

    def createConnections(self):
        self.actionAdd.triggered.connect(self.createNewChar)

    def getPointsDict(self, key):
        pDict = {}
        pointsParser = ConfigParser.SafeConfigParser()
        pointsParser.read(os.path.join('skills', 'Points.abp'))

        for i in range(1, len(pointsParser.options(key)) + 1):
            if i == 1:
                pDict[i] = int(pointsParser.get(key, str(i)))
            else:
                pDict[i] = pDict[i - 1] + int(pointsParser.get(key, str(i)))

        return pDict

    @pyqtSlot()
    def createNewChar(self):
        newDialog = newdialog.NewDialog()
        if newDialog.exec_():
            name = newDialog.lineEditName.text()
            mainClass = str(newDialog.comboClass.currentText())
            subClass = str(newDialog.comboSubClass.currentText())
            customPath = newDialog.lineEditCustomPicture.text()
            if customPath == '':
                path = os.path.join("classes", mainClass, subClass + '.png')
            else:
                path = customPath

            charBuild = build.Build(name, mainClass, subClass, path, self)

            self.stackedBuilds.addWidget(charBuild)
            self.listBuilds.addItem(QListWidgetItem(name))

            self.listBuilds.setCurrentRow(self.listBuilds.count() - 1)

if __name__ == '__main__':
    import sys

    launchGui(sys.argv)
