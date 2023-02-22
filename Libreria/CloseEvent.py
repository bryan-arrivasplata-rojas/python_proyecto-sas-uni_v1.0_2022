from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import *
def closeEvent(self, event):
    reply = QMessageBox.question(self,
                                 'Events - Slot',
                                 "Realmente desea cerrar la aplicacion",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()