from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QCheckBox

class Quest(QCheckBox):
    statusChanged = pyqtSignal()

    def __init__(self, name, questParser, parent=None):
        super(Quest, self).__init__(parent)
        self.name = name
        self.setText(self.name)
        self.qp = int(questParser.get(name, 'qp'))
        self.sp = int(questParser.get(name, 'sp'))
        self.tp = int(questParser.get(name, 'tp'))
        self.level = int(questParser.get(name, 'level'))
        self.setChecked(True)

    @pyqtSlot(int)
    def updateState(self, level):
        if level < self.level and self.isEnabled():
            self.setDisabled(True)
            self.statusChanged.emit()
        elif level >= self.level and not self.isEnabled():
            self.setEnabled(True)
            self.statusChanged.emit()
