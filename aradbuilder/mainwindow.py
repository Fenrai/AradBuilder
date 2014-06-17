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
from PyQt4.QtGui import (QMainWindow, QApplication, QListWidgetItem,
    QMessageBox, QFileDialog, QIcon)

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
        loadParser = ConfigParser.SafeConfigParser()
        loadParser.read(os.path.join('saves', 'default.abpf'))
        for option in loadParser.options('builds'):
            self.loadBuild(loadParser.get('builds', option))
        self.setWindowIcon(QIcon(os.path.join('ARAD.ico')))
        self.loadSettings()

    def createDictionaries(self):
        self.dictSP = self.getPointsDict('SP')
        self.dictTP = self.getPointsDict('TP')

    def createConnections(self):
        self.actionAdd.triggered.connect(self.getNewCharValues)
        self.actionSave.triggered.connect(self.saveBuilds)
        self.actionShowMax.toggled.connect(self.updateMaxVisibility)
        self.actionShowCost.toggled.connect(self.updateCostVisibility)
        self.actionShowTotal.toggled.connect(self.updateTotalVisibility)
        self.actionLoad.triggered.connect(self.loadBuild)

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
        charBuild.lineEditName.textEdited.connect(self.updateListName)

        self.setMaxVisibility(self.actionShowMax.isChecked(), charBuild)
        self.setCostVisibility(self.actionShowCost.isChecked(), charBuild)
        self.setTotalVisibility(self.actionShowTotal.isChecked(), charBuild)

        return charBuild

    def getNameList(self):
        nameList = []
        for i in range(self.listBuilds.count()):
            nameList.append(self.listBuilds.item(i).text())

        return nameList

    def saveCurrentSettings(self):
        settingsParser = ConfigParser.SafeConfigParser()
        settingsParser.add_section('window')
        settingsParser.set('window', 'width', str(self.width()))
        settingsParser.set('window', 'height', str(self.height()))

        settingsParser.add_section('options')
        settingsParser.set('options', 'total',
                           str(self.actionShowTotal.isChecked()))
        settingsParser.set('options', 'cost',
                           str(self.actionShowCost.isChecked()))
        settingsParser.set('options', 'max',
                           str(self.actionShowMax.isChecked()))

        path = os.path.join('saves', 'settings.absf')
        with open(path, 'w') as f:
            settingsParser.write(f)

    def loadSettings(self):
        settingsParser = ConfigParser.SafeConfigParser()
        settingsParser.read(os.path.join('saves', 'settings.absf'))

        self.resize(int(settingsParser.get('window', 'width')),
                    int(settingsParser.get('window', 'height')))

        self.actionShowTotal.setChecked(settingsParser.getboolean('options',
                                                                  'total'))
        self.actionShowCost.setChecked(settingsParser.getboolean('options',
                                                                 'cost'))
        self.actionShowMax.setChecked(settingsParser.getboolean('options',
                                                                'max'))
    @pyqtSlot(str)
    def updateListName(self, name):
        if name == '':
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Empty name')
            msgBox.setText('The name must contain at least one character')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec_()

            name = self.listBuilds.currentItem().text()
            self.stackedBuilds.currentWidget().lineEditName.setText(name)

        elif name in self.getNameList() and name != \
                                    str(self.listBuilds.currentItem().text()):
            oldName = self.listBuilds.currentItem().text()
            self.stackedBuilds.currentWidget().lineEditName.setText(oldName)

            msgBox = QMessageBox()
            msgBox.setWindowTitle('Name already exists')
            msgBox.setText('The name\n' + oldName + '\nalready exists.')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec_()

        else:
            self.listBuilds.currentItem().setText(name)

    @pyqtSlot()
    def getNewCharValues(self):
        newDialog = newdialog.NewDialog(self.getNameList())
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

    @pyqtSlot(bool)
    def updateMaxVisibility(self, visible):
        for i in range(self.stackedBuilds.count()):
            self.setMaxVisibility(visible, self.stackedBuilds.widget(i))

    def setMaxVisibility(self, visible, build):
        for skillBox in build.spDict.values() + \
                        build.tpDict.values() + \
                        build.qpDict.values():
                skillBox.labelMax.setVisible(visible)
                for skill in skillBox.skills.values():
                    skill.spinBoxMax.setVisible(visible)

    @pyqtSlot(bool)
    def updateCostVisibility(self, visible):
        for i in range(self.stackedBuilds.count()):
            self.setCostVisibility(visible, self.stackedBuilds.widget(i))

    def setCostVisibility(self, visible, build):
        for skillBox in build.spDict.values() + \
                        build.tpDict.values() + \
                        build.qpDict.values():
                skillBox.labelCost.setVisible(visible)
                for skill in skillBox.skills.values():
                    skill.spinBoxCost.setVisible(visible)

    @pyqtSlot(bool)
    def updateTotalVisibility(self, visible):
        for i in range(self.stackedBuilds.count()):
            self.setTotalVisibility(visible, self.stackedBuilds.widget(i))

    def setTotalVisibility(self, visible, build):
        for skillBox in build.spDict.values() + \
                        build.tpDict.values() + \
                        build.qpDict.values():
                skillBox.widgetSpacer.setVisible(visible)
                skillBox.labelTotal.setVisible(visible)
                for skill in skillBox.skills.values():
                    skill.line.setVisible(visible)
                    skill.spinBoxTotal.setVisible(visible)

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
            saveParser.set('global', 'path', build.path)
            saveParser.set('global', 'level', str(build.spinBoxLevel.value()))

            saveParser.add_section('Skills')
            for skillBox in build.spDict.values() + \
                            build.tpDict.values() + \
                            build.qpDict.values():
                for skill in skillBox.skills.values():
                    if skill.spinBoxLevel.value() > 0:
                        saveParser.set('Skills', skill.name,
                                       str(skill.spinBoxLevel.value()))

            path = os.path.join('saves', name + '.absf')

            with open(path, 'w') as f:
                saveParser.write(f)

            pathSaveParser.set('builds', name, path)

        path = os.path.join('saves', 'default.abpf')
        with open(path, 'w') as f:
            pathSaveParser.write(f)

    @pyqtSlot()
    def loadBuild(self, path=None):
        if path == None:
            path = QFileDialog.getOpenFileName(caption='Select build',
                                               filter='*.absf',
                                               directory='saves')
        loadParser = ConfigParser.SafeConfigParser()
        loadParser.read(str(path))
        picturePath = loadParser.get('global', 'path')
        mainClass = loadParser.get('global', 'class')
        subClass = loadParser.get('global', 'job')
        if not os.path.isfile(picturePath):
            picturePath = os.path.join("classes", mainClass, subClass + '.png')

        charBuild = self.createNewChar(loadParser.get('global', 'name'),
                                       mainClass, subClass, picturePath)

        charBuild.spinBoxLevel.setValue(int(loadParser.get('global', 'level')))

        for name in loadParser.options('Skills'):
            level = int(loadParser.get('Skills', name))
            skill = charBuild.findSkillByName(name)
            if skill != None:
                skill.spinBoxLevel.setValue(level)
            else:
                print name + ' could not be set, value is ' + str(level)

    @pyqtSlot('QEvent')
    def closeEvent(self, event):
        print self.size()
        self.saveCurrentSettings()
        self.saveBuilds()
        event.accept()


if __name__ == '__main__':
    import sys

    launchGui(sys.argv)
