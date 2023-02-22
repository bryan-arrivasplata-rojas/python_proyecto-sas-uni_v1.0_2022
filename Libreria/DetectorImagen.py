import cv2,os,time,winsound,pyttsx3
import numpy as np
from PIL import Image
import pyzbar.pyzbar as pyzbar
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
error_dialog = QtWidgets.QErrorMessage()

engine = pyttsx3.init()
engine.setProperty("rate", 150)
camara = 0 #SIRVE PARA CUANDO HAY UNA SOLA CAMARA | SRIVE PARA CUANDO HAY DOS CAMARAS Y USARA LA PRIMERA
#camara = 1 #SIRVE PARA CUANDO HAY UNA DOS CAMARA Y USARA LA SEGUNDA
def IdentificadorImagen(direccion_imagenes,direccion_modelo,tipo):
    if tipo =="Rostro":
        cap = cv2.VideoCapture(camara)
        if cap.isOpened():
            dataPath = direccion_imagenes
            imagePaths = os.listdir(dataPath)
            fname = direccion_modelo
            if not os.path.isfile(fname):
                print("Entrenar la data primero")
                exit(0)
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(fname)
            faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
            inicio_de_tiempo = time.time()
            
            while True:
                tiempo_final = time.time()
                tiempo_transcurrido = tiempo_final - inicio_de_tiempo
                informacion = ""
                if (tiempo_transcurrido >= 10):
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    error_dialog.showMessage('Supero sus 10 segundos, intentelo nuevamente')
                    app.exec_()
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                ret,frame = cap.read()
                if ret == False: break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = gray.copy()
                faces = faceClassif.detectMultiScale(gray,1.3,5)
                cv2.imshow('frame',frame)
                for (x,y,w,h) in faces:
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                    result = recognizer.predict(rostro)
                    if result[1] < 80:
                        informacion = format(imagePaths[result[0]])
                        cap.release()
                        cv2.destroyAllWindows()
                        return informacion
                key = cv2.waitKey(1)
                if key == 27 or key ==ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            return informacion           
    elif tipo =="QR": 
        cap = cv2.VideoCapture(camara)
        if cap.isOpened():
            inicio_de_tiempo = time.time()
            while True:#s
                tiempo_final = time.time()
                tiempo_transcurrido = tiempo_final - inicio_de_tiempo
                if (tiempo_transcurrido >= 10):
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    error_dialog.showMessage('Supero sus 10 segundos, intentelo nuevamente')
                    app.exec_()
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                _, frame = cap.read() # detecta un codigo un qr

                decodedObjects = pyzbar.decode(frame) # decodifica el codigo qr a un mensaje ej.: 123456789/12345678
                for obj in decodedObjects:
                    codpas = str(obj.data) #s'123456789/12345678'
                    l = len(codpas)
                    try:
                        codpas = codpas[2:l - 1]
                        cap.release()
                        cv2.destroyAllWindows()
                        return codpas
                    except:
                        return 0
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1)
                if key == 27 or key ==ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            return 0
    return "Falla"
