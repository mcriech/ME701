#!/usr/bin/python2.7
import sys
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        """ MENU BAR SETUP """
        
        """ FILE MENU """
        self.menuFile = self.menuBar().addMenu("&File")
        self.actionSaveAs = QAction("&Save As", self)
        self.connect(self.actionSaveAs, SIGNAL("triggered()"), self.saveas) 
        self.actionExit= QAction("&Exit", self)
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
    
    def saveas(self) :
        fname = unicode(QFileDialog.getSaveFileName(self, "Save as..."))
        """ Do something with data """
        
    def about(self) :
        QMessageBox.about(self, "About Function Evaluator",
                          "This is my help message.")
class Form(QDialog) :
    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
        self.plot = MatplotlibCanvas()
        
        self.function_edit = QLineEdit("f(x) = ...")
        self.function_edit.selectAll()
        
        self.parameter_edit = QLineEdit("x = ...")
        self.parameter_edit.selectAll()
        
        self.output_edit = QLineEdit("output = ...")
        self.output_edit.selectAll()
        
        self.minimum_edit = QLineEdit("plot min x = ...")
        self.minimum_edit.selectAll()

        self.maximum_edit = QLineEdit("plot max x = ...")
        self.maximum_edit.selectAll()       
        
        self.step_edit = QLineEdit("plot number of steps = ...")
        self.step_edit.selectAll() 
        
        self.execute_btn = QPushButton('Execute', self)
        self.execute_btn.clicked.connect(self.updateUI)
        
        self.plot_btn = QPushButton('Plot', self)
        self.plot_btn.clicked.connect(self.update_plot)
        
        """ Create the Layout """
        layout = QGridLayout()
        layout.addWidget(self.plot, 0, 0, 1, 0)
        layout.addWidget(self.function_edit, 2, 0)
        layout.addWidget(self.minimum_edit, 2, 1)
        layout.addWidget(self.parameter_edit, 3, 0)
        layout.addWidget(self.maximum_edit, 3, 1)
        layout.addWidget(self.output_edit, 4, 0)
        layout.addWidget(self.step_edit, 4, 1)
        layout.addWidget(self.execute_btn, 5, 0)
        layout.addWidget(self.plot_btn, 5, 1)
        self.setLayout(layout)
        self.function_edit.setFocus()
        self.connect(self.output_edit, SIGNAL("returnPressed()"),
                     self.updateUI)
        self.connect(self.step_edit, SIGNAL("returnPressed()"),
                     self.update_plot)
        self.setWindowTitle("Function Evaluator")

    def updateUI(self) :
        
        try :
            x = np.array(eval(str(self.parameter_edit.text())))
            f = eval(str(self.function_edit.text()))
            f_s = str(f).replace("[","").replace("]","").replace(" ", ", ")
            self.output_edit.setText(f_s)
        except :
            self.output_edit.setText("I can't code")
            
    def update_plot(self):
        
        try :
            minimum = float(eval(str(self.minimum_edit.text())))
            maximum = float(eval(str(self.maximum_edit.text())))
            step_size = ((maximum - minimum)/int(eval(str(self.step_edit.text()))))
            x = np.arange(minimum, 
                          maximum + step_size, 
                          step_size)
            f = eval(str(self.function_edit.text()))
            self.plot.update_plot(x, f)
        except :
            self.output_edit.setText("Plotting Error")
  
class MatplotlibCanvas(FigureCanvas) :
    """ This is borrowed heavily from the matplotlib documentation;
        specifically, see:
        http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
    """
    def __init__(self, parent=None, width=5, height=4, dpi=100) :
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        f = np.sin(2*np.pi*t)
        self.axes.plot(t, f)
        self.axes.set_xlabel('t')
        self.axes.set_ylabel('f(t)')     
        
    def update_plot(self, x, f):
        self.axes.plot(x, f)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('f(x)')
        self.draw()

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()
