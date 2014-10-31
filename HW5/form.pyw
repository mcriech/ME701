#!/usr/bin/python2.7
import sys
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Form(QDialog) :
    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
        self.functions = [None]
        self.add_functions()
        self.function_edit = QComboBox()
        self.function_edit.addItems(self.functions)
                
        self.parameter_edit = QLineEdit("x = ...")
        self.parameter_edit.selectAll()
        
        self.output_edit = QLineEdit("output = ...")
        self.output_edit.selectAll()
        
        self.execute_btn = QPushButton('Execute', self)
        self.execute_btn.clicked.connect(self.updateUI)
        
        layout = QVBoxLayout()
        layout.addWidget(self.function_edit)
        layout.addWidget(self.parameter_edit)
        layout.addWidget(self.output_edit)
        layout.addWidget(self.execute_btn)
        self.setLayout(layout)
        
        self.function_edit.setFocus()
        
        self.connect(self.output_edit, SIGNAL("returnPressed()"),
                     self.updateUI)
        
        self.setWindowTitle("Function Evaluator")

    def add_functions(self):
        self.functions = ['x + 2',
                          'x*2',
                          'x**2',
                          'sin(' + 'x' + ')'
                          ]

    def updateUI(self) :
        
        try :
            x = float(self.parameter_edit.text())
            f =   str(eval(str(self.function_edit.currentText())))
            self.output_edit.setText(f)
        except :
            self.output_edit.setText("Err....orrrrr")