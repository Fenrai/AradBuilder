from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QWidget, QPixmap, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QVBoxLayout

from aradbuilder.skillbox import SkillBox
from pyui.Build_ui import Ui_WidgetBuild as BuildUi


class Build(QWidget, BuildUi):
    nameChanged = pyqtSignal(str)

    def __init__(self, name, mainClass, subClass, path, mainWindow, parent=None):
        super(Build, self).__init__(parent)
        self.setupUi(self)

        self.lineEditName.setText(name)
        self._mainWindow = mainWindow
        self.mainClass = mainClass
        self.subClass = subClass
        self.lineEditClass.setText(mainClass)
        self.lineEditSubClass.setText(subClass)
        self.spinBoxLevel.lineEdit().setReadOnly(True)
        self.labelCharPicture.setPixmap(QPixmap(path))
        self.updateTotalPoints(self.spinBoxLevel.value() - 1)

        self.createObjects()
        self.fillSpTab()
        self.fillTpTab()
        self.fillQpTab()
        self.fillQuestTab()
        self.fillSkillTreeTab()
        self.createConnections()


    def createObjects(self):
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
        for skillBox in self.spDict.values():
            for skill in skillBox.skills.values():
                if skill.requirements != {}:
                    skill.updateRequirements.connect(self.setRequirements)
                self.spinBoxLevel.valueChanged.connect(skill.updateMax)

    def fillSpTab(self):
        spWidget = QWidget()
        spLayout = QVBoxLayout()

        generalBox = SkillBox('General', 'SP', 'General', 'SP')
        commonBox = SkillBox('Common', 'SP', self.mainClass, self.subClass)
        classBox = SkillBox('Class', 'SP', self.mainClass, self.subClass)

        spLayout.addLayout(self.getLayout(generalBox))
        spLayout.addLayout(self.getLayout(commonBox))
        spLayout.addLayout(self.getLayout(classBox))
        spLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum,
                                           QSizePolicy.Expanding))

        self.spDict['General'] = generalBox
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
        commonBox = SkillBox('Common', 'TP', self.mainClass, self.subClass)
        classBox = SkillBox('Class', 'TP', self.mainClass, self.subClass)

        tpLayout.addLayout(self.getLayout(generalBox))
        tpLayout.addLayout(self.getLayout(commonBox))
        tpLayout.addLayout(self.getLayout(classBox))
        tpLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum,
                                           QSizePolicy.Expanding))

        self.tpDict['General'] = generalBox
        self.tpDict['Common'] = commonBox
        self.tpDict['Class'] = classBox

        tpWidget.setLayout(tpLayout)
        self.scrollAreaTP.setWidget(tpWidget)

        generalBox.totalChanged.connect(self.updateUsedTP)
        commonBox.totalChanged.connect(self.updateUsedTP)
        classBox.totalChanged.connect(self.updateUsedTP)

    def fillQpTab(self):
        qpWidget = QWidget()
        qpLayout = QVBoxLayout()

        generalBox = SkillBox('General', 'QP', 'General', 'QP')

        qpLayout.addLayout(self.getLayout(generalBox))
        qpLayout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum,
                                           QSizePolicy.Expanding))

        self.qpDict['General'] = generalBox

        qpWidget.setLayout(qpLayout)
        self.scrollAreaQP.setWidget(qpWidget)

        generalBox.totalChanged.connect(self.updateUsedQP)

    def fillQuestTab(self):
        questWidget = QWidget()
        questLayout = QVBoxLayout()

        # insert Quests Magic here

        questWidget.setLayout(questLayout)
        self.scrollAreaQuests.setWidget(questWidget)

    def fillSkillTreeTab(self):
        # until further notice
        self.tabWidget.removeTab(3)

    def getLayout(self, skillBox):
        layout = QHBoxLayout()
        layout.addWidget(skillBox)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Expanding,
                                         QSizePolicy.Minimum))
        layout.setContentsMargins(0, 0, 0, 0)

        return layout

    def findSkillByName(self, name):
        for skillBox in self.spDict.values() + \
                        self.tpDict.values() + \
                        self.qpDict.values():
            if name in skillBox.skills.keys():
                return skillBox.skills[name]
        return None

    @pyqtSlot(int)
    def updateTotalPoints(self, level):
        self.spinBoxTpTotal.setValue(self._mainWindow.dictTP[level])
        self.spinBoxSpTotal.setValue(self._mainWindow.dictSP[level])

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

    @pyqtSlot(dict)
    def setRequirements(self, rDict):
        print rDict
        print self.spDict['General'].skills['Leap']
        self.spDict['General'].skills['Leap'].spinBoxLevel.setValue(10)
        for name in rDict.keys():
            print type(rDict[name])
            print self.findSkillByName(name)
            self.findSkillByName(name).spinBoxLevel.setValue(5)


