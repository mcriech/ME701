#!/usr/bin/python2.7
import sys
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Form(QLabel) :
    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
        self.function_edit = QLineEdit("f(x) = ...")
        self.function_edit.selectAll()
        self.parameter_edit = QLineEdit("x = ...")
        self.parameter_edit.selectAll()
        self.output_edit = QLineEdit("output = ...")
        self.output_edit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.function_edit)
        layout.addWidget(self.parameter_edit)
        layout.addWidget(self.output_edit)
        self.setLayout(layout)
        self.function_edit.setFocus()
        self.connect(self.output_edit, SIGNAL("returnPressed()"),
                     self.updateUI)
        self.setWindowTitle("Function Evaluator")

    def updateUI(self) :
        
        try :
            x = float(self.parameter_edit.text())
            f =   str(eval(str(self.function_edit.text())))
            self.output_edit.setText(f)
        except :
            self.output_edit.setText("I can't code")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
