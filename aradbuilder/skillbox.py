import ConfigParser
import os

from PyQt4.QtCore import pyqtSignal, pyqtSlot
from PyQt4.QtGui import QGroupBox

import aradbuilder.paths as paths
from aradbuilder.skill import Skill
from pyui.SkillBox_ui import Ui_SkillBox as SkillBoxUi


class SkillBox(QGroupBox, SkillBoxUi):
    totalChanged = pyqtSignal()

    def __init__(self, title, points, mainClass, subClass, parent=None):
        super(SkillBox, self).__init__(parent)
        self.setupUi(self)

        self.setTitle(title)

        self.createObjects()
        self.createConnections()
        self.createSkills(points, mainClass, subClass)

    def createObjects(self):
        self.total = 0
        self.skills = {}

    def createConnections(self):
        pass

    def createSkills(self, points, main, sub):
        p = paths.Paths()

        mainDir = p.getFilePath(main)

        if main == 'General':
            filePath = os.path.join(mainDir, points + '.abs')
            picDir = os.path.join(mainDir, sub)
        elif self.title() == 'Albert':
            filePath = os.path.join(mainDir, 'SP_Albert.abs')
            picDir = os.path.join(mainDir, 'Common')
        else:
            filePath = os.path.join(mainDir, points + '_' + sub + '.abs')
            picDir = os.path.join(mainDir, sub)

        skillParser = ConfigParser.SafeConfigParser()
        skillParser.read(filePath)

        skills = skillParser.sections()

        if self.title() == 'Albert':
            for skill in skills:
                if skillParser.get(skill, 'job') == sub:
                    skills.remove(skill)

        for skillName in skills:
            skill = Skill(skillName, skillParser, picDir)
            self.mainLayout.addWidget(skill)
            self.skills[skillName] = skill
            skill.totalChanged.connect(self.updateTotal)

    def updateTotal(self):
        self.total = 0
        for skill in self.skills.values():
            self.total += skill.spinBoxTotal.value()

        self.totalChanged.emit()
