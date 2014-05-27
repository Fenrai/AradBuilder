from PyQt4.QtCore import (pyqtSlot)
from PyQt4.QtGui import (QDialog, QFileDialog, QPixmap, QMessageBox)

from pyui.NewChar_ui import Ui_NewCharacter as NewCharUI

import ConfigParser
import os

global paths

class NewDialog(QDialog, NewCharUI):

    def __init__(self, parent=None):
        super(NewDialog, self).__init__(parent)
        self.setupUi(self)

        classParser = ConfigParser.SafeConfigParser()
        classParser.read(os.path.join('classes', 'classes.abc'))
        self.comboClass.addItems(classParser.sections())
        self._subClasses = self.extractSubclasses(classParser)
        self._imageDirectory = ''
        self.updatePath()
        self.updateSubClassCombo()
        self.updateMainClassPictures()
        self.updateCharacterPicture()

        self.createConnections()

        print paths.getPicturePath('char', 'Gunner (F)')

    def extractSubclasses(self, classParser):
        subclassDict = {}

        for mainClass in classParser.sections():
            subClassList = []
            for sub in classParser.options(mainClass):
                subClass = classParser.get(mainClass, sub)
                if subClass != "":
                    subClassList.append(subClass)
            subclassDict[mainClass] = subClassList

        return subclassDict

    def createConnections(self):
        self.comboClass.currentIndexChanged.connect(self.updatePath)
        self.comboClass.currentIndexChanged.connect(self.updateSubClassCombo)
        self.comboClass.currentIndexChanged.connect(self.updateMainClassPictures)
        self.comboSubClass.currentIndexChanged.connect(self.updateCharacterPicture)
        self.toolButtonCustomPath.clicked.connect(self.editCustomPicturePath)
        self.lineEditCustomPicture.textChanged.connect(self.updateCharacterPicture)
        self.pushButtonCreate.clicked.connect(self.checkAccept)

    @pyqtSlot()
    def editCustomPicturePath(self):
        path = QFileDialog.getOpenFileName(caption='Path to your picture',
                                            filter='*.png *.jpg *.bmp')

        self.lineEditCustomPicture.setText(path)

    @pyqtSlot()
    def updatePath(self):
        self._imageDirectory = os.path.join('classes',
                                        str(self.comboClass.currentText()))

    @pyqtSlot()
    def updateSubClassCombo(self):
        classes = self._subClasses[str(self.comboClass.currentText())]
        self.comboSubClass.clear()
        self.comboSubClass.addItems(classes)

    @pyqtSlot()
    def updateMainClassPictures(self):
        path = os.path.join(self._imageDirectory, 'Classframe.png')
        self.labelClassPicture.setPixmap(QPixmap(path))
        path = os.path.join(self._imageDirectory, 'name.png')
        self.labelClassName.setPixmap(QPixmap(path))

    @pyqtSlot()
    def updateCharacterPicture(self):
        if self.sender() == self.lineEditCustomPicture \
        and self.lineEditCustomPicture.text() != '':
            path = self.lineEditCustomPicture.text()
            self.labelCharPicture.setPixmap(QPixmap(path))
        else:
            if self.lineEditCustomPicture.text() == '':
                path = os.path.join(self._imageDirectory,
                                str(self.comboSubClass.currentText()))
                self.labelCharPicture.setPixmap(QPixmap(path))

    @pyqtSlot()
    def checkAccept(self):
        if self.lineEditName.text() == '':
            msgBox = QMessageBox()
            msgBox.setWindowTitle('No Name')
            msgBox.setText('Your character needs a Name.')
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec_()
        else:
            self.accept()
