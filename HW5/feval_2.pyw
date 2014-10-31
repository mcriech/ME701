#!/usr/bin/python2.7
import sys
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from form import Form

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        """ MENU BAR SETUP """
        
        """ FILE MENU """
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.connect(self.actionSaveAs, SIGNAL("triggered()"), self.saveas)
        self.actionExit = QAction("&Exit", self)
        self.connect(self.actionExit, SIGNAL("triggered()"), self.close)
        self.menuFile.addActions([self.actionSaveAs, self.actionExit])
        
        """ HELP MENU """
        self.menuHelp = self.menuBar().addMenu("&Help")
        self.actionAbout = QAction("&About", self)
        self.connect(self.actionAbout, SIGNAL("triggered()"), self.about)
        self.menuHelp.addActions([self.actionAbout])
        
        """ CENTRAL WIDGET """
        self.form = Form()
        self.setCentralWidget(self.form)
        
    def about(self):
        QMessageBox.about(self, "About Function Evaluator",
                    "This is my help message")
    
    def saveas(self):
        fname = unicode(QFileDialog.getSaveFileName(self, "Save as..."))
        """ Do something with the data """
        
    
    
app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()