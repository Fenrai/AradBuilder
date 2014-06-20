from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget

from pyui.Loading_ui import Ui_Load as LoadUi


class SplashScreen (QWidget, LoadUi):
    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)

    def setPixmap(self, pixmap):
        self.labelPicture.setPixmap(pixmap)

    def showMessage(self, message):
        self.labelText.setText(message)
