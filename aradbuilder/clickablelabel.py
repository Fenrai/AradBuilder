from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QLabel


class ClickableLabel(QLabel):
    doubleClicked = pyqtSignal()

    def __init__(self, parent=None):
        super(ClickableLabel, self).__init__(parent)

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()
