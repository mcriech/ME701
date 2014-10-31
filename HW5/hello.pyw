#!/usr/bin/python2.7

import sys
from PyQt4.QtGui import *
app = QApplication(sys.argv)
widget = QLabel("<font size=100 color='red'>Hello World!</font>")
widget.show()
sys.exit(app.exec_())



