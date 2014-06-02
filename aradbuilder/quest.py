from PyQt4.QtGui import QCheckBox

class Quest(QCheckBox):
    def __init__(self, name, questParser, parent=None):
        super(Quest, self).__init__(parent)
        self.name = name
        self.setText(self.name)
        self.qp = int(questParser.get(name, 'qp'))
        self.sp = int(questParser.get(name, 'sp'))
        self.tp = int(questParser.get(name, 'tp'))
        self.setChecked(True)