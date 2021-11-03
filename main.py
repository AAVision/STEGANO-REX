
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_functions import *
## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow
from decode import Ui_MainWindow as new

from intro import Ui_MainWindow as intro
## ==> GLOBALS
counter = 0


class Second(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = new()
        self.ui.setupUi(self)
        
        ###checkk
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.decode_image(self))
        self.ui.back.clicked.connect(self.backk)
        self.ui.bmw.clicked.connect(lambda: UIFunctions.open_file(self))
        
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        #self.ui.bmw.clicked.connect(self.remove)
        self.ui.title_bar.mouseMoveEvent = moveWindow
        #pushButton.clicked.connect(self.clickk)

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
    def backk(self):
        self.main = Intro()     
        self.main.show()
        self.close()   
            
# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.get1(self))
        self.ui.pushButton_2.clicked.connect(lambda: UIFunctions.get2(self))
        self.ui.bmw.clicked.connect(lambda: UIFunctions.open_file(self))
        self.ui.back.clicked.connect(self.backk)
        

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        #self.ui.bmw.clicked.connect(self.remove)
        self.ui.title_bar.mouseMoveEvent = moveWindow
        #pushButton.clicked.connect(self.clickk)

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    def backk(self):
        self.main = Intro()     
        self.main.show()
        self.close()
        
    




# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> MODULES"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    
    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Intro()
            
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


class Intro(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = intro()
        self.ui.setupUi(self)
        self.ui.pushButton_encode.clicked.connect(self.swit1)
        self.ui.pushButton_decode.clicked.connect(self.swit2)
        self.ui.btn_maximize.hide()
        self.ui.bmw.clicked.connect(lambda: UIFunctions.open_file(self))
        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
    
        # SET TITLE BAR
        
        #self.ui.bmw.clicked.connect(self.remove)
        self.ui.title_bar.mouseMoveEvent = moveWindow
        #pushButton.clicked.connect(self.clickk)

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def swit1(self):
        self.main = MainWindow()     
        self.main.show()
        self.close()
        
    def swit2(self):
        self.main = Second()     
        self.main.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
    
