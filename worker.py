from cmath import sin
from turtle import pen
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog,QComboBox 
import sys
# from skimage.color import rgb2gray
from PyQt5 import QtCore, QtGui, QtWidgets 
from GUI import Ui_MainWindow
import logging
import qdarkstyle
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import pyqtgraph


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.pen1 = pyqtgraph.mkPen((0, 0, 255), width=3)
        self.pen2 = pyqtgraph.mkPen((0, 255, 0), width=3)

        self.gui.horizontalSlider.valueChanged.connect(self.probability)
        self.show()

        # Plot between -10 and 10 with .001 steps.
        self.x_axis = np.arange(0, 240, 1)
  
        # Calculating mean and standard deviation
        self.mean = 120
        self.sd = 20
        self.gui.main_graph.plotItem.plot(self.x_axis, norm.pdf(self.x_axis, self.mean, self.sd),pen=self.pen1)

    def probability(self):
        value = self.gui.horizontalSlider.value()
        self.gui.label_5.setText(str(value))

        probability_pdf = round(norm.cdf(value, loc=self.mean, scale=self.sd),8)
        self.gui.textEdit.setText(str(probability_pdf))
        new_x = self.x_axis[:value]
        self.gui.main_graph.plotItem.clear()
        self.gui.main_graph.plotItem.plot(self.x_axis[:value], norm.pdf(self.x_axis, self.mean, self.sd)[:len(new_x)],pen=self.pen2)
        self.gui.main_graph.plotItem.plot(self.x_axis[value:], norm.pdf(self.x_axis, self.mean, self.sd)[len(new_x):],pen=self.pen1)
        self.gui.main_graph.plotItem.addLine(x=value)


        
	# def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.gui = Ui_MainWindow()
    #     self.gui.setupUi(self)
	# 	# Load the ui file

	# 	# Define our widgets
	# 	self.button = self.findChild(QPushButton, "pushButton")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    Interpoltor = MainWindow()
    logger = logging.getLogger("main.py")
    logger.setLevel(level=logging.DEBUG)
    logging.basicConfig(filename="logging_file.log")
    logger.info("lunching of the Application ")
    sys.exit(app.exec_())