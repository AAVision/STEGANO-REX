
## ==> GUI FILE
from main import *
from PyQt5.QtWidgets import QFileDialog,QLabel
from PyQt5.QtGui import QPixmap
import os
import win32api
from CodeUPDATED import encod,decodee
import time
import subprocess
from os import path
import cv2
import webbrowser

## ==> GLOBALS

GLOBAL_STATE = 0
imagePath=""
imagePath2=""
timestamp=""
imagePath_dec=""

class UIFunctions(MainWindow):
    def clickk():
        print("ALII")
    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")
    def load_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "OpenFile", "", "")
        if image_path:
            updatedImage = Updated_encrypt.decrypt(image_path, 123)
            pixmap = QPixmap(updatedImage)
            self.image_lbl.setPixmap(QPixmap(pixmap))
    
    def open_file(self):
        
        webbrowser.open('https://ali.jprq.live/FYP/Image_Upoad_PHP/')  
    
    def decode_image(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', 
        os.getcwd(),"Image files (*.jpg *png)")
        global imagePath_dec
        
        
        imagePath_dec = fname[0]
        if not imagePath_dec:
            win32api.MessageBox(0, 'Empty paths', 'Warning')
            self.ui.bmw.setIcon(QIcon('help_16px.png'))
        else:
            self.ui.pushButton.setIcon(QIcon('ok_24px.png'))
            timestamp = round(time.time() * 1000)
            check = decodee("4",imagePath_dec,"Hidden_IM_"+str(timestamp)+".png")
            
            if path.exists("Hidden_IM_"+str(timestamp)+".png") and check == "Done":
                win32api.MessageBox(0, 'Done', 'Completed')
                self.ui.label_13.setText("You can Check Hidden image as :" + "Hidden_IM_"+str(timestamp)+".png")
            elif check == "Error!":
                win32api.MessageBox(0, 'Somethimg Went Wrong', 'ERROR!')
                
            
    def get1(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', 
         os.getcwd(),"Image files (*.jpg *png)")
        global imagePath
        imagePath = fname[0]
        if imagePath:
            self.ui.pushButton.setIcon(QIcon('ok_24px.png'))
        else:
            self.ui.bmw.setIcon(QIcon('help_16px.png'))
            
            #self.ui.pushButton_3.setStyleSheet("background-image : url(2.png);  border: 1px solid #ddd;border-radius: 4px;	width: 150px;height: 300px;border-radius: 30px;") 
            #self.ui.pushButton.setText(imagePath)  
        
        #self.plainTextEdit.setText(imagePath)
        #self.plainTextEdit.adjustSize()

    def get2(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', 
        os.getcwd(),"Image files (*.jpg *png)")
        global imagePath
        global imagePath2
        global timestamp
        imagePath2 = fname[0]
        if not imagePath or not imagePath2:
            win32api.MessageBox(0, 'Empty paths', 'Warning')
            self.ui.bmw.setIcon(QIcon('help_16px.png'))
        else:
            self.ui.pushButton_2.setIcon(QIcon('ok_24px.png'))
            im = cv2.imread(imagePath)
            im2 = cv2.imread(imagePath2)
            h, w, c = im.shape
            h2, w2, c2 = im2.shape
            if h2*w2*c2 > h * w *c :
                win32api.MessageBox(0, 'Hidden image is greater than the original', 'ERROR!')
            else:
                timestamp = round(time.time() * 1000)
                encod(imagePath,imagePath2,"4","IM_"+str(timestamp)+".jpg")
                if path.exists("IM_"+str(timestamp)+".png"):
                    win32api.MessageBox(0, 'Done', 'Completed')
                    self.ui.label_13.setText("You can Check the image as :" + "IM_"+str(timestamp)+".png")
                else:
                    win32api.MessageBox(0, 'Somethimg Went Wrong', 'ERROR!')
                
            """p=subprocess.Popen(['python', 'Code.py', 'encode',
        '-i', imagePath , '-o', 'aa.jpg', '-f', imagePath2,'-l','4'], stdout=subprocess.PIPE)
            text = p.communicate()[0].decode('utf-8')
            for i in text.splitlines():
                if "Output file changed to" in i:
                    win32api.MessageBox(0, ' TRUE', 'TRUE')"""
        #os.system("Code.py encode -i "+imagePath+" -o aa.jpg -f "+imagePath2)
        
        
    ## ==> UI DEFINITIONS
    
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE 
        self.ui.btn_maximize.clicked.connect(lambda: self.showMinimized())
        
        
        #self.ui.pushButton_3.clicked.connect(lambda: UIFunctions.ali(self))
        
        # MINIMIZE 
        self.ui.btn_minimize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())
        

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")



    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE