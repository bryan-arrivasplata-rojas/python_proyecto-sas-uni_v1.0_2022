'''import numpy as np
from PIL import Image
import pyzbar.pyzbar as pyzbar
import webbrowser as wb
from string import ascii_uppercase
from openpyxl import Workbook
from arrow import utcnow'''
'''import sys,pyttsx3
#from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTime, QTimer
from Interfaces.Inicio import Login
from Interfaces.Menu import Menu_Principal,Seleccionar_Clase
from Interfaces.Reportes import Reporte_AH,Reporte_AS,Reporte_LI,Reporte_RC,Reporte_RM,Reporte_RS'''
from Libreria.Execfile import *
from Libreria.RutaExactaPath import *




'''engine = pyttsx3.init()
engine.setProperty("rate", 150)
camara = 0 #SIRVE PARA CUANDO HAY UNA SOLA CAMARA | SRIVE PARA CUANDO HAY DOS CAMARAS Y USARA LA PRIMERA'''
#camara = 1 #SIRVE PARA CUANDO HAY UNA DOS CAMARA Y USARA LA SEGUNDA
if __name__ == "__main__":
    path = resolver_ruta("Interfaces/Inicio/Login.py")
    execfile(path)
