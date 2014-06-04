from PyQt4.QtGui import QWidget, QGridLayout
from PyQt4.QtCore import pyqtSignal
import ConfigParser
import os
from aradbuilder.quest import Quest
class QuestWidget(QWidget):
    totalChanged = pyqtSignal()

    def __init__(self, parent=None):
        super(QuestWidget, self).__init__(parent)
        questParser = ConfigParser.SafeConfigParser()
        questParser.read(os.path.join('skills', 'Quests.abq'))
        self.quests = {}

        mainLayout = QGridLayout()

        for i, name in enumerate(questParser.sections()):
            quest = Quest(name, questParser)
            quest.statusChanged.connect(self.totalChanged.emit)
            quest.stateChanged.connect(self.totalChanged.emit)
            self.quests[name] = quest
            mainLayout.addWidget(quest, i // 2, i % 2)

        self.setLayout(mainLayout)

    def getTotalQP(self):
        total = 0
        for quest in self.quests.values():
            if quest.isChecked() and quest.isEnabled():
                total += quest.qp
        return total

    def getTotalSP(self):
        total = 0
        for quest in self.quests.values():
            if quest.isChecked() and quest.isEnabled():
                total += quest.sp
        return total

    def getTotalTP(self):
        total = 0
        for quest in self.quests.values():
            if quest.isChecked() and quest.isEnabled():
                total += quest.tp
        return total