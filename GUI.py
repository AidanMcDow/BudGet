from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QComboBox, QGroupBox, QHBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys
from main import addBudGet

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'The Coin Project'
        self.left = 650
        self.top = 250
        self.width = 800
        self.height = 500
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.horizontalLayout()
        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
        sys.exit(app.exec_())

    def horizontalLayout(self):
        self.horizontalGroupBox = QGroupBox()
        hlay = QHBoxLayout()

        balancebt = QPushButton("Balance", self)
        balancebt.setFixedSize(QtCore.QSize(300, 80))

        #Button
        addbt = QPushButton("Spent", self)
        addbt.setFixedSize(QtCore.QSize(300, 80))

        hlay.addWidget(balancebt)
        hlay.addWidget(addbt)
        self.horizontalGroupBox.setLayout(hlay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()