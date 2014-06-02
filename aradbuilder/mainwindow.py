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

import ConfigParser
import os

from PyQt4.QtCore import (pyqtSlot)
from PyQt4.QtGui import (QMainWindow, QApplication, QListWidgetItem)

import build
import newdialog
from pyui.MainWindow_ui import Ui_MainWindow as MainWindowUI


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
        self.actionAdd.triggered.connect(self.getNewCharValues)
        self.actionSave.triggered.connect(self.saveBuilds)

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

    def createNewChar(self, name, mainClass, subClass, path):
        charBuild = build.Build(name, mainClass, subClass, path, self)

        self.stackedBuilds.addWidget(charBuild)
        self.listBuilds.addItem(QListWidgetItem(name))

        self.listBuilds.setCurrentRow(self.listBuilds.count() - 1)
        charBuild.nameChanged.connect(self.updateListName)

    def nameInList(self, name):
        return False

    @pyqtSlot(str)
    def updateListName(self, name):
        print name
        self.listBuilds.currentItem().setText(name)

    @pyqtSlot()
    def getNewCharValues(self):
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
            self.createNewChar(name, mainClass, subClass, path)




    @pyqtSlot()
    def saveBuilds(self):
        pathSaveParser = ConfigParser.SafeConfigParser()
        pathSaveParser.add_section('builds')

        for i in range(self.stackedBuilds.count()):
            saveParser = ConfigParser.SafeConfigParser()
            build = self.stackedBuilds.widget(i)
            name = str(build.lineEditName.text())
            saveParser.add_section('global')
            saveParser.set('global', 'name', name)
            saveParser.set('global', 'class', str(build.lineEditClass.text()))
            saveParser.set('global', 'job', str(build.lineEditSubClass.text()))
            saveParser.set('global', 'level', str(build.spinBoxLevel.value()))

            saveParser.add_section('SP')
            saveParser.add_section('TP')
            saveParser.add_section('QP')
            for skillBox in build.spDict.values():
                for skill in skillBox.skills.values():
                    if skill.spinBoxLevel.value() > 0:
                        saveParser.set('SP', skill.name,
                                       str(skill.spinBoxLevel.value()))
            for skillBox in build.tpDict.values():
                for skill in skillBox.skills.values():
                    if skill.spinBoxLevel.value() > 0:
                        saveParser.set('TP', skill.name,
                                       str(skill.spinBoxLevel.value()))
            for skillBox in build.qpDict.values():
                for skill in skillBox.skills.values():
                    if skill.spinBoxLevel.value() > 0:
                        saveParser.set('QP', skill.name,
                                       str(skill.spinBoxLevel.value()))

            path = os.path.join('saves', name + '.absf')

            with open(path, 'w') as f:
                saveParser.write(f)

            pathSaveParser.set('builds', name, path)

        path = os.path.join('saves', 'default.abpf')
        with open(path, 'w') as f:
            pathSaveParser.write(f)


if __name__ == '__main__':
    import sys

    launchGui(sys.argv)
