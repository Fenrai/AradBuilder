import ast
import os

from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QWidget, QPixmap

from pyui.Skill_ui import Ui_Skill as SkillUi


class Skill(QWidget, SkillUi):
    totalChanged = pyqtSignal()
    updateRequirements = pyqtSignal(int)

    def __init__(self, name, skillParser, picDir, parent=None):
        super(Skill, self).__init__(parent)
        self.setupUi(self)

        self.name = name
        self.createObjects(skillParser, picDir)
        self.setValues()
        self.createConnections()
        self.labelPic.setPixmap(self.active)
        self.labelPic.setToolTip('<b>' + self.name + '</b><br></br>' + \
                                    skillParser.get(self.name, 'desc'))

    def createObjects(self, skillParser, picDir):
        self.start = int(skillParser.get(self.name, 'start'))
        self.max = int(skillParser.get(self.name, 'max'))
        self.interval = int(skillParser.get(self.name, 'interval'))
        self.cost1 = int(skillParser.get(self.name, 'cost1'))
        self.cost = int(skillParser.get(self.name, 'cost'))
        self.active = QPixmap(os.path.join(picDir,
                                           skillParser.get(self.name, 'active')))
        self.inactive = QPixmap(os.path.join(picDir,
                                             skillParser.get(self.name, 'inactive')))
        self.req = ast.literal_eval(skillParser.get(self.name, 'requirements'))
        self.dependants = {}
        self.requirements = {}

    def setValues(self):
        self.spinBoxMax.setValue(self.max)
        self.spinBoxLevel.setMaximum(self.max)
        self.updateCost()
        self.updateTotal()

    def createConnections(self):
        self.spinBoxMax.valueChanged.connect(self.spinBoxLevel.setMaximum)
        self.spinBoxMax.valueChanged.connect(self.updatePicture)
        self.spinBoxLevel.valueChanged.connect(self.updateTotal)
        self.spinBoxLevel.valueChanged.connect(self.updateCost)
        self.spinBoxLevel.valueChanged.connect(self.updateDependants)

    @pyqtSlot()
    def updatePicture(self):
        if self.spinBoxMax.value() == 0:
            self.labelPic.setPixmap(self.inactive)
        elif self.spinBoxMax.value() == 1:
            self.labelPic.setPixmap(self.active)

    @pyqtSlot()
    def updateTotal(self):
        if self.spinBoxTotal.value() == 0:
            for skill in self.requirements.keys():
                skill.setRequirement(self.requirements[skill])
        if self.spinBoxLevel.value() > 0:
            total = (self.spinBoxLevel.value() - 1) * self.cost + self.cost1
        else:
            total = 0

        self.spinBoxTotal.setValue(total)
        self.totalChanged.emit()

    @pyqtSlot()
    def updateCost(self):
        if self.spinBoxLevel.value() == 0:
            self.spinBoxCost.setValue(self.cost1)
        else:
            self.spinBoxCost.setValue(self.cost)

    @pyqtSlot()
    def updateDependants(self):
        for entry in self.dependants.keys():
            if entry > self.spinBoxLevel.value():
                for dependant in self.dependants[entry]:
                    dependant.spinBoxLevel.setValue(0)

    @pyqtSlot(int)
    def updateMax(self, level):
        if level < self.start:
            maximum = 0
        else:
            maximum = (level - self.start) / self.interval + 1

        if maximum > self.max:
            maximum = self.max

        self.spinBoxMax.setValue(maximum)

    @pyqtSlot(int)
    def setRequirement(self, level):
        self.spinBoxLevel.setValue(max(level, self.spinBoxLevel.value()))
