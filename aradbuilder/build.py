from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QWidget, QPixmap, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QVBoxLayout, QFileDialog

from aradbuilder.questwidget import QuestWidget
from aradbuilder.skillbox import SkillBox
from pyui.Build_ui import Ui_WidgetBuild as BuildUi


class Build(QWidget, BuildUi):
    nameChanged = pyqtSignal(str)

    def __init__(self, name, mainClass, subClass, path, mainWindow, parent=None):
        super(Build, self).__init__(parent)
        self.setupUi(self)

        self.lineEditName.setText(name)
        self.mainWindow = mainWindow
        self.mainClass = mainClass
        self.subClass = subClass
        self.path = path
        self.lineEditClass.setText(mainClass)
        self.lineEditSubClass.setText(subClass)
        self.spinBoxLevel.lineEdit().setReadOnly(True)
        self.labelCharPicture.setPixmap(getPixmap(path))

        self.createObjects()
        self.fillSpTab()
        self.fillTpTab()
        self.fillQpTab()
        self.fillQuestTab()
        self.fillSkillTreeTab()
        self.createConnections()
        self.connectRequiredSkills()

        self.updateTotalPoints(self.spinBoxLevel.value())

    def createObjects(self):
        self.questWidget = QuestWidget()
        self.spDict = {}
        self.tpDict = {}
        self.qpDict = {}

    def createConnections(self):
        self.spinBoxLevel.valueChanged.connect(self.updateTotalPoints)
        self.lineEditName.editingFinished.connect(self.updateName)
        self.spinBoxSpTotal.valueChanged.connect(self.updateRemainingSP)
        self.spinBoxSpUsed.valueChanged.connect(self.updateRemainingSP)
        self.spinBoxTpTotal.valueChanged.connect(self.updateRemainingTP)
        self.spinBoxTpUsed.valueChanged.connect(self.updateRemainingTP)
        self.spinBoxQpTotal.valueChanged.connect(self.updateRemainingQP)
        self.spinBoxQpUsed.valueChanged.connect(self.updateRemainingQP)
        for skillBox in self.spDict.values() + \
                        self.tpDict.values() + \
                        self.qpDict.values():
            for skill in skillBox.skills.values():
                self.spinBoxLevel.valueChanged.connect(skill.updateMax)
        self.labelCharPicture.doubleClicked.connect(self.changePicture)

    def fillSpTab(self):
        spWidget = QWidget()
        spLayout = QVBoxLayout()

        generalBox = SkillBox('General', 'SP', 'General', 'SP')
        albertBox = SkillBox('Albert', 'SP', self.mainClass, self.subClass)
        commonBox = SkillBox('Common', 'SP', self.mainClass, 'Common')
        classBox = SkillBox('Class', 'SP', self.mainClass, self.subClass)

        spLayout.addLayout(getLayout(generalBox, albertBox))
        spLayout.addLayout(getLayout(commonBox))
        spLayout.addLayout(getLayout(classBox))
        spLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum,
                                           QSizePolicy.Expanding))

        self.spDict['General'] = generalBox
        self.spDict['Albert'] = albertBox
        self.spDict['Common'] = commonBox
        self.spDict['Class'] = classBox

        spWidget.setLayout(spLayout)
        self.scrollAreaSP.setWidget(spWidget)

        for skillBox in self.spDict.values():
            skillBox.totalChanged.connect(self.updateUsedSP)

    def fillTpTab(self):
        tpWidget = QWidget()
        tpLayout = QVBoxLayout()

        generalBox = SkillBox('General', 'TP', 'General', 'TP')
        commonBox = SkillBox('Common', 'TP', self.mainClass, 'Common')
        classBox = SkillBox('Class', 'TP', self.mainClass, self.subClass)

        tpLayout.addLayout(getLayout(generalBox))
        tpLayout.addLayout(getLayout(commonBox))
        tpLayout.addLayout(getLayout(classBox))
        tpLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum,
                                           QSizePolicy.Expanding))

        self.tpDict['General'] = generalBox
        self.tpDict['Common'] = commonBox
        self.tpDict['Class'] = classBox

        tpWidget.setLayout(tpLayout)
        self.scrollAreaTP.setWidget(tpWidget)

        for skillBox in self.tpDict.values():
            skillBox.totalChanged.connect(self.updateUsedTP)

    def fillQpTab(self):
        qpWidget = QWidget()
        qpLayout = QVBoxLayout()

        generalBox = SkillBox('General', 'QP', 'General', 'QP')

        qpLayout.addLayout(getLayout(generalBox))
        qpLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum,
                                           QSizePolicy.Expanding))

        self.qpDict['General'] = generalBox

        qpWidget.setLayout(qpLayout)
        self.scrollAreaQP.setWidget(qpWidget)

        for skillBox in self.qpDict.values():
            skillBox.totalChanged.connect(self.updateUsedQP)

    def fillQuestTab(self):
        self.scrollAreaQuests.setWidget(self.questWidget)
        self.questWidget.totalChanged.connect(self.updateTotalPoints)
        for quest in self.questWidget.quests.values():
            self.spinBoxLevel.valueChanged.connect(quest.updateState)
        self.tabWidget.removeTab(4)

    def fillSkillTreeTab(self):
        # until further notice
        self.tabWidget.removeTab(3)

    def findSkillByName(self, name):
        for skillBox in self.spDict.values() + \
                        self.tpDict.values() + \
                        self.qpDict.values():
            for skill in skillBox.skills.keys():
                if skill.lower() == name.lower():
                    return skillBox.skills[skill]
        print name + ' not found'
        return None

    def connectRequiredSkills(self):
        for skillBox in self.spDict.values() + \
                        self.tpDict.values() + \
                        self.qpDict.values():
            for skill in skillBox.skills.values():
                for name in skill.req:
                    req = self.findSkillByName(name)
                    req.dependants.setdefault(skill.req[name], []).append(skill)
                    skill.requirements[req] = skill.req[name]

    @pyqtSlot(int)
    def updateTotalPoints(self, level=0):
        if level == 0:
            level = self.spinBoxLevel.value()
        self.spinBoxTpTotal.setValue(self.mainWindow.dictTP[level] +
                                     self.questWidget.getTotalTP())
        self.spinBoxSpTotal.setValue(self.mainWindow.dictSP[level] +
                                     self.questWidget.getTotalSP())
        self.spinBoxQpTotal.setValue(self.questWidget.getTotalQP())

    @pyqtSlot()
    def updateUsedSP(self):
        used = 0
        for skillBox in self.spDict.values():
            used += skillBox.total
        self.spinBoxSpUsed.setValue(used)

    @pyqtSlot()
    def updateUsedTP(self):
        used = 0
        for skillBox in self.tpDict.values():
            used += skillBox.total
        self.spinBoxTpUsed.setValue(used)

    @pyqtSlot()
    def updateUsedQP(self):
        used = 0
        for skillBox in self.qpDict.values():
            used += skillBox.total
        self.spinBoxQpUsed.setValue(used)

    @pyqtSlot()
    def updateRemainingSP(self):
        self.spinBoxSpRemaining.setValue(self.spinBoxSpTotal.value() -
                                         self.spinBoxSpUsed.value())

    @pyqtSlot()
    def updateRemainingTP(self):
        self.spinBoxTpRemaining.setValue(self.spinBoxTpTotal.value() -
                                         self.spinBoxTpUsed.value())

    @pyqtSlot()
    def updateRemainingQP(self):
        self.spinBoxQpRemaining.setValue(self.spinBoxQpTotal.value() -
                                         self.spinBoxQpUsed.value())

    @pyqtSlot()
    def updateQuestPoints(self):
        pass

    @pyqtSlot()
    def updateName(self):
        self.nameChanged.emit(str(self.lineEditName.text()))

    @pyqtSlot()
    def changePicture(self):
        path = QFileDialog.getOpenFileName(caption='Path to your picture',
                                            filter='*.png *.jpg *.bmp *.gif')
        if path != '':
            self.path = str(path)
            self.labelCharPicture.setPixmap(self.getPixmap(path))

def getPixmap(path):
    pixmap = QPixmap(path)
    if pixmap.width() > 300 or pixmap.height() > 200:
        return pixmap.scaled(300, 200)
    return pixmap

def getLayout(skillBox1, skillBox2=None):
    layout = QHBoxLayout()
    layout.addWidget(skillBox1)
    layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding,
                                     QSizePolicy.Minimum))
    if skillBox2:
        layout.addWidget(skillBox2)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding,
                                         QSizePolicy.Minimum))
    layout.setContentsMargins(0, 0, 0, 0)

    return layout

def copyBuild(original, name):
    copy = Build(name, original.mainClass, original.subClass, original.path,
                 original.mainWindow)
    for skillBox in original.spDict.values() + \
                            original.tpDict.values() + \
                            original.qpDict.values():
        for skill in skillBox.skills.values():
            value = skill.spinBoxLevel.value()
            if value > 0:
#                 cSkill = copy.findSkillByName(skill.name)
                copy.findSkillByName(skill.name).spinBoxLevel.setValue(value)
    return copy

